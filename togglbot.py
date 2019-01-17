#!/usr/bin/python

#James Andrews
#Jandrews7348@floridapoly.edu
#2019-01-09 14:21:38

import datetime
import http.client
import urllib2
import requests
import json
import sys
import re
import os
import platform
import random
import subprocess

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

# SEED
seed = randint(11111,99999)
slotv1 = int(randint(1200,3600))
slotv2 = randint(1200,3600)
slotv3 = randint(1200,3600)
slotv4 = randint(1200,3600)
slotv5 = randint(1200,3600)
slotv6 = randint(1200,3600)
slotv7 = randint(1200,3600)
slotv8 = randint(1200,3600)

date = datetime.datetime.now()
#Add more activities to add more entropy and make it more interesting! |

hw = ["Calculus", "Break", "Study", "Physics", "LAB", "Misc.", "Robotics", "Programming", "Study group", "Project", "C&M"]
#LOG DATA (before sending)


print slotv1 / 60, "Minutes", random.choice(hw)
print slotv2 / 60, "Minutes", random.choice(hw)
print slotv3 / 60, "Minutes", random.choice(hw)
print slotv4 / 60, "Minutes", random.choice(hw)
print slotv5 / 60, "Minutes", random.choice(hw)
print slotv6 / 60, "Minutes", random.choice(hw)
print slotv7 / 60, "Minutes", random.choice(hw)
print slotv8 / 60, "Minutes", random.choice(hw)

v1 = slotv1, "Minutes", random.choice(hw)
v2 = slotv2, "Minutes", random.choice(hw)
v3 = slotv3, "Minutes", random.choice(hw)
v4 = slotv4, "Minutes", random.choice(hw)
v5 = slotv5, "Minutes", random.choice(hw)
v6 = slotv6, "Minutes", random.choice(hw)
v7 = slotv7, "Minutes", random.choice(hw)
v8 = slotv8, "Minutes", random.choice(hw)

hw1 = str(random.choice(hw))
hw2 = random.choice(hw)
hw3 = random.choice(hw)
hw4 = random.choice(hw)
hw5 = random.choice(hw)
hw6 = random.choice(hw)
hw7 = random.choice(hw)
hw8 = random.choice(hw)

# Get API Token
wid = 3164178
os.system('echo running shell...')
APIT = str(os.popen('curl -s -u %s -X POST https://www.toggl.com/api/v8/reset_token | sed \'s/"//g\'' % ustring).read())
print "Token:", APIT

# Make Project

sdate = str(os.popen('date --rfc-3339=seconds | sed \'s/ /T/g\'').read())

# Build string
#scommand = ("curl -v -u %s:api_token -H \"Content-Type: application/json\"\'{\"time_entry\":{\"description\":\"%s\",\"created_with\":\"togglbot\",\"start\":\"%s\",\"duration\":%i,\"wid\":3164178}}\' -X POST https://www.toggl.com/api/v8/time_entries" % APIT, hw1, sdate, slotv1)
#os.system(scommand)

# Build request 2.0
os.system('curl -u '+str(os.popen('curl -s -u %s -X POST https://www.toggl.com/api/v8/reset_token | sed \'s/"//g\'' % ustring).read())+':api_token -H \"Content-Type: application/json\"\'{\"time_entry\":{\"description\":'+str(random.choice(hw))+',\"created_with\":\"togglbot\",\"start\":'+str(os.popen('date --rfc-3339=seconds | sed \'s/ /T/g\"').read())+',duration:'+str(int(randint(1200,3600)))+',wid\":3164178}}\' -X POST https://www.toggl.com/api/v8/time_entries')
