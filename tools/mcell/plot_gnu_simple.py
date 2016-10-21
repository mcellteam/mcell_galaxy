#!/usr/bin/env python

import os
import string
import sys
import tempfile
import subprocess

assert sys.version_info[:2] >= ( 2, 4 )

f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
f.write ( "In __main__\n" )
f.write ( "cwd = " + os.getcwd() + "\n" )

for i in range (len(sys.argv)):
  arg = sys.argv[i]
  f.write ( "  arg[" + str(i) + "] = " + str(arg) + "\n" )

infile = sys.argv[1]
pngfile = sys.argv[2]
title = sys.argv[3]

p = subprocess.Popen ( [ "gnuplot" ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
p.stdin.write ( "set term png\n".encode() )
# p.stdin.write ( "set output '/scratch/Galaxy/galaxy/cos88.png'\n".encode() )
p.stdin.write ( "set output '" + pngfile + "'\n".encode() )
# p.stdin.write ( "plot cos(x)\n".encode() )
p.stdin.write ( ( "plot \"%s\" using 1:2 title '%s' with lines\n" % (infile, title) ).encode() )
p.stdin.write ( "quit\n".encode() )
p.stdin.flush()

