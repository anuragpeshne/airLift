import urllib2
import re
import os
from os import listdir
from os.path import expanduser
import sys

def lift(currentLocation):
    req = urllib2.Request(sourceLocation + currentLocation)
    page = urllib2.urlopen(req)
    webpage = page.read().decode(encoding = 'UTF-8')
    anchors = anchorRe.findall(webpage + currentLocation)
    for anchor in anchors:
        if isDirRe.search(anchor):
            lift(currentLocation + anchor)
        elif(targetFileRe.search(anchor)):
            fileReq = urllib2.Request(sourceLocation+currentLocation+anchor)
            if not os.path.exists(unloadLocation + urllib2.unquote(currentLocation)):
                os.makedirs(unloadLocation + urllib2.unquote(currentLocation))
            local_file = open(unloadLocation + urllib2.unquote(currentLocation) + anchor, 'wb')
            local_file.write(urllib2.urlopen(fileReq).read())
            local_file.close()
            print(unloadLocation + urllib2.unquote(currentLocation))

userHome = expanduser("~")
unloadLocation = userHome + '/Downloads'
print('unloading stuff at '+unloadLocation)
targetFileTypes = ['.txt','.djvu']
sourceLocation = sys.argv[1]
anchorRe = re.compile('<a href=[\'"](.*)[\'"]>', re.I)
isDirRe = re.compile('/$')
targetFileRe = re.compile('(' + '|'.join(targetFileTypes)+')$', re.I)
lift('/')
