# You addon identifier goes where std.tplus is (at the bottom)
# To install, run pkg obtain (your identifier) --latest -U

# Use the imports section to signal which PYTHON modules your addon requires
import gg8lib
import os

# This space is for Terminal + addon requirements
pkg = ["pkg obtain builtins --latest -U"]

# Data
name = "Nice T+ Features"
export = "1.0.0"
export = "Very useful packages for Terminal +"
identifier = "std.tplus"
