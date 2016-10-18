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

  print ( "top of main" )
  f = open ( '/scratch/Galaxy/galaxy/junk.txt', 'w' )
  f.write ( "In __main__\n" )
  f.write ( "cwd = " + os.getcwd() + "\n" )
  for i in range(len(sys.argv)):
    arg = sys.argv[i]
    f.write ( "  arg["+str(i)+"]: " + str(arg) + "\n" )

  python_exec = sys.executable

  tool_path = os.path.dirname(sys.argv[0])

  json_file = sys.argv[1]
  mdl_file = sys.argv[2]

  dm2mdl_name = os.path.join ( tool_path, "data_model_to_mdl.py" )
  
  mcell_path = os.path.join ( tool_path, "mcell" )

  f.write ( "Tool Path = " + tool_path + "\n" )
  f.write ( "DM to MDL = " + dm2mdl_name + "\n" )
  f.write ( "JSON File = " + json_file + "\n" )
  f.write ( "MDL File = " + mdl_file + "\n" )

  subprocess.call ( [python_exec, dm2mdl_name, json_file, mdl_file ] )


  f.close()

if __name__ == "__main__":
    __main__()
