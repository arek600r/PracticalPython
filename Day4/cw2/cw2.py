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


def sort(inn, out):
    None

frag_number = -1
with open("shuffled.png.bin", "rb") as f:
    while True:
        frag_number += 1
        fdata = f.read(FRAG)
        if not fdata:
            break
        print(fdata)
#        sort(fdata, )