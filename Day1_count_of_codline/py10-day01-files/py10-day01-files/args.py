import sys

if len(sys.argv) != 2:
  sys.exit("usage: args.py <path>")

path = sys.argv[1]
print(f"Path: {path}")
