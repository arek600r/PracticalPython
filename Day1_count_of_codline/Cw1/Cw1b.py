import sys
from pathlib import Path

if len(sys.argv) != 2:
    sys.exit("usage: args.py <path>")

main_path = sys.argv[1]
print(f"Path: {main_path}")
count = 0

print("Method2")
for i in Path(main_path).rglob("*"):
    print(i)
    count += 1

print(f"Whole files count: {count}")