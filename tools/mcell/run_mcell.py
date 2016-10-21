#!/usr/bin/env python

"""
Read a JSON Data Model and run MCell
"""

import os
import string
import sys
import tempfile
import subprocess


def __main__():

  f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
  f.write ( "In __main__\n" )
  f.write ( "cwd = " + os.getcwd() + "\n" )
  for i in range(len(sys.argv)):
    arg = sys.argv[i]
    f.write ( "  arg["+str(i)+"]: " + str(arg) + "\n" )


  tool_path = os.path.dirname(sys.argv[0])
  mcell_path = os.path.join ( tool_path, "mcell" )
  dm2mdl_path = os.path.join ( tool_path, "data_model_to_mdl.py" )
  f.write ( "Tool Path = " + tool_path + "\n" )
  f.write ( "MCell Path = " + mcell_path + "\n" )
  f.write ( "DM to MDL = " + dm2mdl_path + "\n" )
  
  json_file = sys.argv[1]

  f.write ( "JSON File = " + json_file + "\n" )

  p = subprocess.Popen ( [ mcell_path ], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
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

if __name__ == "__main__":
    __main__()
