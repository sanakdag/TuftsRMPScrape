# SAN AKDAG - PS118/CS116 FINAL PROJECT
# avg_rating.py  ==> adds gender to the professor bio page
#					 change the gender and keyword values for
#					 different genders and pronouns
#					 i.e. he/him/his/guy
#						  she/her/hers
import os
import argparse


content = ""
count = 0
fname = ""
gender = "Male"
keyword = " he "
ind = 0
m = 0
f = 0
test = ""
to_print = set()

for file in os.listdir("./reviews"):
	if file.find("review") != -1:

		with open((os.path.join("./reviews", file)), "r") as fi:
			content = fi.readlines()
			g = 0
			c = 0
			for l in content:
				l = l.lower()
				n = l.find(keyword)
				if n != -1:
					print(file)
					print(l)
				g = g + n
				c = c + 1
			if (g + c != 0):
				count = count + 1
				fname = (os.path.join("./reviews", file))
				ind = fname.find("_review")
			
	if (count != 0):
		to_print.add(fname[:ind]+".txt")

	count = 0

for p in to_print:
	with open(p, "rw") as fil:
		print(p[10:])
		content=fil.readlines()
		text = ""
		for l in content:
			text += l
		if (text.find(gender) == -1):
			fil.write ("\n" + gender)

print ("m : " + str(m/515))
print ('f : ' + str(f/464))
