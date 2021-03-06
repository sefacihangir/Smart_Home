#!/usr/bin/env python
#Davy Ragland | dragland@stanford.edu
#Home Automation System version 2.0 | 2016

#*********************************************************************
#                           SETUP
#*********************************************************************
import os
import cgi
import sqlite3
import datetime
import subprocess
import cleverbot

#*********************************************************************
#                          FUNCTIONS
#*********************************************************************
#Function: header
#This function returns the apropriate header.
def header(TYPE):
	if TYPE == "BLANK":
		print "Status: 204 No Content"
		print "Content-type: text/plain"
	if TYPE == "HTML":
		print "Content-Type: text/html"
	print ""

#Function: queryData
#This function querries the SQL data base with the appropriate
#HTTP GET parmeters.
def queryData(DATABASE, RANGE, VALUE):
	conn = sqlite3.connect(DATABASE)
	curs = conn.cursor()
	curs.execute("SELECT * FROM data WHERE timestamp >= datetime('%s','-%i %s')" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), int(VALUE), RANGE))
	rows = curs.fetchall()
	conn.close()
	return rows

#Function: formatData
#This function formats the querried data so that the graph can display it.
def formatData(ROWS):
	for row in ROWS:
		print str(row)[3:-1].replace("'","")

#Function: queryBot
#This function queries the cleverbot API for a responce to a string.
def queryBot(QUERY):
	cb = cleverbot.Cleverbot()
	print(cb.ask(QUERY))
#*********************************************************************
#                          HELPERS
#*********************************************************************
#Function: get_value
#This function gets the value from an HTTP GET call.
def get_value(KEY):
	form = cgi.FieldStorage()
	return form[KEY].value

#Function: set_mode
#This function sets the mode of a relay.
def set_mode(PIN_NUMBER):
	os.system("gpio mode %i out" % PIN_NUMBER)

#Function: read_state
#This function reads the state of a relay.
def read_state(PIN_NUMBER):
	output = subprocess.check_output(["gpio read %i" % (PIN_NUMBER)], shell=True)
	return str(output)[:1]

#Function: relay_on
#This function turns on a relay.
def relay_on(PIN_NUMBER):
	os.system("gpio write %i 0" % (PIN_NUMBER))

#Function: relay_off
#This function turns off a relay.
def relay_off(PIN_NUMBER):
	os.system("gpio write %i 1" % (PIN_NUMBER))