#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import datetime
import urllib2
import requests
import json
import sys
import re
import random
import subprocess
import base64
import getpass

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

# Ask and encrypt username and passcode
print "IMPORTANT!"
print "Format Must be USERNAME:PASSWORD\n"
passk = getpass.getpass("Enter your username:password ==> ")

key = base64.b64encode(passk)

now = datetime.datetime.now()
time = now.hour

while True:
	now = datetime.datetime.now()
	time = now.hour
	print "+ Logging in...\n" # Jump to line 68
	print now.hour, now.minute
# SEED
	slotv1 = int(randint(1200,3600))
	slotv2 = randint(1200,3600)
	
	#Add more activities to add more entropy and make it more interesting! |
	
	hw = ["Calculus", "Break", "Study", "Physics", "LAB", "Misc.", "Robotics", "Programming", "Study group", "Project", "C&M"]
	#LOG DATA (before sending)
	
	hw1 = random.choice(hw)
	hw2 = random.choice(hw)
	
	# Get API Token
	wid = 3164178
	headers = { 'Authorization' : 'Basic %s' %  key }
	tokenrequest = requests.post('https://www.toggl.com/api/v8/reset_token', headers=headers)
	
	# Did it work?
	print "Status:", tokenrequest.status_code
	
	# Login failed case
	if tokenrequest.status_code != 200:
            print "Login Error!"
            break
		
	# Login success case
	API = tokenrequest.text
	APIT = json.loads(API)
	
	# Test Token
	if len(APIT) > 1:
		print "--> Connected"
		print "Token:", APIT

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
	
# Python Request 3.0
	request1 = requests.post('https://www.toggl.com/api/v8/time_entries', auth=(APIT, 'api_token'), data=json.dumps(time_entry1))
	if not request1: # request.Response returns True if status 'OK'
		print(request1.text)

	i = slotv1
	while i != 0:
		print ("Next request in: %s\r" % i)
		sleep(1)
		i = i - 1
		if i == 0:
			break
	now = datetime.datetime.now()

