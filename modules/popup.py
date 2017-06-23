#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

""" Popup message module for viBot Project """

__author__ = "blackvkng"

import Tkinter as tk
import tkMessageBox as messagebox

usage = "[?] Popup module usage: popup TEXT"

def run(message):
	root = tk.Tk()
	root.withdraw()
	messagebox.showinfo(message, message)
	root.destroy()
