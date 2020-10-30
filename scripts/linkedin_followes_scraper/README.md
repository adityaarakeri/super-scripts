## Overview

This python automation script logs into your LinkedIn account, scrapes the names of your followers and adds them to an excel sheet.
If the script is run for the first time, it creates a new excel sheet, otherwise adds to the next column of the previously created sheet, along with the date.
Also, it compares current names to the ones in the previous column (if present) to check if you have lost or gained any followers, and highlights their names them with red and green text respectively.


## Usage

The script uses gecko driver and Firefox browser so make sure you have it installed. 
Also, make sure that the path of gecko webdriver is added to your system path variables.

Install the following pip packages before running the script:
- selenium
- bs4
- pathlib
- openpyxl

Finally, make sure to change the credentials to your LinkedIn credentials.
Also, change the path to wherever you want the excel file to be stored, but make sure it is accessible by the pathlib module.

