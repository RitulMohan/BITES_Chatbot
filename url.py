import urllib.request as urllib2
from bs4 import BeautifulSoup

#response = urllib2.urlopen('https://www.thefitindian.com/blog/hostel-pg-college-going-students-diet/')
# response = urllib2.urlopen('')
# html = response.read()
# soup = BeautifulSoup(html)
# lis = []
# for tag in soup.find_all(class_="ftwp-heading") :
  
# 	print(tag.attrs)
#print(html)
def topFood():
	response = urllib2.urlopen('https://www.thefitindian.com/blog/hostel-pg-college-going-students-diet/')
	html = response.read()
	#print(html)
	soup = BeautifulSoup(html, 'html.parser')
	foods = []
	for title in soup.find_all(class_="ez-toc-list") :	
		items = [item.text.encode("utf-8") for item in title.select('li')]
		#print(items)
		foods = items
	return foods
#
