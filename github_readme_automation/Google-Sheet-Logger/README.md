# googlesheetlogger README

  

[Extension Download Link](https://marketplace.visualstudio.com/items?itemName=rubenkharel.googlesheetlogger) <br  />

GoogleSheetLogger was built for one and only purpose of doing [github's README automation](https://github.com/rubenkharel/README-VSCODE-Automation). It extracts your workspace information and which is later used by Github to display the data in Github README. You can see the demo below.
<br />
*[![FileName!](https://raster.shields.io/badge/Currently_Editing--green?style=for-the-badge)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-main.py-yellow?style=for-the-badge&color=white&logoColor=green&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-Folder_name-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
<br />
*[![FileName!](https://raster.shields.io/badge/Seen_20_Min_Ago_Editing--red?style=for-the-badge)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-main.py-yellow?style=for-the-badge&color=white&logoColor=red&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-Folder_name-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*
<br />
*[![FileName!](https://raster.shields.io/badge/IDLE--orange?style=for-the-badge)](https://github.com/rubenkharel)[![FileName!](https://raster.shields.io/badge/-No_file_Opened-yellow?style=for-the-badge&logoColor=orange&color=white&logo=canonical)](https://github.com/rubenkharel)[![WorkSpace!](https://raster.shields.io/badge/VScode-IDLE-blue?style=for-the-badge&logo=visual-studio-code)](https://github.com/rubenkharel)*


  

## Features

  

Reads your vscode workspace informations and push it to google sheet. <br />
For example if you are editing a index.html file in MyProject folder. <br />
The extension reads the information and sends it to your Google Sheet. <br />

  
  

## Requirements

Google Service Account.
Watch this short video to get everything you need.
https://youtu.be/DiGJditCzYY
<br />
or Follow these steps on your own.
<br />
**Steps**:

1. Create Google Service Account
2. Get Google service's email, apiKey, and .p12 file.
3. Create a Google Sheet document
4. Extract the google sheet document's ID and Sheet name which is by default `Sheet1`
<br />

**Now You have 5 things at total.**

1. Google Service Email
2. Google Service .p12 file
3. Google Service API Key ( Not for extension but for Github Action )
4. Google Sheet Name and
5. Google Sheet ID 


After you have all these files and Info, Go to extension settings and fill up the informations.

**For the .p12 file**: 

 - First rename it to mykey.p12
 - Find the vscode's extension instillation directory
 - Paste the file inside the extension's folder.
<br />
In **windows** it is located in : 
<br />
 `C:/users/yourUserName/.vscode/extensions/rubenkharel.googlesheet.....` 
<br  />
In **WSL** it is in: 
<br />
`/home/yourUserName/.vscode-server/extension/rubenkharel.googlesheet......`
<br />


*Now go to [Automation Repo](https://github.com/rubenkharel/README-VSCODE-Automation) and follow the remaining instructions to finalize your automation.*

  

## Extension Settings

  

This extension contributes the following settings:

* `email`: The Google service email you are provided while creating Google service account.

* `keyFile.p12`: Specifies the folder path containing the mykey.p12 file you downloaded from google service. Follow the tutorial from the Github repo if you get any issues.

* `sheetID` : Sheet ID of the sheet you are going to be using as a bridge. It is located in the url of the sheet you will be using.

* `sheetName` : Found on google sheet document's right-bottom corner. Let it be default I would say.

  

## Known Issues
Just create an issue if you find any. Or if need help create an issue.
## Release Notes
- Initial Release
### 0.0.1
Well, this is all I got right now. Its just a noob version, Might update after few months when I got some real skills...

  

-----------------------------------------------------------------------------------------------------------
**Enjoy!**