#!/usr/bin/env python

"""
Read a JSON Data Model and display it
"""

import os
import string
import sys
import json


data_model_depth = 0
def write_data_model ( html_file, name, dm ):
    global data_model_depth
    if type(dm) == type({'a':1}):  #dm is a dictionary
        html_file.write ( str(data_model_depth*"  ") + name + " {}\n" )
        data_model_depth += 1
        for k,v in sorted(dm.items()):
            write_data_model ( html_file, k, v )
        data_model_depth += -1
    elif type(dm) == type(['a',1]):  #dm is a list
        html_file.write ( str(data_model_depth*"  ") + name + " []\n" )
        data_model_depth += 1
        i = 0
        for v in dm:
            k = name + "["+str(i)+"]"
            write_data_model ( html_file, k, v )
            i += 1
        data_model_depth += -1
    # elif (type(dm) == type('a1')) or (type(dm) == type(u'a1')):  #dm is a string
    elif (type(dm) == type('a1')):  #dm is a string
        html_file.write ( str(data_model_depth*"  ") + name + " = " + "\"" + str(dm) + "\"\n" )
    else:
        html_file.write ( str(data_model_depth*"  ") + name + " = " + str(dm) + "\n" )



f = open ( '../../../../../../junk_out.txt', 'w' )
f.write ( "cwd = " + os.getcwd() + "\n" )
for i in range(len(sys.argv)):
  arg = sys.argv[i]
  f.write ( "  arg["+str(i)+"]: " + str(arg) + "\n" )

tool_path = os.path.dirname(sys.argv[0])

json_file_name = sys.argv[1]
html_file_name = sys.argv[2]

f.write ( "Tool Path = " + tool_path + "\n" )
f.write ( "JSON File = " + json_file_name + "\n" )
f.write ( "HTML File = " + html_file_name + "\n" )

jsonf = open ( json_file_name, 'r' )
json_string = jsonf.read()
jsonf.close()

dm = json.loads ( json_string )

htmlf = open ( html_file_name, 'w' )

style = ' style="background-color: #eee;"'

htmlf.write ( "<center><html><body><h1>Data Model</h1>\n<hr /><h2>Model Parameters</h2><br />\n" )

htmlf.write ( '<table style="width:95%; border: 1px solid black;">\n' )
for p in dm['mcell']['parameter_system']['model_parameters']:
  htmlf.write ( '<tr'+style+'><td'+style+'>' + p['par_name'] + '</td><td'+style+'>' + p['par_expression'] + '</td><td'+style+'>' + p['par_description'] + '</td></tr>\n' )

htmlf.write ("</table><br /><h2>Raw Data Model</h2><br /></center><pre>" )

write_data_model ( htmlf, "", dm )

htmlf.write ( "</pre></body></html>" )

htmlf.close()


f.close()

print ( "Data Model shown as HTML" )

