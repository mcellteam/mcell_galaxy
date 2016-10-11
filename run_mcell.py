#!/usr/bin/env python

"""
Read a JSON Data Model and run MCell
"""
import os
import sys


def __main__():
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
    infile = open ( input_filename, 'r' )
    outfile = open ( output_filename, 'w' )
    outfile.write ( "Ran!!!" )
    outfile.close()
    infile.close()

if __name__ == "__main__":
    __main__()
