# Organization Email Forwarding
PowerShell GUI made to set up, remove and view fowarding for users in an organization. 

# Pre-reqs 

To start using this, you need exchange administrative credentials, and to properly create and configure a 'config.xml' file. 
(I've included the config.psm1 for you to import in poewrshell, set the fields and export to a xml file.)

* "ContentPath" - The full path of the "additonal" folder, or whatever your iconts, graphics, are (and where the config should be) stored in.
* "BlackListedUsers" - Users you'd like to prevent setting modification on. 
* "Department" - This is set up currently to look for a distrobution group.  Some tinkering would be required to change it, but it can modifed to take a user list from a different source. 
* "MailDomain" - The email domain. (E.g. @domain.com)
* "ApplicationHome" - The full path where "email_forwarding.ps1" resides. 

# Optional

I'd recommend using "PS2EXE GUI" (https://gallery.technet.microsoft.com/scriptcenter/PS2EXE-GUI-Convert-e7cb69d5) once you confirm that your configuration works to compile the application to an .exe.  This will better hide any sensitive information, especially if distrobuted as means to give users micro-admin permissions. 
      
# Set-up Forwarding

Once configured properly, launching either with "Run with PowerShell", a .bat file, or if you compiled this into an exe, 
the script will have 2 fields and listbox.  To set up forwarding, enter the email (w/out the @domain) you wish to have forwarding set on, in the left, then the recipient of those emails on the right. 

Then select "forward". 

# Remove Forwarding

Inside the listbox, you should see whatever forwarding is active for the group it's configred to. 
To remove active forwarding, right click on a name and choose "Remove forwarding". 
This will proccess, confirm that you wish to make the changes, and you're done. 
