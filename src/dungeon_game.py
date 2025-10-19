from system import System
import sys

# Get server URL and model name from command line arguments.
url = ""
model = ""
for arg in sys.argv:
    parts = arg.split("=", 1)
    if len(parts) == 2:
        if parts[0] == "-url":
            url = parts[1]
        elif parts[0] == "-model":
            model = parts[1]

System().main(url, model)
