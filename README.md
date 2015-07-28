# Moodle Sync IIT Bombay

## Dependencies
* Python 2.7
* beautifulsoup4
* requests

## Usage
* Make a **preferences.txt** and **indipages.txt**, place them along with the script
* **preferences.txt** should have your LDAP ID as first line, LDAP PASSWORD as second line, and the absolute path to the folder you want to save the files too.
* **indipages.txt** should contain the Urls from where to directly pick up the files fo the course.   Each line should contain info about one course in this *SPECIFIC* format (COURSECODE:URL) (eg. "MA 106:http://math.iitb.ac.in/~keshari/MA106.html") The URL should link directly to the files
* Run the script trivially