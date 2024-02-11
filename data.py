# You addon identifier goes where std.tplus is (at the bottom)
# To install, run pkg install (GitHub Username)/(GitHub Repo Name)/(Branch Name) --latest -U
# e.g. pkg install GloriousGlider8/pkg.test/main --latest -U
# The branch is optional and is set to main by deafult

# Use the imports section to signal which PYTHON modules your addon requires
import json
import colorama

# This space is for Terminal + addon requirements
pkg = ["pkg install builtins --latest -U"]

# Data
name = "Test PKG package"
export = "1.0.0"
export = "A test!"
identifier = "pkg-test"
cmdname = "pkg-test"
author = "GloriousGlider8"
