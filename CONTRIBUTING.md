# Contributing Guidelines

## Folders and Files
- Create a **separate folder** for your script inside the [scripts](#) folder.
- The script can be in any language.
- Script and folder naming convention (Only use underscore):
	- :x: Script Name
	- :x: Folder-Name
	- :x: folder_name
	- :heavy_check_mark: Script_Name
	- :heavy_check_mark: Folder_Name
- The folder should contain the following:
	- Main Script
	- Supporting files for the script
	- A separate `README.md` file with proper documentation.
- Please feel free to add your project to the list of scripts. They have been arranged in alphabetical order according to script folder name.
- Make sure the link to your script is working.
- Please do not add any binary or executable files
- For node projects, please do not upload `node_modules`
- For python projects, please do not upload dependencies, use requirements.txt or a Pipfile to manage dependencies
- Please do not submit very simple scripts which does simple tasks which could be accomplished by some system command
- Please do not submit a PR with multiple files, the script should be self contained

### Opening Issues
- When you open an issue, please make sure the script does not already exist
- Opened Issues by existing Problem will be closed & PR made to this Issue marked as **spam**
- The Contributer who opened an issue will be assigned prefered to the issue. If there is no PR within about 7 Days the issue will be assigned to another Contributer.

### Pull Requests
- Only Pull Requests **joined with an Issue** and matching the **naming-conventions** (See Folders and Files) will be merged!
- If there is no Issue joined in the PR your PR will be labeld as **spam** and closed.
- If your PR doesn' follow the Contributing Guidelines of this Repository it will be also marked as **spam** and closed!

## Which PR's will be accepted?
- Ones you are assigned to
- Your PR has to link the Issue
- PR's with out any binary or executable files
- PR's which contains less than 10 files