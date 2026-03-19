tmpl = "Ala ma {animal}, kot ma {name}."
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

txt = tmpl
for k, v in replacements.items():
	txt = txt.replace("{" + k + "}", v)

print(txt)