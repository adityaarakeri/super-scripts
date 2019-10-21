# Translate excel
Small script that allows you to translate specified column and row-range of an excel file using Google Translator. 

## Requirements
`pip3 install -r requirements.txt`


## Usage
`python3 translate_excel.py <filename> <column> <row-start> <row-end>`

It will ask to and from which language you want the translation to be done.

## Improvements
App is currently using sys.argv. It could be rewritten to use `argparse` instead. 
