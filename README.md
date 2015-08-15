airLift
=======

easiest way to transfer files between computers over network.

### How-To
1. Fire up any http server on host machine which serves the files to be transfered.
1. If you are on *nix then easiest way would be to 'cd' into root directory of files to be transfered and entering
    ```python3 -m http.server``` or ```python -m SimpleHTTPServer```
1. Get the IP Address by executing ```ifconfig```
1. Execute ```python lift2.py {ipAddress:port} {extension}```
   You can also pass file extension in arguments. Example: ```python lift2.py http://10.0.0.7:8000 mp4```
1. Profit!
