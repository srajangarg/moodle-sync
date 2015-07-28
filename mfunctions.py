class MyFile:

	URL=""
	Name=""
	Extension=""
	Course=""
	Type=""

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

	if name[len(name)-4:len(name)]=="File":
		name=name[0:len(name)-4]

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

def download(self,BASEDIR,HTTPSession):

	if not os.path.exists(os.path.join(BASEDIR, self.Course, self.Type)) :

		print "Made " + self.Course + "/" + self.Type
		os.makedirs(os.path.join( BASEDIR, self.Course, self.Type))