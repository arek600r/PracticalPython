import os
import sys

if len(sys.argv) != 2:
    sys.exit("usage: args.py <path>")

path = sys.argv[1]
print(f"Path: {path}")

for path, dirs, files in os.walk(path):
    for file in files:
        _, ext = os.path.splitext(file)
        ext.lower()
        print(f"{path}/{file}")