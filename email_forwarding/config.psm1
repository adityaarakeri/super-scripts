add-type -AssemblyName System.Collections

## Import this template, modify the fields and then use the export command to compile. ##  

class config
{
    [string]$ContentPath;
    [System.Collections.ArrayList]$BlackListedUsers;
    [string]$Department;
    [string]$MailDomain;
    [string]$ApplicationHome;
    
    config(){}
    
    static BlackListedUsers()
    {
        get{return $this.BlackListeedUsers}
        set{$this.BlackListedUsers = $_}
        
    }

    static ApplicationHome()
    {
        get{return $this.ApplicationHome}
        set{$this.ApplicationHome = $_}
    }

    static ContentPath() 
    {
        get{return $this.ContentPath}
        set{$this.ContentPath = $_}
    }

    static Department()
    {
        get{return $this.Department}
        set{$this.Department = $_}
    }

    static MailDomain()
    {
        get{return $this.MailDomain}
        set{$this.MailDomain = $_} 
    }
    
    static ExportToCliXml([string]$path, [config]$obj)
    {
         <#
            .Description
            Get-Function displays the name and syntax of all functions in the session.
        #>
        Export-Clixml -InputObject $obj -Path "$($path).xml" 
    }

    #################################################################
    #Deserialize object
    #################################################################
    static [int]Deserialize([PSObject]$obj)
    {
    return 0
        #return [Person]::new($obj.FirstName, $obj.LastName, $obj.Username, $obj.Title, $obj.Department, $obj.Manager, $obj.Number, $obj.Fax, $obj.Extention, $obj.Location)
    }

}

$Global:nBlacklistedUsers 	= @("userName_1", "userName_2");
$con = [config]::new()
$con.ApplicationHome = ".\Forms"
$con.BlackListedUsers = $Global:nBlacklistedUsers
$con.ContentPath = ".\Forms\additional"
$con.Department = "Department"
$con.MailDomain = "maildomain.com"
[config]::ExportToCliXml(".\Forms\config", $con)