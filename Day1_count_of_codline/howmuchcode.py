import time
import os
from pprint import pprint

DIR_TO_SCAN = "C:\\Users\\arek_\\git\\random-stuff"

EXT_TO_LANG = {
  ".c": "C/C++",
  ".cc": "C/C++",
  ".h": "C/C++",
  ".hpp": "C/C++",
  ".cpp": "C/C++",
  ".ino": "C/C++",
  ".py": "Python",
  ".pyw": "Python",
  ".html": "HTML",
  ".htm": "HTML",
  ".md": "Markdown",
  ".css": "CSS",
  ".js": "JavaScript",
  ".bat": "Batch",
  ".pl": "Perl",
  ".php": "PHP",
  ".sh": "Bash",
}

def count_lines(fname):
  #otwieramy plik binarnie, żeby się kodowanie nie rozjechało
  with open(fname, "rb") as f:
    return len(f.read().split(b'\n'))

def get_stats(stats):
  #Tworzymy pustą listę, w której wyniki nie mogą się powtarzać (set - zbiór)
  #unknow_exts = set()
  #langs = defaultdict(int)
  langs = {
    # Python : 17,
    # C/C++ : 26

  }
  total_loc = 0
  for path, dirs, files in os.walk(DIR_TO_SCAN):
    path_elements = path.split(os.path.sep)
    
    if any([x.startswith(".") for x in path_elements]):
      continue

    for file in files:
      
#			full_fname = os.path.join
      full_name = f"{path}/{file}"
      _, ext = os.path.splitext(file)
      
      ext.lower()

      #Gorsza metoda na sprawdzenie, czy wartość jest w zbiorze
#      if ext in EXT_TO_LANG:
#        print(ext)
      #Lepsza metoda
      lang = EXT_TO_LANG.get(ext)
      if lang is None:
#        unknow_exts.add(ext)
        continue
#  print(unknow_exts)

      loc = count_lines(full_name)
      total_loc += loc

      if lang in langs:
        langs[lang] += loc
      else:
        langs[lang] = loc

  stats["langs"] = langs
  stats["totalLoC"] = total_loc

def show_stats(stats):
  pprint(stats)

def main():
  stats = {
    "totalLoC": None,
    "langs": {
    }
  }

  try: 
    while True:
      get_stats(stats)
      show_stats(stats)
      time.sleep(5.5)
  except KeyboardInterrupt:
    pass

if __name__ == "__main__":
  main()