#!/usr/bin/env python
"""
Plot a file ...
  arg: /scratch/Galaxy/galaxy/tools/mcell/plot_gnu.py

  arg: /scratch/Galaxy/galaxy/database/files/000/dataset_40.dat
  arg: 1      # Column  to plot as x
  arg: 2,3,5  # Columns to plot as y
  arg: Plot   # Plot title
  arg: V1     # Label for Y axis
  arg: 0      # Y Min
  arg: 0      # Y Max
  arg: /scratch/Galaxy/galaxy/database/files/000/dataset_71.dat
  arg: 800,600  # output size
"""

import os
import string
import sys
import tempfile
import subprocess

assert sys.version_info[:2] >= ( 2, 4 )

f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
f.write ( "In __main__\n" )
f.write ( "cwd = " + os.getcwd() )
for arg in sys.argv:
  f.write ( "  arg: " + str(arg) + "\n" )

p = subprocess.Popen ( [ "gnuplot" ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
p.stdin.write ( "set term png\n".encode() )
# p.stdin.write ( "set output '/scratch/Galaxy/galaxy/cos88.png'\n".encode() )
p.stdin.write ( "set output '" + sys.argv[3] + "'\n".encode() )
# p.stdin.write ( "plot cos(x)\n".encode() )
p.stdin.write ( ( "plot \"%s\" using 1:2 title '%s' with lines\n" % (sys.argv[1], sys.argv[2]) ).encode() )
p.stdin.write ( "quit\n".encode() )
p.stdin.flush()

