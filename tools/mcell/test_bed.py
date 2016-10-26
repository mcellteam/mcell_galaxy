#!/usr/bin/env python
"""
Testing
"""

import string
import sys
import tempfile
import subprocess

debug_out = open ( '../../../../../../junk_out.txt', 'w' )

debug_out.write ( "In __main__\n" )
for arg in sys.argv:
  debug_out.write ( "  arg: " + str(arg) + "\n" )


test_bed_out_name = sys.argv[1];



tbo = open ( test_bed_out_name, 'w' )
tbo.write ( "Hello from the test bed!!\n\n" )

i = 0
for arg in sys.argv:
  tbo.write ( "  arg[" + str(i) + "] = " + str(arg) + "\n" )
  i += 1


tbo.close()

debug_out.close()
