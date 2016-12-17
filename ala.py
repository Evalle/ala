#!/usr/bin/env python3

'''
Usage:
    ala.py some_apache_logfile.log
'''
import sys

infile = sys.argv[1]

try:
    log_file = open(infile, 'r')
except:
    print('No such file')
    sys.exit(1)


def log_to_dic(line):
    split_line = line.split()
    return {'host': split_line[0], 'bytes': split_line[9]}


def open_log(log):
    for line in log:
        result = log_to_dic(line)
        print(result)

print(open_log(log_file))
log_file.close()
