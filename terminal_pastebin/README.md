# Termbin 

## Overview:

This is a script to quickly post some text or file on termbin.com and get a short url for it.   

## Why would you find that useful?

It is convenient for quickly transfering snippet of code or text to another computer or another person, without having to open the browser.  

## Usage 

* For mac user, run the following to setup alias
```
./mac_setup.sh
```

* For linux user, run the following to setup alias
```
./linux_setup.sh
```

* Paste short text 
```
echo "hello world" | tb
```

* Paste a file 
```
cat file.txt | tb
```

* Paste a file and copy the url to clipboard
```
cat file.txt | tb | pbcopy
```
___

