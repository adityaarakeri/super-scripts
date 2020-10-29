$ErrorActionPreference 	= 'Continue'
$DebugPreference 		= 'Continue'

try {

	Add-Type -AssemblyName System.Windows.Forms
	Add-Type -AssemblyName System.Drawing
	Add-Type -AssemblyName PresentationFramework
	Add-Type -AssemblyName System.Management.Automation
	
	
	<#
	Remove comments to hide console. 

	if (-not ("Console.Window" -as [type])) { 

		Add-Type -Name Window -Namespace Console -MemberDefinition '
		[DllImport("Kernel32.dll")]
		public static extern IntPtr GetConsoleWindow();

		[DllImport("user32.dll")]
		public static extern bool ShowWindow(IntPtr hWnd, Int32 nCmdShow);
		'
	}

	$consolePtr = [Console.Window]::GetConsoleWindow()
	$null = [Console.Window]::ShowWindow($consolePtr, 0)
	#>

	$Error.Clear()
	Get-PSSession | Remove-PSSession
	if(!(Get-Module -Name ExchangeOnlineManagement))
	{
		Import-Module -Name ExchangeOnlineManagement 
	} 

	$cfg = Import-Clixml -Path ".\additional\config.xml"

	$credential     		= Get-Credential
    
	$global:Session
	$mailDomain 			= $cfg.MailDomain;
	$global:Department 		= $cfg.Department;

	$global:forwardedCollec = New-Object System.Collections.ObjectModel.ObservableCollection[String]
	$global:extended
	
	$timer = New-Object System.Windows.Forms.Timer
	$timer.Interval = 500

	$loc = $cfg.ContentPath
	Set-Variable -Name extended -Value 1 -Scope Global -Force
	
	#  Add a better how-to window. 
	$instructString = @("--ENTER INSTRUCTIONS HERE")


	[System.Drawing.Icon]$mailIcon  = [System.Drawing.Icon]::new("$($loc)\graphics\Mail_.ico", 256, 256) #
		
	$mainForm 					= New-Object System.Windows.Forms.Form
	$mainForm.Text 				= "Email Forwarding [$($Department)]"
	$mainForm.Width 			= 550
	$mainForm.Height 			= 380
	$mainForm.FormBorderStyle	="FixedSingle"
	#$mainForm.ControlBox
	#$mainForm.Icon = new-object System.Drawing.Icon($mailIcon)
	$mainForm.Icon = $mailIcon
	$arrowIcon 					= New-Object System.Drawing.Bitmap("$($loc)\graphics\arrow.png")

	$arrowClick 				= New-Object System.Windows.Forms.Button 
	$arrowClick.Location 		= New-Object System.Drawing.Point(225, 310)
	$arrowClick.FlatStyle 		= "Flat"
	
	$arrowClick.Image 			= $arrowIcon
	$arrowClick.BackColor 		= [System.Drawing.Color]::Transparent
	$arrowClick.ForeColor 		= [System.Drawing.Color]::Transparent

	$mainForm.Controls.Add($arrowClick)


    ###############################################################################
	#Current Forwarding List
	###############################################################################
	$currentForwardingLbl = New-Object System.Windows.Forms.Label;
	$currentForwardingLbl.Text = "Active Forwarding: "
	$currentForwardingLbl.Location = New-Object System.Drawing.Point(30, 120)
	$currentForwardingLbl.Width = 200
	$currentForwardingLbl.BringToFront()
	$currentForwardingLi = New-Object System.Windows.Forms.ListBox;
	#$currentForwardingLi.Items.AddRange($testRange);
	$currentForwardingLi.DataSource = $forwardedCollec
	$currentForwardingLi.Width = 480
	$currentForwardingLi.Height = 160
	$currentForwardingLi.Location = New-Object System.Drawing.Point(30, 145)

	$menuStrip 					= New-Object System.Windows.Forms.ContextMenuStrip
	$menuStrip.Items.Add("Remove Forwarding")
	
	$currentForwardingLi.ContextMenuStrip = $menuStrip
	$selectedUserField 			= New-Object System.Windows.Forms.TextBox
	$selectedUserField.Location = New-Object System.Drawing.Point(30, 40)
	$selectedUserField.Width 	= 90


	$selectedUserLbl 			= New-Object System.Windows.Forms.Label
	$selectedUserLbl.Text 		= "Forward: "
	$selectedUserLbl.Location 	= New-Object System.Drawing.Point(30, 10) 

	$selectedUserLblExt 		= New-Object System.Windows.Forms.Label
	$selectedUserLblExt.Text 	= "@$($mailDomain) "
	$selectedUserLblExt.Location = New-Object System.Drawing.Point(130, 40)
	$selectedUserLblExt.Width 	= 120

	$recipientField 			= New-Object System.Windows.Forms.TextBox
	$recipientField.Width 		= 90
	$recipientField.Location 	= New-Object System.Drawing.Point(280, 40)

	$recipientFieldLbl 			= New-Object System.Windows.Forms.Label
	$recipientFieldLbl.Text 	= "To: "
	$recipientFieldLbl.Location = New-Object System.Drawing.Point(280, 10) 

	$recipientLblExt 			= New-Object System.Windows.Forms.Label
	$recipientLblExt.Text 		= "@$($mailDomain) "
	$recipientLblExt.Location 	= New-Object System.Drawing.Point(375, 40)
	$recipientLblExt.Width 		= 120

	$msgLbl 					= New-Object System.Windows.Forms.Label; 
	$msgLbl.Text 				= "" 
	$msgLbl.Location 			= New-Object System.Drawing.Point(50, 80);
	$msgLbl.Width 				= 170
	$msgLbl.Height 				= 20

	
	$loadIcon = New-Object System.Drawing.Bitmap("$($loc)\graphics\loader.gif")
	$successIcon = New-Object System.Drawing.Bitmap("$($cfg.ContentPath)\graphics\icon.png")
	$failIcon = New-Object System.Drawing.Bitmap("$($cfg.ContentPath)\graphics\warning.png")

	$msgAnim = New-Object System.Windows.Forms.PictureBox
	$msgAnim.Image = $successIcon
	$msgAnim.Location = New-Object System.Drawing.Point(30,80)
	$msgAnim.Hide()



	$confirmBtn = New-Object System.Windows.Forms.Button
	$confirmBtn.Text = "forward"
	$confirmBtn.Location = New-Object System.Drawing.Point(410, 80)

	$additionalBtn = New-Object System.Windows.Forms.Button
	$additionalBtn.Width = 20
	$additionalBtn.Text = "?"
	$additionalBtn.Location = New-Object System.Drawing.Point(490, 80)

	$reloadBtn = New-Object System.Windows.Forms.Button;
	$reloadBtn.Width = 20; 
	$reloadBtn.Text = "Refresh";
	$reloadBtn.Location = New-Object System.Drawing.Point(450, 80);
	
	$mainForm.Controls.Add($selectedUserField);
	$mainForm.Controls.Add($selectedUserLbl);
	$mainForm.Controls.Add($selectedUserLblExt);


	$mainForm.Controls.Add($recipientField);
	$mainForm.Controls.Add($recipientFieldLbl);
	$mainForm.Controls.Add($recipientLblExt);
	$mainForm.Controls.Add($confirmBtn);
	$mainform.Controls.Add($additionalBtn);
	$mainForm.Controls.Add($msgLbl);
	$mainForm.Controls.Add($msgAnim);
	
	$mainForm.Controls.Add($reloadBtn);

	$mainForm.Controls.Add($currentForwardingLbl);
	$mainForm.Controls.Add($currentForwardingLi);
	
	
	## PROGRESS WIN
	$progWin 				= New-Object System.Windows.Forms.Form;
	$progWin.Width 			= 400
	$progWin.Height 		= 150
	$progWin.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::None
	$progWin.Icon 			= $mailIcon
	
	## TEXT
	$progText 				= New-Object System.Windows.Forms.Label
	$progText.Width 		= 300
	$progText.Height 		= 50
	$progText.Font 			= [System.Drawing.Font]::new("Calibri", 24)
	$progText.Text 			= "loading..."
	$progText.Location 		= New-Object System.Drawing.Point(125, 20)

	## PROGRESS BAR
	$progBar = New-Object System.Windows.Forms.ProgressBar 
	$progBar.Location 		= New-Object System.Drawing.Point(95, 75)
	$progBar.Width 			= 200
	$progBar.Height 		= 40
	$progBar.Style 			= [System.Windows.Forms.ProgressBarStyle]::Continuous

	$progWin.Controls.Add($progText)
	$progWin.Controls.Add($progBar)
    
    $progBar.PerformStep() 
    $progBar.Visible 		= $true;
	$progBar.Minimum 		= 1;
	$progBar.Maximum 		= 2
	$progBar.Value 			= 1;
	
	###############################################################################
	#Event Handlers 
	###############################################################################

    ###############################################################################
    #Initialization for session Starts here. 
	###############################################################################
    $progWin.Add_Activated(
		{

			$progBar.Visible 		= $true;
			
			try 
	        {
		        Connect-ExchangeOnline -Credential $credential -ShowBanner:$false -UseMultithreading $true
				#Import-PSSession $Session -AllowClobber -DisableNameChecking
				$global:Session = Get-PSSession
        
	
	        }catch
	        {
		        Write-Output $Error
	        }

			
			$progBar.Minimum 		= 1;
			$progBar.Maximum 		= (Get-EXOMailbox).Count + 1
			$progBar.Value 			= 1;
		

			UpdateForwardingList 2>&1;
			
			
			Write-Host "last."
			$progWin.Dispose()
		}
	)

	$mainForm.Add_Activated(
		{
	
			
		}
	)
	
	$mainForm.Add_FormClosing(
		{
			#$response = [System.Windows.Forms.MessageBox]::Show("NO!","", "YesNo");
			
		}
	)

	$mainForm.Add_FormClosed(
		{
			Get-PSSession | Remove-PSSession;
			$mainForm.Dispose();
		}
	)

	function SetFw
	{
		param(
			[string]$address, 
			[string]$value, 
			[bool]$force, 
			[bool]$RemoveForwarding
		)

		$global:group;
		$SMTPforwarding;
		$forwarding;
		$existsBool;
		
		try 
		{
			$global:group 		= (Get-DistributionGroupMember -Identity $cfg.Department | Select-Object -ExpandProperty name -InformationAction SilentlyContinue )
			$SMTPforwarding 	= (Get-Mailbox -Identity $address).ForwardingSmtpAddress 
			$forwarding 		= (Get-Mailbox -Identity $address).ForwardingAddress 
			$existsBool 		= (Get-Mailbox "$($value)")
		
		}catch
		{
			Write-Host "Error assigning variables"
		}
		
		"`nAddress: $($address) Recipient: $($value)`n";

		if((!$address -and !$RemoveForwarding))
		{
			"`nReturning -1...`r`n`n"
			Return(-1);
		}
		#check for current forwarding
		if((!$existsBool) -and !($RemoveForwarding))
		{
			"`Returning -4...`r`n`n" 
			Return(-4)
		}

		if ($cfg.BlacklistedUsers.Contains($address))
		{
			"Returning 0...";
			"`nYou are not permitted to forward $address's emails!`n"
			Return(-2);
			Exit
		}elseif($global:group.Contains($address) -and $address)#distro contains user)
		{
			"`nGroup contains address, it is not equal to null`n"
			if(!$RemoveForwarding)
			{
				
				if($force -and (($SMTPforwarding) -or ($forwarding)))
				{
					Set-Mailbox -Identity $address -ForwardingAddress $value -DeliverToMailboxAndForward $true
					return 1;
				}
				if(!$force -and (($SMTPforwarding) -or ($forwarding)))
				{
					"`nCurrent Forwarding Exists for...$($SMTPforwarding)$($forwarding)`n"
					return(-3);
					break;
				}
				
				if(!$SMTPforwarding.ForwardingSmtpAddress -and !$forwarding.ForwardingAddress){
					Set-Mailbox -Identity $address -ForwardingAddress $value -DeliverToMailboxAndForward $true
					"`nReturning 1`n"
					
					Return 1;
				}

			}elseif($RemoveForwarding) 
			{
				## REMOVE FOWARDING
					
				if($force -and (($SMTPforwarding) -or ($forwarding)))
				{
				
					Set-Mailbox -Identity $address -ForwardingAddress $null -ForwardingSmtpAddress $null
					return 1;
				}
				if(!$force -and (($SMTPforwarding) -or ($forwarding)))
				{
					"`nCurrent Forwarding Exists for...$($SMTPforwarding)$($forwarding)`n"
					return(-3);
					break;
				}
				
				if(!$SMTPforwarding.ForwardingSmtpAddress -and !$forwarding.ForwardingAddress){
					Set-Mailbox -Identity $address-ForwardingAddress $null -ForwardingSmtpAddress $null
					"`nReturning 1`n"
					
					Return 1;
				}
			}
		}elseif(!$global:group.Contains($address) -and $address)
		{
			"User not found in distro."
			Return(-2);
		}
		else {
			"Returning 0."
			Return(0);
		}


		"`nEOF"

	}
	function ForwardFunc([bool]$force)
	{
		
		$passVal = $force
		
		$res = SetFw -RemoveForwarding:$false -force:$passVal -value:"$($recipientField.Text)" -address:$selectedUserField.Text
		switch($res)
		{
			1 { 
				"SUCCESS";
				
				$msgAnim.Image 	= $successIcon;
				$msgLbl.Text 	= "SUCCESS";
				
				UpdateForwardingList;					
				break;
			}
			0 { 
				"NULL";
				$msgAnim.Image 	= $null;
				$msgLbl.Text 	= "";
				break;
			}
			-1 { 
				"RECIEVED -1";
				$msgLbl.Text 	= "ADDRESS FIELD IS EMPTY";
				$msgAnim.Image 	= $failIcon;	
				break;
			}
			-2 { 
				Write-Host "UNAUTHORIZED";
				$msgLbl.Text = "UNAUTHORIZED";
				$msgAnim.Image = $failIcon;	
				[System.Windows.MessageBox]::Show("You do not have permission to forward $($selectedUserField.Text)'s emails.","Unauthorized","OK");
				break;
			}
			-3 {
				Write-Host "Forwarding exists";
				Write-Host "Prompt me!";
				$confirm = [System.Windows.Forms.MessageBox]::Show("Current forwarding exists for $($selectedUserField.Text)! Continue to modify forwarding?","Forwarding Already Exists", "YesNo");
				return($confirm)
			}
			-4 {
				Write-Host "REJECTED: Can't find email in organization"
				[System.Windows.MessageBox]::Show("The address entered can't be found.","Unauthorized","OK");
				$msgAnim.Image = $failIcon;	
				break;
			}
			default{
				
			}
		}
		
		Write-Host $res;

	}

	function RemoveForwardFunc([bool]$force)
	{
		
		$passVal = $force
		write-host $passVal
		
	    Write-Host $currentForwardingLi.SelectedItem
		$res = SetFw -RemoveForwarding:$true -force:$passVal -value:$null -address $currentForwardingLi.SelectedItem
		Write-Host $selectedUserField.Text
		
		switch($res)
		{
			1 { 
				Write-Host "SUCCESS";
				$msgAnim.Image = $successIcon;
				$msgLbl.Text = "SUCCESS";
				 					
				break;
			}
			0 { 
				Write-Host "NULL";
				$msgAnim.Image = $null
				$msgLbl.Text = "";
				break;
			}
			-1 { 
				Write-Host "RECIEVED -1";
				$msgLbl.Text = "ADDRESS FIELD IS EMPTY";
				$msgAnim.Image = $failIcon;	
				break;
			}
			-2 { 
				Write-Host "UNAUTHORIZED";
				$msgLbl.Text = "UNAUTHORIZED";
				$msgAnim.Image = $failIcon;	
				[System.Windows.MessageBox]::Show("You do not have permission to modify $($selectedUserField.Text)'s forwarding settings.","Unauthorized","OK");
				break;
			}
			-3 {
				Write-Host "Forwarding exists"
				Write-Host "Prompt me!"
				$confirm = [System.Windows.Forms.MessageBox]::Show("Are you sure you wish to remove forwarding for $($currentForwardingLi.SelectedItem)?","Continue?", "YesNo")
				return($confirm)
			}
			-4 {
				Write-Host "REJECTED: Can't find email in organization"
				[System.Windows.MessageBox]::Show("The address entered can't be found.","Unauthorized","OK");
				break;
			}
			default{
				
			}
		}
		
		Write-Host $res


	}

	
	## Create temp list and assign it.
	function UpdateForwardingList{
		
		## INDEX 
		$currentSelected = $currentForwardingLi.SelectedIndex
		$val1 = $forwardedCollec.Count
		#######################################################

		$tempLi = New-Object System.Collections.Generic.List[String]
		$forwardedCollec | ForEach-Object -Process { $tempLi.Add($_)}
		$currentForwardingLi.DataSource = $tempLi
		
		$members = (get-distributiongroupmember -Identity $cfg.Department | Select-Object -ExpandProperty Name).ToLower()
		"no iter" 2>&1
		## Set list as null and then forwarded collec after the proccess
		Get-Mailbox | Select-Object Name, ForwardingAddress, ForwardingSmtpAddress | ForEach-Object -Process{
		

			if($members.Contains($_.Name))
			{ 
				
				if(!($_.ForwardingSmtpAddress -and $_.ForwardingAddress) -and $forwardedCollec.Contains($_.Name) ) {
				
					$forwardedCollec.RemoveAt($forwardedCollec.IndexOf($_.Name));
					if($currentForwardingLi.SelectedIndex)
					{
						$currentForwardingLi.SelectedIndex = $currentSelected - ($val1 - $forwardedCollec.Count)
					}
					
					
				}if(($_.ForwardingSmtpAddress -or $_.ForwardingAddress) -and !$forwardedCollec.Contains($_.Name)) {
		
					"RETUSR,$($_.Name),1" *>&1;
					$forwardedCollec.Add($_.Name);
					$currentForwardingLi.DataSource = $null;
					$currentForwardingLi.DataSource = $forwardedCollec;
					if($currentForwardingLi.SelectedIndex)
					{
						$currentForwardingLi.SelectedIndex = $currentSelected - ($val1 - $forwardedCollec.Count)
					}
					
				}
			}

			$progBar.PerformStep()
		}	

	
		$currentForwardingLi.DataSource = $null;
		$currentForwardingLi.DataSource = $forwardedCollec;
	}

	$confirmBtn.Add_Click(
		{
			
			$msgLbl.Text = ". . ."
			$msgAnim.Image = $loadIcon
			$msgAnim.Show()
			$currentForwardingLbl.BringToFront() 
			
			$resp = ForwardFunc($false)
			if($resp -eq "yes")
			{
				ForwardFunc($true)
			}
			
			
		}
	)

	$additionalBtn.Add_Click(
		{
			[System.Windows.Forms.MessageBox]::Show($instructString)
		}
	)
	

	
	$timer.Add_Tick(
		{
		
		
		
		
	})

	$arrowClick.Add_Click(
		{
			$var = Get-Variable -Name extended -Scope global 
			Write-Debug $var.Value
			switch($var.Value)
			{
				0{ 
					Write-Debug "Screen: Extend";
					$mainForm.Height += 230;$global:extended = 1;
					$arrowClick.Location = New-Object System.Drawing.Point(225, 310)
					break;
				}
				1{ 
					Write-Host "Screen: Restrict"; $mainForm.Height -= 230;
					$global:extended = 0; 
					$arrowClick.Location = New-Object System.Drawing.Point(225, 90)
						
					break;
				}
			}
		}
		
	)

	
	$menuStrip.Add_Click({
		
		$msgLbl.Text = ". . ."
			$msgAnim.Image = $loadIcon
			$msgAnim.Show()
			$currentForwardingLbl.BringToFront() #this shouldnt be needed 
			
			$resp = RemoveForwardFunc($false)
			if($resp -eq "yes")
			{
				RemoveForwardFunc($true)
				$forwardedCollec.RemoveAt($forwardedCollec.IndexOf($currentForwardingLi.SelectedItem)) 
				$currentForwardingLi.DataSource = $null;
				$currentForwardingLi.DataSource = $forwardedCollec;
			}
			
	})

	
	
	$progWin.ShowDialog()
	$mainForm.ShowDialog()
	


	}
catch 
{
	Write-Host $_.Exception.GetType().FullName, $_.Exception.Message

}finally
{
	Get-PSSession | Remove-PSSession
	Get-Job | Stop-Job
	Get-Job | Remove-Job 

}