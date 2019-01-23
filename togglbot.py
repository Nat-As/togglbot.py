#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import time
import datetime
import http.client
import urllib2
import requests
import json
import sys
import re
import os
import random
import subprocess

from time import sleep
from dateutil.tz import tzoffset
from urlparse import urlparse
from six.moves.urllib.parse import urlparse
from random import randint
from HTMLParser import HTMLParser
if ((3, 0) <= sys.version_info <= (3, 9)):
    from urllib.parse import urlparse
elif ((2, 0) <= sys.version_info <= (2, 9)):
    from urlparse import urlparse

ustring = "jandrews7348@floridapoly.edu:PASSWORD"
username = "email@floridapoly.edu"
password = "Password123"

now = datetime.datetime.now()
time = now.hour

while now.hour > 7:
	now = datetime.datetime.now()
	time = now.hour
	print now.hour, now.minute
# SEED
	slotv1 = int(randint(1200,3600))
	slotv2 = randint(1200,3600)
	slotv3 = randint(1200,3600)
	slotv4 = randint(1200,3600)
	slotv5 = randint(1200,3600)
	slotv6 = randint(1200,3600)
	slotv7 = randint(1200,3600)
	slotv8 = randint(1200,3600)
	
	#Add more activities to add more entropy and make it more interesting! |
	
	hw = ["Calculus", "Break", "Study", "Physics", "LAB", "Misc.", "Robotics", "Programming", "Study group", "Project", "C&M"]
	#LOG DATA (before sending)
	
	hw1 = random.choice(hw)
	hw2 = random.choice(hw)
	hw3 = random.choice(hw)
	hw4 = random.choice(hw)
	hw5 = random.choice(hw)
	hw6 = random.choice(hw)
	hw7 = random.choice(hw)
	hw8 = random.choice(hw)
	
	# Get API Token
	wid = 3164178
	APIT = str(os.popen('curl -s -u %s -X POST https://www.toggl.com/api/v8/reset_token | sed \'s/"//g\'' % ustring).read())
	
	# Test Token
	if len(APIT) > 1:
		print "--> Connected"
		print "Token:", APIT
		
	
# Build string
	
# Date
	now = datetime.datetime.now(tzoffset('EDT', +4*60*60)).replace(microsecond=0)
	sdate = now.isoformat()
	# JSON Data
	time_entry1 = {'time_entry':{
	                "description": hw1,
	                "start": sdate,
	                "duration": slotv1,
	                "created_with": "togglbot"
	}}
# Check JSON
	print "--> Request Sent:", time_entry1
	
	# Shell request 2.0 (cURL)
	# os.system('curl -u '+str(os.popen('curl -s -u %s -X POST https://www.toggl.com/api/v8/reset_token | sed \'s/\"//g\'' % ustring).read())+':api_token -H \"Content-Type: application/json\" -d \'{\"time_entry\":{\"description\":\"'+str(random.choice(hw))+'\",\"created_with\":\"togglbot\",\"start\":'+str(os.popen('date --rfc-3339=seconds | sed \'s/ /T/g\'').read())+',duration:'+str(int(randint(1200,3600)))+',\"wid\":3164178}}\' -X POST https://www.toggl.com/api/v8/time_entries')
	
# Python Request 3.0
	request1 = requests.post('https://www.toggl.com/api/v8/time_entries', auth=(APIT, 'api_token'), data=json.dumps(time_entry1))
	if not request1: # request.Response returns True if status 'OK'
		print(request1.text)

	i = slotv1
	while i != 0:
		print i
		sleep(1)
		i = i - 1
		sys.stdout.write("\033[F")
		if i == 0:
			break
	now = datetime.datetime.now()

