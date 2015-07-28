import requests
import os
<<<<<<< HEAD
=======
import sys # for the error message
>>>>>>> c3bdcd0ef20f7d89230ee4c44a0022fee8bc95ed
from bs4 import BeautifulSoup
from mfunctions import *

loginURL = "http://moodle.iitb.ac.in/login/index.php"
HTTPSession = requests.session()

<<<<<<< HEAD
=======
if not os.path.isfile("preferences.txt"):
	sys.exit("Please create a preferences.txt with first line as your LDAP ID and the second as your password.") 

>>>>>>> c3bdcd0ef20f7d89230ee4c44a0022fee8bc95ed
userPrefs = open("preferences.txt").read().splitlines()

loginData = {'username':userPrefs[0] ,'password':userPrefs[1]}

afterLoginPage = HTTPSession.post(loginURL, data = loginData )
afterLoginPage = HTTPSession.get('http://moodle.iitb.ac.in/my/')

mainPageSoup = BeautifulSoup(afterLoginPage.content)
Courses = mainPageSoup.select("li.type_course.depth_3")

BASEDIR = "MoodleSyncFiles"

if not os.path.exists(BASEDIR):
	os.makedirs(BASEDIR)  

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
<<<<<<< HEAD
		#Download if already doesn't exist!
=======

		if currFile.Extension != "none":
			currFile.download(BASEDIR,HTTPSession)
>>>>>>> c3bdcd0ef20f7d89230ee4c44a0022fee8bc95ed

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
<<<<<<< HEAD

				currFile.Name = Atag.text.split(".")[0]
				currFile.Type = classify(currFile.Name)
				#Download if already doesn't exist!
=======
				currFile.Name = Atag.text.split(".")[0]
				currFile.Type = classify(currFile.Name)
				
				currFile.download(BASEDIR,HTTPSession)

>>>>>>> c3bdcd0ef20f7d89230ee4c44a0022fee8bc95ed
