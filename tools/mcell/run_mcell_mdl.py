#!/usr/bin/env python

"""
Read a JSON Data Model and run MCell
"""

import os
import string
import sys
import tempfile
import subprocess
import time


def __main__():

  print ( "Running run_mcell_mdl.py" )
  f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
  f.write ( "In run_mcell_mdl.py __main__\n" )
  f.write ( "cwd = " + os.getcwd() + "\n" )
  for i in range(len(sys.argv)):
    arg = sys.argv[i]
    f.write ( "  arg["+str(i)+"]: " + str(arg) + "\n" )


  tool_path = os.path.dirname(sys.argv[0])
  mcell_path = os.path.join ( tool_path, "mcell" )
  f.write ( "Tool Path = " + tool_path + "\n" )
  f.write ( "MCell Path = " + mcell_path + "\n" )
  
  mdl_file = sys.argv[1]
  out_file = sys.argv[2]
  seedstr = sys.argv[3]
  seed = int(seedstr)
  
  

  f.write ( "MDL File = " + mdl_file + "\n" )

  os.mkdir ( "react_data" )
  data_dir = "react_data/seed_%05g" % seed
  os.mkdir ( data_dir )

  #p = subprocess.Popen ( [ mcell_path ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
  f.write ( "Starting process at " + str(time.time()) + "\n" )
  p = subprocess.Popen ( [ mcell_path, "-seed", seedstr, mdl_file ] )
  p.wait()
  f.write ( "Finished process at " + str(time.time()) + "\n" )
  
  files = os.listdir( data_dir )
  
  f.write ( "listdir(.) = " + str(files) )
  
  if len(files) > 0:
    react_files = []
    react_cols = []
    for react_file_name in files:
      react_file = open ( data_dir + "/" + react_file_name )
      react_lines = react_file.readlines()
      l0 = []
      l1 = []
      for l in react_lines:
        l = l.strip()
        l = l.split()
        if len(l) == 2:
          l0.append ( l[0] )
          l1.append ( l[1] )
      if len(react_cols) == 0:
        react_cols.append ( l0 )
      react_cols.append ( l1 )
      react_file.close()

    fout = open ( out_file, "w" )
    for i in range ( len(react_cols[0]) ):
      l = react_cols[0][i]
      for col in range ( 1, len(react_cols) ):
        l = l + '\t' + react_cols[col][i]
      l = l + os.linesep
      fout.write ( l )

  
  """
  input_filename = sys.argv[1]
  output_filename = sys.argv[2]
  infile = open ( input_filename, 'r' )
  outfile = open ( output_filename, 'w' )
  outfile.write ( "Ran!!!" )
  outfile.close()
  infile.close()
  """

  f.close()

  print ( "Finished run_mcell_mdl.py" )

if __name__ == "__main__":
    __main__()
    
# database/jobs_directory/000/178/working/react_data/seed_03232
