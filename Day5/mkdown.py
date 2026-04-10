with open("ex.md", "r", encoding="utf-8") as f:
	md = f.read()
"""
def heading(level, ln):
	ln = ln[level:].strip()
	return (f"<h{level}>{ln}</h{level}>")	
"""
lines = md.splitlines()

for ln in lines:
	if ln.startswith("#"):
		print(heading(ln))
		continue





# for ln in lines:
# 	if ln.startswith("###"):
# 		print(heading,3, ln)
# 		continue
# 	if ln.startswith("##"):
# 		print(heading,2, ln)
# 		continue
# 	if ln.startswith("#"):
# 		print(heading,1, ln)
# 		continue