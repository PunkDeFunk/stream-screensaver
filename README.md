#stream-screensaver - a linux video streaming screensaver
There are nice live videos all over the Internet. Why not run a screensaver out of em'? 

#DISCLAIMER:
I am not responsible for excessive bandwidth usage.
Make sure that you understand the terms and conditions of websites you are streaming from.

#TARGETS: 
ustream.tv
earthcam.com
justin.tv (?)
Anything you can think of...

#SUPPORT:
Linux

#PREREQUISITES: 
xscreensaver
mplayer
rtmpdump 

#HOWTO: 
1 - get the rtmp stream address using voodoo magic (or simply use ustream-recorder to get the rtmp stream information - https://github.com/kenorb/UStream-recorder) -- Soon information will be in XML files... 

2 - setup xscreensaver. 
vi ~/.xscreensaver 
Insert after your last screensaver 
"Stream ScreenSaver" /path/to/bin/stream-screensaver/stream.py $XSCREENSAVER_WINDOW \n\

3 - Enable screensaver using xscreensaver-demo
Select Stream Screensaver in xscreensaver-demo

4 - Lock your session and see if it works. 
It might take some time to load the stream.
