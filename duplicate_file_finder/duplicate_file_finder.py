"""

Searches for files that have matching content using a hashing/checksum algorithm
MD5 (Message-Digest algorithm 5) gets a long "message" and returns a 128-bit "checksum"
2 files with distinct content has less chance of returning same checksum

"""
import os,sys
import hashlib
 
def MatchFind(homeDir):
    matching= {}
    for dirName, subdirs, fileList in os.walk(homeDir):
        print('Searching %s...' % dirName)
        for filename in fileList:
            # Gets path to file
            path = os.path.join(dirName, filename)
            # calculates hash
            file_hash = hashfile(path)
            # Adds or appends file path
            if file_hash in matching:
                matching[file_hash].append(path)
            else:
                matching[file_hash] = [path]
    return matching
 
def joinDictionaries(dictionary1, dictionary2):
    for key in dictionary2.keys():
        if key in dictionary1:
            dictionary1[key] = dictionary1[key] + dictionary2[key]
        else:
            dictionary1[key] = dictionary2[key]
 
 
def hashfile(path, blocksize = 65536):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()
 
 
def printResults(dictionary1):
    results = list(filter(lambda x: len(x) > 1, dictionary1.values()))
    if len(results) > 0:
        print('---Matching Files Found:---')
        print('---The files below are identical---')
        print('___________________')
        for result in results:
            for subresult in result:
                print('\t\t%s' % subresult)
            print('___________________')
 
    else:
        print('---No matching files found---')
 
 
if __name__ == '__main__':
    if len(sys.argv) > 1:
        matching = {}
        folders = sys.argv[1:]
        for i in folders:
            # Go through all the folders given
            if os.path.exists(i):
                # Detect the matching files and append them to the matching
                joinDictionaries(matching, MatchFind(i))
            else:
                print('%s is not a valid path' % i)
                sys.exit()
        printResults(matching)
    else:
        print('Feed following lines into terminal: python duplicate_file_finder.py folder or python duplicate_file_finder.py folder1 folder2 folder3')
