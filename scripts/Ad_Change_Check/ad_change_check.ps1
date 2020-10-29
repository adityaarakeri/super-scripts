# Check specified Active Directory objects that have been modified in the last 24 hours.
# If its a group then list the members.
#
# Justin S. Cooksey, Newcastle, Australia
# https://gist.github.com/jscooksey
#
# Version 1.00, 3th August 2018
#

$checkDate = (Get-Date).AddHours(-24)

$adObjectNameList = @("Domain Admins", "Administrators")

foreach($adObjectName in $adObjectNameList)
{
    $object = Get-ADObject -Filter {name -like $adObjectName} -Properties WhenChanged
    if($object.WhenChanged -gt $checkDate)
    {
        Write-Host "ALERT:" $adObjectName "was modified on" $object.WhenChanged 
        if($object.ObjectClass -eq "group") { Get-ADGroupMember -Identity $object.ObjectGUID | Select @{name="Type";expression={$_.objectClass}}, @{name="Name";expression={$_.Name}} | Format-Table }
    }
}