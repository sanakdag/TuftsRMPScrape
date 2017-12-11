fname = "list.html"
content = ""
with open(fname, "r") as f:
    content = f.readlines()

fo = open("proflist.txt", "w")
for l in content:
	ind = l.find("tid=")
	if ind != -1:
		fo.write(l[ind+4:-3]+"\n")