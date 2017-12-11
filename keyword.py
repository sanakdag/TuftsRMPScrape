# avg_rating.py  ==> finds the keyword in all reviews
#					 use python3 keyword.py -h for a helpful message

import os
import argparse
from collections import Counter
parser = argparse.ArgumentParser(description='Query the scraped reviews for a keyword. Optional filter by department or gender \n Needs -f or -p to print anything.' )


parser.add_argument('-s', metavar='STRING', type=str, help= 'keyword to search')
	
parser.add_argument('-f', metavar='FILTER', type=str, help= 'filter options: "gender" or "dept"')

parser.add_argument('-v', action='store_true', help='verbose')
parser.add_argument('-n', action='store_true', help='normalize the results based on the number of reviews for either gender total')

parser.add_argument('-l', metavar='LIST', type=str, help='reads query options from file a .txt file LIST')
parser.add_argument('-p', action='store_true', help='print the reviews and filenames where keyword appears')

args = parser.parse_args();

to_print_profs = set()
	
num_male = 515
num_male_reviews = 5491
num_female = 464
num_female_reviews = 3913

keyword = "sweet"

if args.s != None:
	keyword = args.s

def print_lines(lines):
	for (f,l) in lines:
		print(f)
		print(l)

def query(key):
	content = ""
	count = 0
	fname = ""
	ind = 0
	test = ""
	lines = []
	lenl = 0
	for file in os.listdir("./reviews"):
		if file.find("review")!=-1:
			#print(os.path.join("./reviews", file))
			with open((os.path.join("./reviews", file)), "r") as fi:
				content = fi.readlines()
				g = 0
				c = 0
				read = False
				for l in content:
					l = l.lower()
					if read:
						n = l.find(key)
						if n != -1:
							lines.append((file,l))
							lenl = len(l)
						g = g + n
						c = c + 1
						if (g + c != 0):
							count = count + 1
							fname = (os.path.join("./reviews", file))
							ind = fname.find("_review")
					if l.find("grade received") != -1:
						read = True 
		if (count != 0):
			if (ind != -1):
				to_print_profs.add(((fname[:ind]+".txt"), lenl))
		count = 0
	if args.p:
		print_lines(lines)
		# if args.v:
		# 	print_lines(lines)

def dept(key):
	depts = []
	for (p,count) in to_print_profs:
		with open(p, "r") as fil:
			content=fil.readlines()
			for l in content:
				i = l.find("the ")
				if (i != -1):
					dept = l[i+4:-12]
				i2 = l.find("Male")
				i3 = l.find("Female")
				if (i2 != -1):
					depts.append((dept, "M"))
				if (i3 != -1):
					depts.append((dept, "W"))

	breakdown = Counter(depts)
	breakdown = breakdown.most_common()
	if args.v:
		print("Note: Percent share of reviews with keyword = " + key)
	t = 0
	for (d,c) in breakdown:
		t = t + c

	for ((d,g),c) in breakdown:
		if (c/t*100 >1):
			if args.v:
				print (d +" ("+g+") " + " : " + str('%.3f'%((c/t)*100)) + "%  "+ "("+str(c)+")")
			elif args.n:
				if (g == "M"):
					print (d +" ("+g+")" + "," + str('%.3f'%((c/num_male_reviews)*100)))
				else:
					print (d +" ("+g+")" + "," + str('%.3f'%((c/num_female_reviews)*100)))
			else:
				print(d + " " + g + ": " + str(c))
	to_print_profs.clear()

def gender(key):
	rm = 0
	rf = 0
	f = 0
	m = 0
	t = 0
	mline = 0
	fline = 0
	afline = 0
	amline = 0
	for (p,c) in to_print_profs:
		with open(p, "r") as fil:
			#print(p[10:-4])
			content=fil.readlines()
			for l in content:
				if (l.find("Male") != -1):
					mline += c
					t = t+1
					m = m + 1
				if (l.find("Female") != -1):
					fline += c
					f = f + 1
					t = t+1
	if t != 0 :
		nrm = m/num_male_reviews * 100
		nrf = f/num_female_reviews * 100
		rm = m/t * 100
		rf = f/t * 100
		if f != 0:
			afline = fline/f
		if m != 0:
			amline = mline/m
		if args.v and args.n:
			print("Note: normalized gender breakdown of reviews containing keyword = " + key)
			print ("m : " + str('%.3f'%nrm) + "% (" + str(m) + ") - avg review length = " + str('%.1f'%amline) + " chars")
			print ('f : ' + str('%.3f'%nrf) + "% (" + str(f) + ") - avg review length = " + str('%.1f'%afline) + " chars")
		elif args.v:
			print("Note: gender breakdown of reviews containing keyword = " + key)
			print ("m : " + str('%.3f'%rm) + "% (" + str(m) + ") - avg review length = " + str('%.1f'%amline) + " chars")
			print ('f : ' + str('%.3f'%rf) + "% (" + str(f) + ") - avg review length = " + str('%.1f'%afline) + " chars")
		elif args.n:
			print(keyword + "," + str('%.3f'%nrm) + ","+ str(m) + "," + str('%.3f'%nrf)+ ","+ str(f))
		else:
			print(str('%.3f'%rm) + " ("+ str(m) + ") " + " : " +str('%.3f'%rf)+ " ("+ str(f) +") ")
		m = 0
		f = 0
	else:
		print("No reviews with keyword " + key)
	to_print_profs.clear()


if args.f == None:
	if args.s == None:
		parser.print_help()
	else:
		query(keyword)
elif args.l != None:
	words = []
	with open(args.l, "r") as fi:
		words = fi.readlines()
	for w in words:
		keyword = w[:-1]
		query(keyword)
		if args.f == "gender":
			gender(keyword)
		if args.f == "dept":
			dept(keyword)
elif args.f == "gender":
	query(keyword)
	gender(keyword)
elif args.f == "dept":
	query(keyword)
	dept(keyword)
else:
	parser.print_help()
