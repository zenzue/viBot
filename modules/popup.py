#!/usr/bin/env python2
#-*- coding: utf-8 -*-
#
#

""" Popup message module for viBot Project """

__author__ = "blackvkng"

import os
import Tkinter as tk
import tkMessageBox as messagebox

def run(message):
	root = tk.Tk()
	root.withdraw()
	messagebox.showinfo(message, message)
	root.destroy()
