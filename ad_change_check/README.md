# Active Directory Change Check

## Overview:

This is a script is used to check if any changes have been made to listed Active Directory objects within the last 24 hours.

## Why would you find that useful?

Generally used to alert if any changes have been made to critical group membership such as Domain Admins or Administrators

## How would you setup your own startup script?

1. The script should run on any system with AD roles installed.
2. The period can easily be changed by adjusting the number of hours in the AddHours(-24) argument.
3. You can modify what is checked by adding/removing items from the $adObjectNameList array.