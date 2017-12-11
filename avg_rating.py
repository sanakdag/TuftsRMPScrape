# fname = "female_profs.txt"
# content = ""
# with open(fname, "r") as f:
#     content = f.readlines()

# for l in content:
# 	with open(l[:-1], "a") as f2:
# 		f2.write("\n Female \n")

import os
m = 0
f = 0
c = 0
num_male_reviews = 5491
num_female_reviews = 3913
depts = []
dept = ""
for file in os.listdir("./reviews"):
	ind = file.find("_review")
	if ind != -1:
		count = 1
		with open((os.path.join("./reviews",file)), "r") as fi:
			content = fi.readlines()
			for l in content:
				if (count == 3) and l.find("COMMENT") == -1:
					c = float(l[:-1])
				count = count + 1
		prof_file = file[:ind]+".txt"
		#print(os.path.join("./reviews", file))
		with open((os.path.join("./reviews", prof_file)), "r") as fi:
			content = fi.readlines()
			
			for l in content:
				i = l.find("the ")
				if (i != -1):
					dept = l[i+4:-12]
				n = l.find("Male")
				o = l.find("Female")
				if n != -1:
					m = m + c
					depts.append((dept, "M", c))
				if o != -1:
					f = f + c
					depts.append((dept, "W", c))
depts = sorted(depts, key=lambda x: x[0])
z = depts[0][0]
mc = 0
fc = 0
r = 0
m = 0
f = 0
breakdown = []
for d in depts:
	if (d[0] != z):
		breakdown.append((z, m, f, mc, fc))
		r = 0
		fc = 0
		mc = 0
		m = 0 
		f = 0
	if (d[1] == "M"):
		m = m + int(d[2])
		mc = mc + 1
	else: 
		f = f + int(d[2])
		fc = fc + 1
	c = c + 1
	z = d[0]
bd = []
for (d, m, f, mc, fc) in breakdown:
	if fc == 0:
		fc = 1
	if mc == 0:
		mc = 1
	bd.append((d,'%.3f'%(m/mc),'%.3f'%(f/fc)))
bd = sorted(bd, key=lambda x: x[2])
bd = sorted(bd, key=lambda x: x[1])
bd.reverse()
for (d, m, f) in bd:
	if (float(m) == 0):
		if (float(f) == 0):
			print(d + ",,")
		else:
			print(d + ",," + str(f))
	elif (float(f) == 0):
		print(d + ","+ str(m) + ",")
		
	else: print(d+ "," + str(m) + ","+ str(f))




# print (str('%.3f'%(m/num_male_reviews)))
# print (str('%.3f'%(f/num_female_reviews))