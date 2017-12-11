from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pathlib

option = webdriver.ChromeOptions()
option.add_argument("--start-maximized")
option.add_argument("--ignore-certificate-errors")
option.add_extension("/Users/sanozan7/Desktop/TUFTS/year3/comp116/final/Adblock-Plus_v1.13.4.crx")
browser = webdriver.Chrome(executable_path='/Users/sanozan7/Desktop/TUFTS/year3/comp116/final/chromedriver', chrome_options=option)
browser.get("http://www.google.com/")
window_before = browser.window_handles[1] 
browser.switch_to_window(window_before)
actions = ActionChains(browser)




fname = "proflist.txt"

with open(fname) as f:
    content = f.readlines()

# remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content]


test = True

for id in content:
	print(id)
	rev = set()


	# Load a page 
	browser.get('http://www.ratemyprofessors.com/ShowRatings.jsp?tid='+ id)
	# checking if dialog box pops up
	if test:
		browser.find_element_by_css_selector('.btn').click()
		test = False
	#finding professor info 
	name = browser.find_elements_by_class_name("boxfitted")
	prof = ""
	for n in name:
		prof+=(n.text)
	prof=prof.replace(" ", "_")

	# load more button loop to bottom of page	
	while True:
		try: browser.find_element_by_id('loadMore').click()
		except: 
			break

	count = 0

	#finds all of the reviews in the HTML
	reviews = browser.find_elements_by_tag_name("tr")
	
	#finds department info for prof in HTML
	dept = browser.find_elements_by_class_name("result-title")
	
	#creates a prof bio file
	fname = prof+".txt"
	file = open(fname, 'w')
	for d in dept:
	 	text = d.text
	 	ind = text.find ("ARE")
	 	file.write(prof+"\n"+text[:ind])



	for r in reviews:
		if (r.text != ""):
			rev.add(r.text)


	# saves the individual reviews 
	for re in rev:

		if (count != 0):
			fname=prof+"_review"+str(count)+".txt"
			f1 = open(fname, 'w')
			if (re != ""):
				f1.write(re)
		count=count+1



