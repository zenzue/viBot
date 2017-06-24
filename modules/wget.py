#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

""" File downloader module for viBot Project """

__author__ = "blackvkng"

import urllib

usage = "[?] Wget module usage: wget FILEURL FILE NAME TO SAVE"

def run(url, fileName):
	try:
		urllib.urlretrieve(url, fileName)
		result = True
	except Exception as err:
		result = err.strerror

	return result
