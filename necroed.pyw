#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Name: NecroEd
# Version: 0.87
#
# Author: Martin petersson
# Created: 2013-12-27
# Written for: Python 2.7
# Licence: none

import sys

from Tkinter import * #import tkFont
from tkColorChooser import askcolor
from tkFileDialog import askopenfilename, asksaveasfilename
import tkMessageBox

import colortheme
#import keybindings
#import editorgui

filepath = ""
savepath = ""
filepath_update = "" #StringVar()
settings_loaded = 0

root = Tk()
menu_frame = Frame(master=root, bg=colortheme.color_frame)
text_frame = Frame(master=root)
textfield = Text(master=text_frame, width=62, height=20, wrap=NONE, insertbackground=colortheme.color_text, font=colortheme.font_text, borderwidth=0.0, fg=colortheme.color_text, bg=colortheme.color_background)
menu_framelower = Frame(master=root, bg=colortheme.color_frame)
menu_framelowerleft = Frame(master=menu_framelower, bg=colortheme.color_frame)
filepath_display = Label(master=menu_framelowerleft, font=colortheme.font_menu, textvariable=filepath_update, fg=colortheme.color_frame_text, bg=colortheme.color_frame)
textfield.focus_set()
root.configure(background=colortheme.color_frame)

def e_exit(event):
	#root.exit()
	sys.exit()
	#print("Now exiting NecroEd")

def e_new_files(event):
	f_new_files()

def f_new_files():
	global textfield
	textfield.delete(1.0, "end")

def e_open_files(event):
	f_open_files()

def f_open_files():
	global textfield
	global filepath
	global filepath_display
	filepath = askopenfilename(filetypes=[("All files", "*"), ("Text files", "*.txt"), ("Python files", "*.py")])
	Openfile = open(filepath)
	textfield.delete(1.0, "end")
	textfield.insert(0.0, Openfile.read())
	#filepath_display(filepath)
	Openfile.close()
	textfield.focus_set()

def e_save_files(event):
	f_save_files()

def f_save_files():
	global textfield
	global filepath
	global settings_loaded
	Savefile = open(filepath, "w")
	Savefile.write(textfield.get(1.0, "end"))

	#if settings_loaded == 1:
	#	Savefile = open(colortheme.py, "w")
	#	Savefile.write(textfield.get(1.0, "end"))
	#if settings_loaded == 0:
	#	Savefile = open(filepath, "w")
	#	Savefile.write(textfield.get(1.0, "end"))

def e_save_files_as(event):
	f_save_files_as()

def f_save_files_as():
	global textfield
	global savepath
	savepath = asksaveasfilename(filetypes=[("All files", "*"), ("Text files", "*.txt"), ("Python files", "*.py")])
	Savefile = open(savepath, "w")
	Savefile.write(textfield.get(1.0, "end"))

def e_find_text(event):
	f_find_text()

def f_find_text():
	global textfield
	global Openfile
	global filepath
	filepath.find('Nekrosus')
	print("Found it!")

def e_run_files(event):
	f_run_files()

def f_run_files():
	global filepath
	execfile(filepath)

def e_color_picker(event):
	f_color_picker()

def f_color_picker():
	current_color = askcolor()
	textfield.insert(INSERT, current_color[1])

def e_color_theme(event):
	f_color_theme()

def f_color_theme():
	global textfield
	global filepath
	Openfile = open("colortheme.py", "r")
	textfield.delete(1.0, "end")
	textfield.insert(0.0, Openfile.read())
	settings_loaded = 1

def e_show_keybindings(event):
	f_show_keybindings()

def f_show_keybindings():
	global textfield
	global filepath
	Openfile = open("keybindings.py", "r")
	textfield.delete(1.0, "end")
	textfield.insert(0.0, Openfile.read())

def e_show_help(event):
	f_show_help()

def f_show_help():
	global textfield
	global filepath
	Openfile = open("help.txt", "r")
	textfield.delete(1.0, "end")
	textfield.insert(0.0, Openfile.read())

def f_about_message():
	tkMessageBox.showinfo("NecroEd Version 0.86", "(C)2013-2014 Martin Petersson")

class editor_gui():

	def __init__(self):

		root.title("NecroEd")
		try:
			root.wm_iconbitmap("Data/necroed.ico")
		except:
			pass
		
		menu_frame.pack(side=TOP, fill=X)

		b_new_file = Button(master=menu_frame, font=colortheme.font_menu, text="New", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_new_files)
		b_new_file.pack(side=LEFT) 
		
		b_open_file = Button(master=menu_frame,  font=colortheme.font_menu, text="Open", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_open_files)
		b_open_file.pack(side=LEFT)
		
		b_save_file = Button(master=menu_frame, font=colortheme.font_menu, text="Save", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_save_files)
		b_save_file.pack(side=LEFT)

		b_save_file_as = Button(master=menu_frame,  font=colortheme.font_menu, text="Save as", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_save_files_as)
		b_save_file_as.pack(side=LEFT)

		b_find = Button(master=menu_frame, font=colortheme.font_menu, text="Find", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_find_text)
		b_find.pack(side=LEFT)
		
		b_run = Button(master=menu_frame, font=colortheme.font_menu, text="Run", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_run_files)
		b_run.pack(side=LEFT)

		b_colorpicker = Button(master=menu_frame, font=colortheme.font_menu, text="Color", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_color_picker)
		b_colorpicker.pack(side=LEFT)
		
		#b_exit = Button(master=menu_frame, font=colortheme.font_menu, text="Exit", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=exit)
		#b_exit.pack(side=RIGHT)

		b_help = Button(master=menu_frame, font=colortheme.font_menu, text="Help", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_show_help)
		b_help.pack(side=RIGHT)
		
		b_about = Button(master=menu_frame, font=colortheme.font_menu, text="About", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_about_message)
		b_about.pack(side=RIGHT)

		b_colortheme = Button(master=menu_frame, font=colortheme.font_menu, text="Theme", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_color_theme)
		b_colortheme.pack(side=RIGHT)
		
		b_keybindings = Button(master=menu_frame, font=colortheme.font_menu, text="Keybindings", borderwidth=0.5, fg=colortheme.color_button_fg, bg=colortheme.color_button_bg, command=f_show_keybindings)
		b_keybindings.pack(side=RIGHT)
		
		text_frame.pack(side=TOP, fill=BOTH, expand=YES)
		textfield.pack(side=TOP, fill=BOTH, expand=YES)
		menu_framelower.pack(side=BOTTOM, fill=BOTH)
		menu_framelowerleft.pack(side=LEFT)
		filepath_display.pack(side=LEFT)

		root.bind("<F1>", f_show_help)
		# root.bind("<F2>", e_hide_menu)
		root.bind("<F3>", e_color_picker)
		root.bind("<F4>", f_show_keybindings)
		root.bind("<F5>",e_color_theme)		
		#root.bind("<F9>", run_files)
		
		root.bind("<Control_L><n>", e_new_files)
		root.bind("<Control_L><o>", e_open_files)
		root.bind("<Control_L><s>", e_save_files)
		root.bind("<Control_L><p>", e_save_files_as)
		root.bind("<Control_L><d>", e_find_text)
		root.bind("<Control_L><q>", e_exit)

		root.mainloop()

editor_gui()
open_files()
f_save_files()


