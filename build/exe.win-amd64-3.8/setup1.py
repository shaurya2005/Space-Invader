#!/usr/bin/env python3
import cx_Freeze
from cx_Freeze import *

executables = [cx_Freeze.Executable("newga.py")]

setup(
    name="newga",
    options={'build_exe':{'packages':['pygame']}},
    executables=executables
    )
