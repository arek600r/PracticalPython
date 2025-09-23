import zlib
import string
import random
from multiprocessing import Process, Manager, Event, cpu_count

# --- Parametry ---
ALPHABET_LOW = string.ascii_lowercase
DIGITS = "0123456789"

MIN_LEN_ALPHA = 2
MAX_LEN_ALPHA = 5
MIN_LEN_DIGITS = 1
MAX_LEN_DIGITS = 6

NUM_ALPHA = 200_000   # liczba literowych haseł do wygenerowania
NUM_DIGITS_PER_PROCESS = 50_000  # ile cyfr losuje każdy proces

NUM_PROCESSES = cpu_count()  # liczba procesów (np. liczba rdzeni CPU)

# --- Generowanie słownika literowego (jednokrotnie) ---
def build_alpha_dict():
    crc_alpha_dict = {}
    for _ in range(NUM_ALPHA):
        length = random.randint(MIN_LEN_ALPHA, MAX_LEN_ALPHA)
        passwd = "".join(random.choices(ALPHABET_LOW, k=length))
        crc = zlib.crc32(passwd.encode()) & 0xFFFFFFFF
        if crc not in crc_alpha_dict:
            crc_alpha_dict[crc] = []
        crc_alpha_dict[crc].append(passwd)
    return crc_alpha_dict

# --- Funkcja wykonywana równolegle przez każdy proces ---
def find_collision(crc_alpha_dict, stop_event):
    while not stop_event.is_set():
        for _ in range(NUM_DIGITS_PER_PROCESS):
            length = random.randint(MIN_LEN_DIGITS, MAX_LEN_DIGITS)
            passwd_digits = "".join(random.choices(DIGITS, k=length))
            crc_digits = zlib.crc32(passwd_digits.encode()) & 0xFFFFFFFF

            if crc_digits in crc_alpha_dict:
                for alpha_pass in crc_alpha_dict[crc_digits]:
                    print(f"Kolizja! CRC={crc_digits}")
                    print(f"Cyfry: {passwd_digits}, Litery: {alpha_pass}")
                stop_event.set()  # sygnał dla innych procesów, żeby się zatrzymały
                return

# --- Główna funkcja ---
def main():
    crc_alpha_dict = build_alpha_dict()
    stop_event = Event()
    processes = []

    for _ in range(NUM_PROCESSES):
        p = Process(target=find_collision, args=(crc_alpha_dict, stop_event))
        p.start()
        processes.append(p)

    for p in processes:
        p.join()  # czekamy aż wszystkie procesy skończą

if __name__ == "__main__":
    main()
