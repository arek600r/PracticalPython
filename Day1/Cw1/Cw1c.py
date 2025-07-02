import os
import sys
#os.listdir()
#os.path.isdir
#os.path.isfile

#if len(sys.argv) != 2:
    #sys.exit("usage: args.py <path>")

#bieżemy listę plików i katalogów z listy os.listdir
#Listujemy pliki, korzystając z os.path.isfile, definiujemy katalogi za pomocą os.path.isdir
#Jeżeli isdir == True, to otwieramy go i znowy powtarzamy robotę. 

#main_path = sys.argv[1]
main_path = "/home/arek/Documents/Code/Python/random-stuff/"
print(f"Path: {main_path}")

count = 0

def listing(path):
    global count
    for i in os.listdir(path):
        full_path = os.path.join(path,i)
        if os.path.isfile(full_path):
            print(f"{full_path}")
            count += 1
        elif os.path.isdir(full_path):
            listing(full_path)
            count += 1
    return count

total = listing(main_path)
print(f"{total}")