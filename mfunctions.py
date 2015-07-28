import os

class MyFile:

	URL=""
	Name=""
	Extension=""
	Course=""
	Type=""

	def download(self,BASEDIR,HTTPSession):

		if not os.path.exists(os.path.join(BASEDIR, self.Course, self.Type)) :

			print "Made " + self.Course + "/" + self.Type
			os.makedirs(os.path.join( BASEDIR, self.Course, self.Type))

		if os.path.exists(os.path.join(BASEDIR, self.Course, self.Type, self.Name) + self.Extension) :
			print self.Name + self.Extension + " Already Exists"
			return

		localFile = open(os.path.join(BASEDIR, self.Course, self.Type, self.Name) + self.Extension, "wb")  
		responseObject = HTTPSession.get(self.URL)
			
		if not responseObject.ok:
			print ("Something went wrong")
			os.remove(os.path.join(BASEDIR, self.Course, self.Type, self.Name) + self.Extension)
			return

		else :
			print "Downloading " + self.Name + self.Extension + " into " + self.Course + "/" + self.Type
			fileData = responseObject.content 
			localFile.write(fileData)

		localFile.close()

def validate(name):

	name = name.replace("?","")
	name = name.replace("<","")
	name = name.replace(">","")
	name = name.replace(":","")
	name = name.replace("|","")
	name = name.replace("\n","")
	name = name.replace("\t","")
	name = name.replace("/","")

	return name

def betterName(name):

	if name[len(name)- 4 :len(name)] == "File":
		name = name[0:len(name)-4]

	return name

def classify(name):

	if "Tut" in name or "tut" in name:
		return "Tutorials"

	if "Lec" in name or "lec" in name :
		return "Lectures"

	for num in range(1,30):

		if str(num) in name:
			return "Lectures"

		if "0"+str(num) in name:
			return "Lectures"

	return "Misc"

def getFileType(URL):

	fileTypes=[".pdf",".PDF",".xlsx",".pptx",".ppt",".xls",".txt",".TXT"]

	for fileType in fileTypes:

		if fileType in URL :
			return fileType
			
	return "none"

def getfileName(URL, filetype):

	indexEnd = URL.find(filetype)

	i = indexEnd - 1
	while URL[i]!="/" and i >= 0:
		i = i-1

	return URL[ i + 1 : indexEnd]
