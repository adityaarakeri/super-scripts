import sys
import os
import comtypes.client
UPLOAD_FOLDER = os.getcwd()+'\\uploads'
from glob import glob
for files in glob(UPLOAD_FOLDER+'/*.docx'):
    wdFormatPDF = 17
    in_file = files
    out_file = UPLOAD_FOLDER+"\\Converted.pdf"
                #CoInitialize()
    word = comtypes.client.CreateObject('Word.Application')
    doc = word.Documents.Open(in_file)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()