import random

with open("bigfile", "r+b") as f:
  for _ in range(5):
    f.seek(random.randint(0, 1024 * 1024 * 1024 - 1))
    f.write(b'?')

