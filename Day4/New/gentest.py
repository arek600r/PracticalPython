MB = b'X' * (1024**2)

with open("bigfile", "wb") as f:
    for _ in range(1024):
        f.write(MB)