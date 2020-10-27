# Manage bluetooth device (connect, disconnect and check status) in mac app CLI
## Overview

This is a script to manage bluetooth device connect, disconnect, check status and list current bluetooth device name exist.

## Why would you find that useful

To easily connect bluetooth device without click (mouseless user), You can connect your bluetooth device by terminal and show Notification.

## How do you install the script?

1. cd mac_bluetooth_connectors
2. swift package update
3. swift build -c release
4. mv .build/release/bt-connect /usr/local/bin/bt-connect

## Usage

Replace '[MAC address]' with your device's MAC address.
- To find MAC address
run 'bt-connect'  will show list of your device name and MAC address
- To connect 
run 'bt-connect -c [MAC address]'
- To disconnect 
run 'bt-connect -d [MAC address]'
- To get status 
run 'bt-connect -s [MAC address]'