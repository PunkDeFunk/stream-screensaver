#!/usr/bin/python
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

import logging
import sys
import time
import os
import subprocess
from subprocess import PIPE, Popen

### Set working directory
os.chdir(sys.path[0])

### Handle window ID 
### TODO: parse arguments 
window=sys.argv[1]

### Here we go
if __name__ == '__main__':
    
    ## TODO: If there's already a screensaver process running, stop it and start this newly called one
    ## TODO: Parse data from XML file in streams.d/
    ## TODO: Select a random stream, from a random provider
    ## TODO: Check if stream works before starting it up.
    ## TODO: Hook with ustream-RTMPdump.py

    # STATIC configs for uStream
    # addr="rtmp://ustreamlivefs.fplive.net/ustream4live-live//stream_live_1_1_9408562"
    # addr="rtmp://ustreamlivefs.fplive.net/ustream3live-live//stream_live_1_1_6540154"
    

    #### generic caller for ISS Space Station 
    # cmd1="/usr/bin/rtmpdump --live -q -r "+addr+ "-W http://static-cdn1.ustream.tv/swf/live/viewer.swf"
    
    ## Time square from EarthCAM.com
    cmd1="rtmpdump --live -q -r rtmp://video2.earthcam.com/fecnetwork -W http://www.earthcam.com/swf/cam_player_v2/ecnPlayer.swf -y 4017timessquare.flv"
    cmd2="/usr/bin/mplayer -nosound -nogui -noconsolecontrols -really-quiet -nolirc -nostop-xscreensaver -wid "+window+" -fs -loop 0 -cache 4096 -"

    ### replace for debug mode
    # cmd2="/usr/bin/mplayer -nosound -nogui -noconsolecontrols -really-quiet -nolirc -nostop-xscreensaver -loop 0 -"
    
    player = Popen(cmd1 + " | " + cmd2, shell=True, preexec_fn=os.setsid)

    ### TODO: Handle preview mode if preview then no watcher.
    ## TODO: Use python for watcher
    watcher = Popen('./stream-watcher.pl',stdout=PIPE)
