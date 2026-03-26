import os.path

# odczytaj plik
# opracuj sekwencję wymiany bitów
# Utwó©z tabelę z bitami wejściowymi
# Utwórz tabelę z bitami wyjściowymi
# Wyslij te posegregowane do pliku
# powtórz cały proces

FRAG = 8192
input_file = "shuffled.png.bin"
output_file = "newfile.png.bin"

# Najpierw usuwamy stary plik wynikowy, jeśli istnieje, 
# żeby "ab" nie dopisywało do starej próby
import os


list_in = [0,1,2,3,4,5,6,7,8,9]
list_out = [9,2,1,4,5,0,8,7,3,6]

with open(input_file, "rb") as f, open(output_file, "wb") as f_out:
    for x in list_out:
        chunk = f.read(FRAG)
        #teraz elementy listy chunk, należy posegregować tak, jak to jest w przypadku list_out
        list_in.pop(int(x))
        list_in.insert(int(x),chunk)

    f_out.write(b"".join(list_in))
            
