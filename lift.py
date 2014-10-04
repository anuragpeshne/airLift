import urllib
import urllib.request
import re
import os
from os import listdir
from os.path import expanduser
import sys

def lift(currentLocation):
	req = urllib.request.Request(sourceLocation + currentLocation)
	page = urllib.request.urlopen(req)
	webpage = page.read().decode(encoding = 'UTF-8')
	anchors = anchorRe.findall(webpage + currentLocation)
	for anchor in anchors:
		if isDirRe.search(anchor):
			lift(currentLocation + anchor)
		elif(targetFileRe.search(anchor)):
			fileReq = urllib.request.Request(sourceLocation+currentLocation+anchor)
			if not os.path.exists(unloadLocation + urllib.parse.unquote(currentLocation)):
			    os.makedirs(unloadLocation + urllib.parse.unquote(currentLocation))
			local_file = open(unloadLocation + urllib.parse.unquote(currentLocation) + anchor, 'wb')
			local_file.write(urllib.request.urlopen(fileReq).read())
			local_file.close()
			print(unloadLocation + urllib.parse.unquote(currentLocation))

userHome = expanduser("~")
unloadLocation = userHome + '/Downloads'
print('unloading stuff at '+unloadLocation)
targetFileTypes = ['.pdf','.djvu']
sourceLocation = sys.argv[1]
anchorRe = re.compile('<a href=[\'"](.*)[\'"]>', re.I)
isDirRe = re.compile('/$')
targetFileRe = re.compile('(' + '|'.join(targetFileTypes)+')$', re.I)
lift('/')
