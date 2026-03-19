import os.path

# odczytaj plik
# opracuj sekwencję wymiany bitów
# Utwó©z tabelę z bitami wejściowymi
# Utwórz tabelę z bitami wyjściowymi
# Wyslij te posegregowane do pliku
# powtórz cały proces

#0 -> 5
#1 -> 2
#2 -> 1
#3 -> 8
#4 -> 3
#5 -> 4     
#6 -> 9
#7 -> 7
#8 -> 9
#9 -> 0  
FRAG = 10

with open("shuffled.png.bin", "rb") as f:
    while True:
        fdata = list(f.read(FRAG))
        print(f"przed: {fdata}")
        if not fdata:
            break
        fdata[0], fdata[1], fdata[2], fdata[3], fdata[4], fdata[5], fdata[6], fdata[7], fdata[8], fdata[9] = fdata[9], fdata[2], fdata[1], fdata[4], fdata[5], fdata[0], fdata[8], fdata[7], fdata[3], fdata[6]
        print(f"po: {fdata}")
        with open("newfile.png.bin", "ab") as f_out:
            f_out.write(bytes(fdata))
        