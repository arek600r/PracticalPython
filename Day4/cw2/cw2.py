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
input_file = "shuffled.png.bin"
output_file = "newfile.png.bin"

# Najpierw usuwamy stary plik wynikowy, jeśli istnieje, 
# żeby "ab" nie dopisywało do starej próby
import os
if os.path.exists(output_file):
    os.remove(output_file)

with open(input_file, "rb") as f, open(output_file, "ab") as f_out:
    while True:
        chunk = f.read(FRAG)
        
        if not chunk: # Jeśli koniec pliku, przerywamy od razu
            break
            
        if len(chunk) < FRAG:
            # Obsługa sytuacji, gdy ostatni kawałek ma mniej niż 10 bajtów
            f_out.write(chunk)
            break

        fdata = list(chunk)
        
        # Twoja zamiana (mapowanie)
        # 0->9, 1->2, 2->1, 3->4, 4->5, 5->0, 6->8, 7->7, 8->3, 9->6
        fdata[0], fdata[1], fdata[2], fdata[3], fdata[4], fdata[5], fdata[6], fdata[7], fdata[8], fdata[9] = \
        fdata[9], fdata[2], fdata[1], fdata[4], fdata[5], fdata[0], fdata[8], fdata[7], fdata[3], fdata[6]
        
        f_out.write(bytes(fdata))

print("Gotowe! Plik został przetworzony.")