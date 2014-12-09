import os
import re

#Variables

tableFolder = "PAPAtables"
prev_line = ''

#Open every file
for filename in os.listdir(tableFolder):
	fpath = os.path.join(tableFolder, filename)
	with open(fpath, 'r+') as f:
		lines = f.readlines()
		f.seek(0)
		f.truncate()
		for line in lines:
			#Delete every tab
			line = line.replace('\t' , '')
			#Remove double spaces
			if line=='\n' and prev_line=='\n':
				line = line.replace('\n' , '')
			#Use Regex to find lines with characters before newline, and replace them with tab
			if re.match('.+\n', line) != None:
				line = line.replace('\n' , '\t')
			line = line.replace(',' , '')
			f.write(line)
			#Set previous line to this line
			prev_line = line
		#File is still open. Continue to format
		
		



