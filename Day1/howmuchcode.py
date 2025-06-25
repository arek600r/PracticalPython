import time
import os

DIR_TO_SCAN = "/home/arek/Documents/Code/Python/random-stuff"

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

def get_stats(stats):
	for path, dirs, files in os.walk(DIR_TO_SCAN):
		for file in files:
#			full_fname = os.path.join
			full_name = f"{path}/{file}"
      _, ext = os.path.splittext(file)
			print(full_name, ext)


def show_stats(stats):
	pass

def main():
	stats = {
		"totalLoC": None,
		"langs": {

		}
	}

	while True:
		get_stats(stats)
		show_stats(stats)
		time.sleep(1.5)

if __name__ == "__main__":
	main()