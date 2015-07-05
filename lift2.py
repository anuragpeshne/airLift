import urllib2
import re
import os
from os import listdir
import os.path
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
            fileReq = urllib2.Request(sourceLocation + currentLocation + anchor)
            if not os.path.exists(unloadLocation +
                    urllib2.unquote(currentLocation)):
                os.makedirs(unloadLocation + urllib2.unquote(currentLocation))
            if not os.path.isfile(unloadLocation +
                    urllib2.unquote(currentLocation + anchor)):
                local_file = open(unloadLocation +
                        urllib2.unquote(currentLocation + anchor), 'wb')
                local_file.write(urllib2.urlopen(fileReq).read())
                local_file.close()
                print(unloadLocation + urllib2.unquote(currentLocation))
            else:
                print(urllib2.unquote(anchor) + ' exists, skipping...')

if len(sys.argv) < 2:
    print("airLift: enter remote location and port number\n" +
            "Example: python lift.py http://192.168.0.1:8000")
    sys.exit(0) #fatal
sourceLocation = sys.argv[1]
if len(sys.argv) > 2:
    targetFileTypes = sys.argv[2:]
else:
    targetFileTypes = ['.txt','.pdf']
    print('Note: No file extension specified')
print('Will copy ' + ','.join(targetFileTypes))
userHome = expanduser("~")
unloadLocation = userHome + '/Downloads'
print('unloading stuff at ' + unloadLocation)
anchorRe = re.compile('<a href=[\'"](.*)[\'"]>', re.I)
isDirRe = re.compile('/$')
targetFileRe = re.compile('(' + '|'.join(targetFileTypes)+')$', re.I)
lift('/')
