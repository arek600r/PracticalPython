import os
import sys
from pathlib import Path
import time

if len(sys.argv) != 2:
    sys.exit("usage: args.py <path>")

main_path = sys.argv[1]
print(f"Path: {main_path}")

print("Method1")
for path, dirs, files in os.walk(main_path):
  path_elements = path.split(os.path.sep)
    
  if any([x.startswith(".") for x in path_elements]):
    print(path_elements)
  for file in files:
      #print(file)
      #print(file_elements)
      #
      #    continue
      _, ext = os.path.splitext(file)
      ext.lower()
      #print(ext)
      #print(f"{path}/{file}")

print("------------")
time.sleep(1.5)
#print("Method2")
#for i in Path(main_path).rglob("*"):
#    print(i)