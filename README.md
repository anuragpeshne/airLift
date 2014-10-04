airLift
=======

easiest way to transfer files between computers over network.

### How-To
1. Fire up any http server on host machine which serves the files to be transfered.
2. If you are on *nix then easiest way would be to 'cd' into root directory of files to be transfered and entering
    ```'python3 -m http.server'```
3. Get the IP Address by executing ```ifconfig```
3. Edit lift.py to select type of files to be transfered.
4. Run ```lift.py {ipAddress:port}```
5. Profit!
