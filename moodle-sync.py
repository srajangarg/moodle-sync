import requests, os
from bs4 import BeautifulSoup
from mfunctions import *
from urlparse import urljoin

loginURL = "http://moodle.iitb.ac.in/login/index.php"
HTTPSession = requests.session()

userPrefs = open("preferences.txt").read().splitlines()

loginData = {'username':userPrefs[0] ,'password':userPrefs[1]}
BASEDIR = userPrefs[2]
if not os.path.exists(BASEDIR):
	os.makedirs(BASEDIR)  

# Moodle Scrape 
afterLoginPage = HTTPSession.post(loginURL, data = loginData )
afterLoginPage = HTTPSession.get('http://moodle.iitb.ac.in/my/')

mainPageSoup = BeautifulSoup(afterLoginPage.content)
Courses = mainPageSoup.select("li.type_course.depth_3")
Courses = filter(lambda course : course.text.find("2015-1") != -1, Courses)

for currCourse in Courses:

	courseFolderName = currCourse.text[0:6]
	courseURL = currCourse.find("a")["href"]

	coursePage = HTTPSession.get(courseURL)	
	courseSoup = BeautifulSoup(coursePage.content)

	linksOnPage = courseSoup.select("li.resource")
	foldersOnPage = courseSoup.select("li.folder")

	currFile = MyFile()

	for link in linksOnPage :

		currFile.Name = validate( betterName(link.find("a").text) )
		currFile.URL = link.find("a")["href"]
		currFile.Course = courseFolderName
		currFile.Type = classify(currFile.Name)
		tempPage = HTTPSession.get(currFile.URL)
		currFile.URL = tempPage.url
		currFile.Extension = getFileType(currFile.URL)
		
		currFile.download(BASEDIR, HTTPSession)

	for folder in foldersOnPage :

		folderUrl = folder.find("a")["href"]
		folderPage = HTTPSession.get(folderUrl)
		folderPageSoup = BeautifulSoup(folderPage.content)

		allAtags = folderPageSoup.find_all("a")

		for Atag in allAtags :

			try :
				currFile.Extension = getFileType(Atag["href"])
			except :
				continue

			if currFile.Extension != "none":

				currFile.URL = Atag["href"]
				currFile.Course = courseFolderName
				currFile.Name = Atag.text.split(".")[0]
				currFile.Type = classify(currFile.Name)

				currFile.download(BASEDIR, HTTPSession)

# IndiPAge Scrape
indiPages = open("indipages.txt").read().splitlines()

for line in indiPages:

	courseFolderName = line[0:6]
	siteURL = line[7:len(line)]

	page = HTTPSession.get(siteURL)
	pageSoup = BeautifulSoup(page.content)

	currFile = MyFile()
	allAtags = pageSoup.find_all("a")

	for Atag in allAtags:

		fileURL = Atag["href"]
		fileURL = urljoin(siteURL, fileURL)
		currFile.Extension = getFileType(fileURL)

		if currFile.Extension != "none":

			currFile.URL = fileURL
			currFile.Name = getfileName(fileURL, currFile.Extension)
			currFile.Type = classify(currFile.Name)
			currFile.Course = courseFolderName
			currFile.download(BASEDIR, HTTPSession)




