#!/usr/bin/python
### IMP 
# https://wiki.ubuntu.com/Novacut/GStreamer1.0#element_link_many.28.29

import os
script_path=os.path.dirname(os.path.realpath(__file__))

import pygst
pygst.require("0.10")
import gst
import gtk
import pygtk
import sys
import traceback
import json
from pprint import pprint

from random import choice
import random

streams_file = 'streams.d/earthcam.json'

def getRandomVideo():
	
	# Open JSON
	stream_file = open(script_path + "/" + streams_file,'r')
	stream_data = json.load(stream_file)
	rtmp_url = stream_data["provider"]["streamer"]["url"]
	swfUrl = stream_data["provider"]["streamer"]["swfUrl"]

	selection = []
	for source in stream_data["provider"]["streamer"]["streams"]["source"]:
		# select only enabled videos
		if source["enabled"] == 'true':
			selection.append(source)

	# return random video
	random.jumpahead(1)
	select = choice(selection)
	uri = rtmp_url + ' swfURL=' + swfUrl + ' playpath=' + select["playpath"] + ' live=true buffer=20000'
	print uri
	return uri


class Main:

	def __init__(self):

		self.pipeline = gst.Pipeline("screensaver")

		self.rtmpsrc = gst.element_factory_make("rtmpsrc", "rtmpstream")

		self.rtmpsrc.set_uri(getRandomVideo())
#		self.rtmpsrc.set_uri("rtmp://video2.earthcam.com/fecnetwork swfUrl=http://www.earthcam.com/swf/cam_player_v2/ecnPlayer.swf playpath=4931.flv live=true buffer=200000")

		# first channel
		self.flvdemux = gst.element_factory_make("flvdemux", "flvdemux")
		self.decode = gst.element_factory_make("decodebin", "decode")
		self.videomix = gst.element_factory_make("videomixer", "videomixer")

		self.videobox1 = gst.element_factory_make("videobox", "videobox1")
		self.videobox1.set_property("alpha", 0.5)
		self.videobox1.set_property("border-alpha", 0)

		self.textoverlay = gst.element_factory_make("textoverlay", "textoverlay")
		self.textoverlay.set_property("text", "Stream Screensaver 0.2")
		self.textoverlay.set_property("font-desc", "Sans 6")
		self.textoverlay.set_property("halignment", 0)
		self.textoverlay.set_property("valignment", 1)

		self.sink = gst.element_factory_make("xvimagesink", "sink")
		self.sink.set_xwindow_id(window)

		self.pipeline.add_many(self.rtmpsrc, self.videobox1, self.videomix, self.textoverlay, self.flvdemux, self.decode, self.sink)
		
		## link them all together
		# channel 1 
		self.rtmpsrc.link(self.flvdemux)
		self.textoverlay.link(self.videobox1)
		self.videobox1.link(self.videomix)
		self.videomix.link(self.sink)

		self.flvdemux.connect("pad-added", self.OnDemuxPadAdded)
		self.decode.connect("pad-added", self.OnDecodePadAdded)
		self.decode.connect("pad-removed", self.OnDecodePadRemoved)
		self.pipeline.set_state(gst.STATE_PLAYING)


	def OnDemuxPadAdded(self, demuxer, pad):
		pad.link(self.decode.get_pad("sink"))
	
	def OnDemuxPadRemoved(self, demuxer, pad):
		print "demuxPadRemoved"

	def OnDecodePadAdded(self, decoded, pad):
		pad.link(self.textoverlay.get_pad("video_sink"))
	
	def OnDecodePadRemoved(self, demuxer, pad):
		print "decodePadRemoved"
	
try:
	window=int(sys.argv[1], 16)
	while True:
		start=Main()
		gtk.main()
except: 
	traceback.print_exc(file=sys.stdout)
