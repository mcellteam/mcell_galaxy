#!/usr/bin/env python
import sys
import json

json_in_name = sys.argv[1]
json_out_name = sys.argv[2]

# Generate a dictionary of user parameter name/value pairs from command line input

user_mods = {}
for i in range(3,len(sys.argv)):
  user_par_assign = sys.argv[i].strip()
  if (user_par_assign[0] == '{') and (user_par_assign[-1] == '}') and (user_par_assign.count('=') == 1):
    # This fits the format for a parameter:  {name=value}
    par_name, par_val = user_par_assign[1:-1].split('=')
    user_mods[par_name] = par_val

  
# Open the JSON file and convert it to a Python dictionary
jsonf = open ( json_in_name, 'r' )
json_string = jsonf.read()
jsonf.close()

pd = json.loads ( json_string )

# Print for testing
print ( "Parameters before modification:" );
for par in pd['parameters']:
  print ( "  " + par['par_name'] + " = " + par['par_expression'] );

# Modify the parameters specified in the arguments

for par in pd['parameters']:
  if par['par_name'] in user_mods:
    par['par_expression'] = user_mods[par['par_name']]

# Print for testing
print ( "Parameters after modification:" );
for par in pd['parameters']:
  print ( "  " + par['par_name'] + " = " + par['par_expression'] );

# Convert the Python dictionary back to JSON and export it
jsonf = open ( json_out_name, 'w' )
jsonf.write ( json.dumps(pd) )
jsonf.close()

print ( "Finished modifications" )


