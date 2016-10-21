#!/usr/bin/env python
"""
histogram_gnuplot.py <datafile> <xtic column> <column_list> <title> <ylabel> <yrange_min> <yrange_max> <grath_file>
a generic histogram builder based on gnuplot backend

   data_file    - tab delimited file with data
   xtic_column  - column containing labels for x ticks [integer, 0 means no ticks]
   column_list  - comma separated list of columns to plot
   title        - title for the entire histrogram
   ylabel       - y axis label
   yrange_max   - minimal value at the y axis (integer)
   yrange_max   - maximal value at the y_axis (integer)
                  to set yrange to autoscaling assign 0 to yrange_min and yrange_max
   graph_file   - file to write histogram image to
   img_size     - as X,Y pair in pixels (e.g., 800,600 or 600,800 etc.)


   This tool required gnuplot and gnuplot.py

anton nekrutenko | anton@bx.psu.edu
"""

import string
import sys
import tempfile
import os
import subprocess

f = open ( '../../../../../../junk_out.txt', 'w' )
f.write ( "In __main__\n" )
f.write ( "cwd = " + os.getcwd() + "\n" )

for i in range (len(sys.argv)):
  arg = sys.argv[i]
  f.write ( "  arg[" + str(i) + "] = " + str(arg) + "\n" )


assert sys.version_info[:2] >= ( 2, 4 )

def stop_err(msg):
    sys.stderr.write(msg)
    sys.exit()

try:
  import matplotlib as mpl
  import matplotlib.pyplot as plt

except:
  stop_err("No MatPlotLib\n")

f.write ( "mpl savefig.dpi = " + str(mpl.rcParams['savefig.dpi']) )

infile = sys.argv[1]
pngfile = sys.argv[8]
title = sys.argv[4]
dpi = sys.argv[10]

# Determine the number of columns
data_file = open ( infile )

table = [x.strip().split('\t') for x in data_file]

num_cols = 0
if len(table) > 0:
  if len(table[0]) > 0:
    num_cols = len(table[0])

f.write ( "Num columns = " + str(num_cols) )

if num_cols > 1:

  #mpl.rcParams['figure.facecolor'] = 'white'

  fig = plt.figure()
  fig.suptitle('Reaction Data', fontsize=18.5)
  ax = fig.add_subplot(111)
  ax.spines['top'].set_color('none')
  ax.spines['right'].set_color('none')
  ax.xaxis.set_ticks_position('bottom')
  ax.yaxis.set_ticks_position('left')
  ax.set_xlabel(r'Time (s)')
  ax.set_ylabel(r'Count')
  
  t_vals = [ s[0] for s in table ]

  legend = False
  for col in range(1, num_cols):
    y_vals = [ s[col] for s in table ]
    ax.plot ( t_vals, y_vals, label="Column %d" % col )

  plt.savefig(pngfile, format="png", facecolor='white', dpi=float(dpi))

