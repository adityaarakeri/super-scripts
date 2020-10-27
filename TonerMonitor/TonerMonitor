$printerlist = import-csv .\printerlist.txt -header Value,Name,Description
$outfile = ".\PrinterReport.html"
$SNMP = new-object -ComObject olePrn.OleSNMP
$ErrorActionPreference = "Continue"
$total = ($printerlist.value|? {$_ -notlike "-*"}).length
$time = (Get-Date).ToString("MM/dd/yyyy")
$alertIT = $false

Write "`
<html>`
<head>`
<title>Printer Report</title>`
<style>* {font-family:'Trebuchet MS';}</style>`
</head>`
<body>
<h1>Toner levels for $time </h1>"|out-file $outfile

write "Found $total SPI printers"
$x = 0

foreach ($p in $printerlist){

if ($p.value -like "-*"){write "<h3>",$p.value.replace('-',''),"</h3>"|add-content $outfile}

if ($p.value -notlike "-*"){

$x = $x + 1
$printertype = $nul
$status = $nul
$percentremaining = $nul
$blackpercentremaining = $nul
$cyanpercentremaining = $nul
$magentapercentremaining = $nul
$yellowpercentremaining = $nul
$wastepercentremaining = $nul

if (!(test-connection $p.Value -Quiet -count 1)){write ($p.value + " is offline<br>")|add-content $outfile}
if (test-connection $p.value -quiet -count 1){
$snmp.open($p.value,"public",2,3000)
$printertype = $snmp.Get(".1.3.6.1.2.1.25.3.2.1.3.1")
write ([string]$x + ": " + [string]$p.Value + " " + $printertype)
}
#PRINTER
if ($printertype -like "*Sharp MX-3050N*"){

$blacktonervolume = $snmp.get("43.11.1.1.8.1.4")
$blackcurrentvolume = $snmp.get("43.11.1.1.9.1.4")
[int]$blackpercentremaining = ($blackcurrentvolume / $blacktonervolume) * 100 
$cyantonervolume = $snmp.get("43.11.1.1.8.1.1")
$cyancurrentvolume = $snmp.get("43.11.1.1.9.1.1")
[int]$cyanpercentremaining = ($cyancurrentvolume / $cyantonervolume) * 100
$magentatonervolume = $snmp.get("43.11.1.1.8.1.2")
$magentacurrentvolume = $snmp.get("43.11.1.1.9.1.2")
[int]$magentapercentremaining = ($magentacurrentvolume / $magentatonervolume) * 100
$yellowtonervolume = $snmp.get("43.11.1.1.8.1.3")
$yellowcurrentvolume = $snmp.get("43.11.1.1.9.1.3")
[int]$yellowpercentremaining = ($yellowcurrentvolume / $yellowtonervolume) * 100
$wastetonervolume = $snmp.get("43.11.1.1.8.1.9")
$wastecurrentvolume = [math]::round([math]::abs($snmp.get("43.11.1.1.9.1.9")))
[int]$wastepercentremaining = (($wastecurrentvolume / $wastetonervolume) * 100)

$statustree = $snmp.gettree("43.18.1.1.8")
$status = $statustree|? {$_ -notlike "print*"} 
$status = $status|? {$_ -notlike "*bypass*"}
$name = $snmp.get(".1.3.6.1.2.1.1.5.0")
if ($name -notlike "PX*"){$name = $p.name}

write ("<b>" + $p.description + "</b><a style='text-decoration:none;font-weight:bold;' href=http://" + $p.value + " target='_new'> " + $name + "</a> <br>" + $printertype + "<br>")|add-content $outfile
if (($blackpercentremaining -gt 10) -and ($blackpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile}
if (($blackpercentremaining -ge 0) -and ($blackpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile
}

if (($cyanpercentremaining -gt 10) -and ($cyanpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$cyanpercentremaining,"</b>% cyan toner<br>"|add-content $outfile}
if (($cyanpercentremaining -ge 0) -and ($cyanpercentremaining -le 10))
{
$alertIT = $true 
write "<b style='font-size:110%;color:red;'>",$cyanpercentremaining,"</b>% cyan toner<br>"|add-content $outfile
}

if (($magentapercentremaining -gt 10) -and ($magentapercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$magentapercentremaining,"</b>% magenta toner<br>"|add-content $outfile}
if (($magentapercentremaining -ge 0) -and ($magentapercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$magentapercentremaining,"</b>% magenta toner<br>"|add-content $outfile
}

if (($yellowpercentremaining -gt 10) -and ($yellowpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$yellowpercentremaining,"</b>% yellow toner<br>"|add-content $outfile}
if (($yellowpercentremaining -ge 0) -and ($yellowpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$yellowpercentremaining,"</b>% yellow toner<br>"|add-content $outfile
}

if (($wastepercentremaining -gt 10) -and ($wastepercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$wastepercentremaining,"</b>% waste container free space<br>"|add-content $outfile}
if (($wastepercentremaining -ge 0) -and ($wastepercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$wastepercentremaining,"</b>% waste container free space<br>"|add-content $outfile
}
if ($status.length -gt 0){write ($status + "<br><br>")|add-content $outfile}else{write "Operational<br><br>"|add-content $outfile}
}

#PRINTER
if ($printertype -like "*SHARP MX-C301W*"){

$blacktonervolume = $snmp.get("43.11.1.1.8.1.4")
$blackcurrentvolume = $snmp.get("43.11.1.1.9.1.4")
[int]$blackpercentremaining = ($blackcurrentvolume / $blacktonervolume) * 100 

$statustree = $snmp.gettree("43.18.1.1.8")
$status = $statustree|? {$_ -notlike "print*"} 
$status = $status|? {$_ -notlike "*bypass*"}
$name = $snmp.get(".1.3.6.1.2.1.1.5.0")
if ($name -notlike "PX*"){$name = $p.name}

write ("<b>" + $p.description + "</b><a style='text-decoration:none;font-weight:bold;' href=http://" + $p.value + " target='_new'> " + $name + "</a> <br>" + $printertype + "<br>")|add-content $outfile
if (($blackpercentremaining -gt 10) -and ($blackpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile}
if (($blackpercentremaining -ge 0) -and ($blackpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile
}


if ($status.length -gt 0){write ($status + "<br><br>")|add-content $outfile}else{write "Operational<br><br>"|add-content $outfile}
}


#PRINTER
if ($printertype -like "*Canon iPF785 1.06*"){

$blacktonervolume = $snmp.get("43.11.1.1.8.1.5")
$blackcurrentvolume = $snmp.get("43.11.1.1.9.1.5")
[int]$blackpercentremaining = ($blackcurrentvolume / $blacktonervolume) * 100 
$Mblacktonervolume = $snmp.get("43.11.1.1.8.1.4")
$Mblackcurrentvolume = $snmp.get("43.11.1.1.9.1.4")
[int]$Mblackpercentremaining = ($Mblackcurrentvolume / $Mblacktonervolume) * 100 
$cyantonervolume = $snmp.get("43.11.1.1.8.1.1")
$cyancurrentvolume = $snmp.get("43.11.1.1.9.1.1")
[int]$cyanpercentremaining = ($cyancurrentvolume / $cyantonervolume) * 100
$magentatonervolume = $snmp.get("43.11.1.1.8.1.2")
$magentacurrentvolume = $snmp.get("43.11.1.1.9.1.2")
[int]$magentapercentremaining = ($magentacurrentvolume / $magentatonervolume) * 100
$yellowtonervolume = $snmp.get("43.11.1.1.8.1.3")
$yellowcurrentvolume = $snmp.get("43.11.1.1.9.1.3")
[int]$yellowpercentremaining = ($yellowcurrentvolume / $yellowtonervolume) * 100
$wastetonervolume = $snmp.get("43.11.1.1.8.1.6")
$wastecurrentvolume = [math]::round([math]::abs($snmp.get("43.11.1.1.9.1.6")))
[int]$wastepercentremaining = (($wastecurrentvolume / $wastetonervolume) * 100)

$statustree = $snmp.gettree("43.18.1.1.8")
$status = $statustree|? {$_ -notlike "print*"} 
$status = $status|? {$_ -notlike "*bypass*"}
$name = $snmp.get(".1.3.6.1.2.1.1.5.0")
if ($name -notlike "PX*"){$name = $p.name}

write ("<b>" + $p.description + "</b><a style='text-decoration:none;font-weight:bold;' href=http://" + $p.value + " target='_new'> " + $name + "</a> <br>" + $printertype + "<br>")|add-content $outfile
if (($blackpercentremaining -gt 10) -and ($blackpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile}
if (($blackpercentremaining -ge 0) -and ($blackpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile
}


if (($Mblackpercentremaining -gt 10) -and ($Mblackpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$Mblackpercentremaining,"</b>% Matte Black toner<br>"|add-content $outfile}
if (($Mblackpercentremaining -ge 0) -and ($Mblackpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$Mblackpercentremaining,"</b>% Matte Black toner<br>"|add-content $outfile
}


if (($cyanpercentremaining -gt 10) -and ($cyanpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$cyanpercentremaining,"</b>% cyan toner<br>"|add-content $outfile}
if (($cyanpercentremaining -ge 0) -and ($cyanpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$cyanpercentremaining,"</b>% cyan toner<br>"|add-content $outfile
}


if (($magentapercentremaining -gt 10) -and ($magentapercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$magentapercentremaining,"</b>% magenta toner<br>"|add-content $outfile}
if (($magentapercentremaining -ge 0) -and ($magentapercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$magentapercentremaining,"</b>% magenta toner<br>"|add-content $outfile
}


if (($yellowpercentremaining -gt 10) -and ($yellowpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$yellowpercentremaining,"</b>% yellow toner<br>"|add-content $outfile}
if (($yellowpercentremaining -ge 0) -and ($yellowpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$yellowpercentremaining,"</b>% yellow toner<br>"|add-content $outfile
}


if (($wastepercentremaining -gt 10) -and ($wastepercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$wastepercentremaining,"</b>% Maintenance Cartridge Free Space<br>"|add-content $outfile}
if (($wastepercentremaining -ge 0) -and ($wastepercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$wastepercentremaining,"</b>% Maintenance Cartridge Free Space<br>"|add-content $outfile
}

if ($status.length -gt 0){write ($status + "<br><br>")|add-content $outfile}else{write "Operational<br><br>"|add-content $outfile}
}


#PRINTER
if ($printertype -like "*HP LaserJet M203dw*"){


$cyantonervolume = $snmp.get("43.11.1.1.8.1.1")
$cyancurrentvolume = $snmp.get("43.11.1.1.9.1.1")
[int]$cyanpercentremaining = ($cyancurrentvolume / $cyantonervolume) * 100


$statustree = $snmp.gettree("43.18.1.1.8")
$status = $statustree|? {$_ -notlike "print*"} 
$status = $status|? {$_ -notlike "*bypass*"}
$name = $snmp.get(".1.3.6.1.2.1.1.5.0")
if ($name -notlike "PX*"){$name = $p.name}

write ("<b>" + $p.description + "</b><a style='text-decoration:none;font-weight:bold;' href=http://" + $p.value + " target='_new'> " + $name + "</a> <br>" + $printertype + "<br>")|add-content $outfile
if (($cyanpercentremaining -gt 10) -and ($cyanpercentremaining -le 24)){write "<b style='font-size:110%;color:orange;'>",$cyanpercentremaining,"</b>% black toner<br>"|add-content $outfile}
if (($cyanpercentremaining -ge 0) -and ($cyanpercentremaining -le 10)){write "<b style='font-size:110%;color:red;'>",$cyanpercentremaining,"</b>% black toner<br>"|add-content $outfile}

if ($status.length -gt 0){write ($status + "<br><br>")|add-content $outfile}else{write "Operational<br><br>"|add-content $outfile}
}


#PRINTER
if ($printertype -like "*HP LaserJet 500 color M551*"){

$blacktonervolume = $snmp.get("43.11.1.1.8.1.1")
$blackcurrentvolume = $snmp.get("43.11.1.1.9.1.1")
[int]$blackpercentremaining = ($blackcurrentvolume / $blacktonervolume) * 100 
$cyantonervolume = $snmp.get("43.11.1.1.8.1.2")
$cyancurrentvolume = $snmp.get("43.11.1.1.9.1.2")
[int]$cyanpercentremaining = ($cyancurrentvolume / $cyantonervolume) * 100
$magentatonervolume = $snmp.get("43.11.1.1.8.1.3")
$magentacurrentvolume = $snmp.get("43.11.1.1.9.1.3")
[int]$magentapercentremaining = ($magentacurrentvolume / $magentatonervolume) * 100
$yellowtonervolume = $snmp.get("43.11.1.1.8.1.4")
$yellowcurrentvolume = $snmp.get("43.11.1.1.9.1.4")
[int]$yellowpercentremaining = ($yellowcurrentvolume / $yellowtonervolume) * 100


$statustree = $snmp.gettree("43.18.1.1.8")
$status = $statustree|? {$_ -notlike "print*"} 
$status = $status|? {$_ -notlike "*bypass*"}
$name = $snmp.get(".1.3.6.1.2.1.1.5.0")
if ($name -notlike "PX*"){$name = $p.name}

write ("<b>" + $p.description + "</b><a style='text-decoration:none;font-weight:bold;' href=http://" + $p.value + " target='_new'> " + $name + "</a> <br>" + $printertype + "<br>")|add-content $outfile

if (($blackpercentremaining -ge 0) -and ($blackpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$blackpercentremaining,"</b>% black toner<br>"|add-content $outfile}

if (($cyanpercentremaining -ge 0) -and ($cyanpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$cyanpercentremaining,"</b>% cyan toner<br>"|add-content $outfile}

if (($magentapercentremaining -ge 0) -and ($magentapercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$magentapercentremaining,"</b>% magenta toner<br>"|add-content $outfile}

if (($yellowpercentremaining -ge 0) -and ($yellowpercentremaining -le 10))
{
$alertIT = $true
write "<b style='font-size:110%;color:red;'>",$yellowpercentremaining,"</b>% yellow toner<br>"|add-content $outfile
}

if ($status.length -gt 0){write ($status + "<br><br>")|add-content $outfile}else{write "Operational<br><br>"|add-content $outfile}
}


}
}

if ($alertIT -eq $true) {

$emailSmtpServer = "smtp.gmail.com"
$emailSmtpServerPort = "587"
$credential = Import-CliXml -Path "C:\Secrets\myCred_${env:USERNAME}_${env:COMPUTERNAME}.xml"
$emailSmtpUser  = $credential.UserName
$emailFrom = "Generic@gmail.com" 
$emailSmtpPass=$credential.GetNetworkCredential().Password
[string[]]$emailTo = "<Bob@email.com>,<Guy@email.com>,<email@email.com>"
$emailMessage = New-Object System.Net.Mail.MailMessage( $emailFrom , $emailTo )
$emailMessage.Subject = "Toner Levels $time" 
$emailMessage.Body = Get-Content $outfile -Raw
$emailMessage.IsBodyHtml=$true
 
$SMTPClient = New-Object System.Net.Mail.SmtpClient( $emailSmtpServer , $emailSmtpServerPort )
$SMTPClient.EnableSsl = $True
$SMTPClient.Credentials = New-Object System.Net.NetworkCredential( $emailSmtpUser , $emailSmtpPass );
$SMTPClient.Send( $emailMessage )
}
