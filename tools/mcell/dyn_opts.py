#!/usr/bin/env python
import sys
import json

json_in_name = sys.argv[1]
json_out_name = sys.argv[2]

def ds_fooOptions():
  print ( "Top of fooOptions" )
  foos = [ ('Name1', 'Val1'), ('Name2', 'Val2') ]
  print ( "Bottom of fooOptions" )
  return foos

