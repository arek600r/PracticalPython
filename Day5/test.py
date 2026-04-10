import re

tmpl = "Ala ma {animal}, kot ma {name}. {xyz}"
print(tmpl)

replacements = {
	"animal": "kota",
	"name": "Ale"
}
"""
txt = tmpl.replace("{animal}", "kota").replace(
					"{name}", "Ale")

print(txt)
"""

"""
txt = tmpl
for k, v in replacements.items():
	txt = txt.replace("{" + k + "}", v)

print(txt)
"""

#r = r"{[a-z]+}"
"""
def get_from_repl(matchobj):
    k = matchobj.group(1)
    return replacements.get(k, "?unknow")

print(re.sub(r"{([a-z]+)}", get_from_repl, tmpl))

output = []
segments = tmpl.split("{")
for segment in segments:
	if "}" not in segment:
		print("NO } IN SEGMENT: ", segment)
		output.append(segment)
		continue
	k, text = segment.split("}", 1)
	print(f"KEY {k}, TEXT {text}")
	output.append(replacements.get(k, "?unknown?"))
	output.append(text)

print(''.join(output))

"""

ST_START = "start"
ST_TEXT = "text"
ST_TAG = "tag"
ST_EXIT = "exit"

st = ST_START
i = 0
output = ""
while i < len(tmpl):
  ch = tmpl[i]
  i += 1
  if st == ST_START:
    if ch == "{":
      st = ST_TAG
      k = ""
      continue
    output += ch
    st = ST_TEXT
    continue

  if st == ST_TEXT:
    if ch == "{":
      st = ST_TAG
      k = ""
      continue
    output += ch
    continue
  if st == ST_TAG:
    if ch == "}":
      v = replacements.get(k, "?unknown?")
      output += v
      st = ST_TEXT
      continue
    k += ch
    continue

print(output)
