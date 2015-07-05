import urllib
import urllib.request
import re
import os
from os import listdir
import os.path
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
            fileReq = urllib.request.Request(sourceLocation +
                    currentLocation + anchor)
            if not os.path.exists(
                unloadLocation + urllib.parse.unquote(currentLocation)
            ):
                os.makedirs(
                    unloadLocation + urllib.parse.unquote(currentLocation)
                )
            if not os.path.isfile(
                unloadLocation +
                urllib.parse.unquote(currentLocation) +
                urllib.parse.unquote(anchor)
            ):
                local_file = open(
                    unloadLocation +
                    urllib.parse.unquote(currentLocation) +
                    urllib.parse.unquote(anchor),
                    'wb'
                )
                local_file.write(urllib.request.urlopen(fileReq).read())
                local_file.close()
                print(unloadLocation + urllib.parse.unquote(currentLocation))
            else:
                print(urllib.parse.unquote(anchor) + ' exists, skipping...')

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
print('unloading stuff at '+unloadLocation)
anchorRe = re.compile('<a href=[\'"](.*)[\'"]>', re.I)
isDirRe = re.compile('/$')
targetFileRe = re.compile('(' + '|'.join(targetFileTypes)+')$', re.I)
lift('/')
