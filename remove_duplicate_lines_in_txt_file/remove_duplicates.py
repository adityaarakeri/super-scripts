#!/usr/bin/env python3
import os


def remove_duplicates():
    checkedLines = set()
    fileName = input('Enter File Name ---> ')
    os.rename(fileName, fileName + '.original')
    if fileName.endswith('.txt'):
        with open(fileName, "w") as outputFile:
            for line in open(fileName + '.original', "r"):
                if line not in checkedLines:
                    outputFile.write(line)
                    checkedLines.add(line)
            os.remove(fileName + '.original')
            return "Duplicates removed new file updated. ---> " + fileName
            
            

    else:
        return 'Failed to check file. Please verify if it ends with .txt extension'


if __name__ == '__main__':
    print(remove_duplicates())
