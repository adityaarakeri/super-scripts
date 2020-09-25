#!/usr/bin/python
# Filename: calc_sparseness.py

import sys, getopt

def read_data(file):
    data_len = 0
    zeros = 0

    infile = open(file, 'r')
    line = infile.readline()
    #print line,'\n'
    values = [float(v) for v in line.split(' ') if len(v)]
    data_len = len(values)

    zero_vals = [v for v in values if v == 0]
    zeros = len(zero_vals)

    print('zeros ',zeros,' in total ',data_len,'\n')

def main(argv):
    data_file = ''
    try:
        opts, args = getopt.getopt(argv,"f:")
    except getopt.GetoptError:
        print('python calc_sparseness.py -f <data_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-f':
            data_file = arg
    
    print('data file:', data_file,'\n')
    read_data(data_file)

if __name__ == "__main__":
    main(sys.argv[1:])
