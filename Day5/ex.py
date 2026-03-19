from markdown import markdown

with open("ex.md", "r", encoding="utf-8") as f:
	md = f.read()

#print(md)

html = markdown(md)
print(html)