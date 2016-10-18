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

import string
import sys
import tempfile
import subprocess

f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
f.write ( "In __main__\n" )
for arg in sys.argv:
  f.write ( "  arg: " + str(arg) + "\n" )

