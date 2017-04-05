import sys
import os
import urllib

totalcmd = len(sys.argv)

if len(sys.argv) < 2:
	print ('Usage: parseCovers.py source_folder_path')
	exit(1)

source_folder = str(sys.argv[1])

#print ('Source Folder: %s' % source_folder)

idx = 0
print '|Name|Cover|'
print '|----|-----|'
strline = '|'
for file in os.listdir(source_folder):
	if file.endswith(".png"):
		strline += file + '|'
		strline += '<img src="https://raw.githubusercontent.com/angelmic/eBooks/master/_Covers/'
		strline += file
		strline += '" width="100" height="150" />|'

		#strline += '!["' + file + '""](' 
		#strline +=  'https://raw.githubusercontent.com/angelmic/eBooks/master/_Covers/'
		#strline += urllib.quote(file) + '?raw=true' + ')|'

		#strline += '\n'
		print strline
		strline = '|'
