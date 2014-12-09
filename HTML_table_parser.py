from HTMLParser import HTMLParser
#from lxml.html import parse
import urllib2

#Constants
tableString = "table"
fileListLocation = "PAPAurls/PAPAurls.txt"

#Variables
inTable=0
iteration=0
curTable=""

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
		#print "Encountered a start tag:", tag
		global inTable
		if tag=="table":
			inTable=1
			print "Encountered start of", tag
    def handle_endtag(self, tag):
		#print "Encountered an end tag :", tag
		global inTable
		if tag=="table":
			inTable=2	
			print "Encountered end of", tag
    def handle_data(self, data):
		global curTable
		if inTable==1:
			#print "Encountered some data  :", data
			curTable+=data
			#curTable+=","

# instantiate the parser 
parser = MyHTMLParser()


# From list of websites pull in tables
infile = open(fileListLocation, "r")
for line in infile:
	iteration +=1
	
	req = urllib2.Request(line)
	response = urllib2.urlopen(req)
	the_page = response.read()
	
	
	#Error here from BAD HTML, delete first line
	sansfirstline = '\n'.join(the_page.split('\n')[1:]) 
	
	#Make new curTable
	curTable=""
	#Feed HTML 
	parser.feed(sansfirstline)
	#Save table as an output file
	with open("PAPAtables/table"+str(iteration)+".txt", "w") as text_file:
		text_file.write(curTable)
	
