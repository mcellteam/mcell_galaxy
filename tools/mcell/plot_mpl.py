#!/usr/bin/env python
"""
Use MatPlotLib to plot multiple columns from a file
"""

import string
import sys
import tempfile
import os
import subprocess

# This is a convenient file location for debug output
f = open ( '../../../../../../junk_out.txt', 'w' )
f.write ( "In __main__\n" )
f.write ( "cwd = " + os.getcwd() + "\n" )

for i in range (len(sys.argv)):
  arg = sys.argv[i]
  f.write ( "  arg[" + str(i) + "] = " + str(arg) + " of type " + str(type(arg)) + "\n" )


assert sys.version_info[:2] >= ( 2, 4 )

def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()

try:
  import matplotlib as mpl
  import matplotlib.pyplot as plt

except:
  stop_err("No MatPlotLib\n")

f.write ( "mpl savefig.dpi = " + str(mpl.rcParams['savefig.dpi']) + "\n" )

infile = sys.argv[1]
pngfile = sys.argv[2]
cols_to_plot = [int(v)-1 for v in sys.argv[3].split(',')]
x_axis = int(sys.argv[4]) - 1
title = sys.argv[5]
xlabel = sys.argv[6]
ylabel = sys.argv[7]
dpi = sys.argv[8]

f.write ( "Actual Columns to plot = " + str(cols_to_plot) + ", x column = " + str(x_axis) + "\n" )

# Convert the data file into a table
data_file = open ( infile )
table = [x.strip().split('\t') for x in data_file]

# Determine the number of columns in the table
num_cols = 0
if len(table) > 0:
  if len(table[0]) > 0:
    num_cols = len(table[0])

f.write ( "Num columns = " + str(num_cols) + "\n" )

if num_cols > 1:

  #mpl.rcParams['figure.facecolor'] = 'white'

  fig = plt.figure()
  fig.suptitle(title, fontsize=18.5)
  ax = fig.add_subplot(111)
  ax.spines['top'].set_color('none')
  ax.spines['right'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  ax.set_xlabel(xlabel)
  ax.set_ylabel(ylabel)
  #ax.set_xlabel(r'Time (s)')
  #ax.set_ylabel(r'Count')
  
  t_vals = [ s[x_axis] for s in table ]

  legend = False
  for col in range(num_cols):
    if (col in cols_to_plot) and (col != x_axis):
      y_vals = [ s[col] for s in table ]
      ax.plot ( t_vals, y_vals, label="Column %d" % (col+1) )

  plt.savefig(pngfile, format="png", facecolor='white', dpi=float(dpi))

