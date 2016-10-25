#!/usr/bin/env python

"""
Modify a JSON Data Model

Top
cwd = /netapp/cnl/home/bobkuczewski/proj/Galaxy/galaxy/database/jobs_directory/000/115/working
  arg[0]: .../galaxy/tools/mcell/modify_dm_parameters.py  # This file
  arg[1]: .../galaxy/database/files/000/dataset_114.dat   # Name of input data set (should be JSON)
  arg[2]: .../galaxy/database/files/000/dataset_115.dat   # Name of output data set (should write as JSON)
  arg[3]: {a=0.0}  # Parameters are created as name=value pairs by Cheetah code in modify_dm_parameters.xml
  arg[4]: {b=1.0}  # Parameters are created as name=value pairs by Cheetah code in modify_dm_parameters.xml
  arg[5]: {c=2.0}  # Parameters are created as name=value pairs by Cheetah code in modify_dm_parameters.xml
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

# Generate a dictionary of user parameter name/value pairs

user_mods = {}
for i in range(3,len(sys.argv)):
  user_par_assign = sys.argv[i].strip()
  if (user_par_assign[0] == '{') and (user_par_assign[-1] == '}') and (user_par_assign.count('=') == 1):
    # This fits the format for a parameter name=value
    par_name, par_val = user_par_assign[1:-1].split('=')
    user_mods[par_name] = par_val

  
# Open the JSON file and convert it to a Python dictionary
jsonf = open ( json_in_name, 'r' )
json_string = jsonf.read()
jsonf.close()

dm = json.loads ( json_string )

# Dump for testing
f.write ( "Parameters before modification:\n" );
for par in dm['mcell']['parameter_system']['model_parameters']:
  f.write ( "  " + par['par_name'] + " = " + par['par_expression'] + "\n" );

# Modify the parameters specified in the arguments

for par in dm['mcell']['parameter_system']['model_parameters']:
  if par['par_name'] in user_mods:
    par['par_expression'] = user_mods[par['par_name']]

# Dump for testing
f.write ( "Parameters after modification:\n" );
for par in dm['mcell']['parameter_system']['model_parameters']:
  f.write ( "  " + par['par_name'] + " = " + par['par_expression'] + "\n" );

# Convert the Python dictionary back to JSON and export it

jsonf = open ( json_out_name, 'w' )
jsonf.write ( json.dumps(dm) )
jsonf.close()


print ( "Finished modifications" )


