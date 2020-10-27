# Should I run it?

This script detect if something changed in your project folder.
If the project folder is dirty, node will continue with run execution, if not, will exit.

## Steps to test the script

### 1st step

- run in terminal: npm run start
- npm script will continue because project is dirty

### 2nd step

- run in terminal: npm run start
- npm script will stop script execution because project is pristine

### 3rd step

- make some change/add/delete inside my-project-dir
- run in terminal: npm run start
- npm script will continue because project is dirty
