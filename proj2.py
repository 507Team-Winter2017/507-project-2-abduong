#proj2.py
import requests
from bs4 import BeautifulSoup
import re

#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

 
base_url = 'http://www.nytimes.com'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, "html.parser")
 
for story_heading in soup.find_all(class_="story-heading")[:10]: 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here

base_url_md = 'https://www.michigandaily.com/'
r_md = requests.get(base_url_md)
soup_md = BeautifulSoup(r_md.text, "html.parser")

most_read = soup_md.find_all('ol')
for A in most_read:
	print (A.get_text())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here

base_url_m = 'http://newmantaylor.com/gallery.html'
r_m = requests.get(base_url_m)
soup_m = BeautifulSoup(r_m.text, "html.parser")

imgs = soup_m('img')

for all in range(len(imgs)):
	try: 
		print (imgs[all]["alt"])
	except: 
		print ("No alternative text provided!!")



#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here


all_urls = []
for i in range(6):
	all_urls.append("https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page=" + str(i))

all_links = []
for U in all_urls:
	req = requests.get(U)
	soup_U = (BeautifulSoup(req.text, "html.parser"))
	for elem in soup_U.find_all('a', href=re.compile('\/node\/')):
		all_links.append((elem["href"]))


contact_us = []
for X in all_links:
	contact_us.append("https://www.si.umich.edu/" + X)

emails = []
num = 0
for prof in contact_us:
	R = requests.get(prof)
	soup_R = BeautifulSoup(R.text, "html.parser")
	for E in soup_R.find_all('a', href=re.compile('[a-zA-Z._+0-9]+@[a-zA-Z._+]+\.[a-zA-Z]{2,}')):
		if E["href"] not in emails:
			emails.append(E["href"].split(":")[1])

for em in emails:
	num +=1
	print (str(num) + " " + em)


# print (str(num) + " " + (E["href"]).split(":")[1])	

