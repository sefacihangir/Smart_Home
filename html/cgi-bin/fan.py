#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#Import Libraries
import time
import subprocess
import os

#Function to return if state is true
def read_state(pin):
	output = subprocess.check_output(["gpio read %i" % (pin)], shell=True)
	return str(output)[:1]

#Functions to swich relay state
def relay_on(pin):
	os.system("gpio write %i 0" % (pin))
def relay_off(pin):
	os.system("gpio write %i 1" % (pin))

#Function to return blank HTML packet
def header():
	print "Status: 204 No Content"
	print "Content-type: text/plain"
	print ""

#Actual program
os.system("gpio mode 16 out")
if read_state(int(16)) == "1":
	relay_on(int(16))
else:
	relay_off(int(16))
header()