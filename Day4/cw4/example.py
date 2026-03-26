import itertools

# Przechodzimy przez kolejne długości ciągu bajtów
for dlugosc in range(1, 5):
    print(f"--- Generowanie dla długości: {dlugosc} ---")
    
    # itertools.product zastępuje zagnieżdżone pętle
    # repeat=dlugosc określa, ile bajtów ma mieć każda kombinacja
    for kombinacja in itertools.product(range(256), repeat=dlugosc):
        bajtowe_dane = bytes(kombinacja)
        print(bajtowe_dane.hex())
        # Przykład: wypisanie (uwaga: dla długości > 3 będzie tego za dużo!)
        # print(bajtowe_dane)