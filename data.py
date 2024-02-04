# You addon identifier goes where std.tplus is (at the bottom)
# To install, run pkg obtain (your identifier) --latest -U

# Use the imports section to signal which PYTHON modules your addon requires
import json
import colorama

# This space is for Terminal + addon requirements
pkg = ["pkg obtain builtins --latest -U"]

# Data
name = "Test PKG package"
export = "1.0.0"
export = "A test!"
# Identifiers should follow the pattern: author.name
# This is NOT case-sensitive
# authors: pkg, std, builtins, gg8, gloriousglider8 are reserved
identifier = "pkg.test"
cmdname = "pkg-test"
author = "GloriousGlider8"
