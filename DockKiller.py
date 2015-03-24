# -*- coding: utf-8 -*-
import subprocess
import re

lines = subprocess.check_output(["ps","-x"]).splitlines()
for line in lines:
  mo = re.match('\s*(\d+)\s*.*Dock.app/Contents/MacOS/Dock',line)
  if mo:
    subprocess.call(["kill",mo.group(1)])