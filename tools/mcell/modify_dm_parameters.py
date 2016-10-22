#!/usr/bin/env python

"""
Read a JSON Data Model and run MCell
"""

import os
import string
import sys
import json


f = open ( '../../../../../../junk_out.txt', 'w' )
f.write ( "Top\n" )
f.write ( "cwd = " + os.getcwd() + "\n" )
for i in range(len(sys.argv)):
  arg = sys.argv[i]
  f.write ( "  arg["+str(i)+"]: " + str(arg) + "\n" )

json_in_name = sys.argv[1]
json_out_name = sys.argv[2]

f.write ( json_in_name + " => " + json_out_name + "\n" )

jsonf = open ( json_in_name, 'r' )
json_string = jsonf.read()
jsonf.close()

dm = json.loads ( json_string )

f.write ( "Pars:\n" + str(dm['mcell']['parameter_system']['model_parameters']) )

jsonf = open ( json_out_name, 'w' )
jsonf.write ( json_string )
jsonf.close()


print ( "Finished modifications" )


