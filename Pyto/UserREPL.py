"""
The REPL. Goes to the file browser when exited.
"""

from pyto import REPLViewController
import console
import sys

try:

    banner = None
    if "no-banner" in sys.argv:
        banner = "\n\n* REPL restored *\n"

    console.__runREPL__(__file__.split("/")[-1], banner=banner)
    print("Done")
except Exception as e:
    print(str(e))
finally:
    del console.__repl_namespace__[__file__.split("/")[-1]]
    REPLViewController.goToFileBrowser()

