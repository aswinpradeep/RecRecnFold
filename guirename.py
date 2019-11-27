#!/usr/bin/env python

from Tkinter import *
import tkFileDialog
import os
import sys
from os import listdir
from os.path import isfile, join
import glob
import Tkinter
import tkMessageBox
import ttk

master = Tk()
x=""
imagesx=[]
master.title("Content Based Automated Group Image Renamer")
l = Label(master, text="CONTENT BASED IMAGE RENAMER",justify='center')
master.geometry('400x200')



def callback():
    global x,imagesx
    path = tkFileDialog.askdirectory()
    e.delete(0, END)  # Remove current text in entry
    e.insert(0, path)  # Insert the 'path'
    #print(path)
    x=""+path
    # print path
    imagesx = glob.glob(x+'/*.jpg') or glob.glob(x+'/*.jpeg') or glob.glob(x+'/*.png') 
    if(imagesx):
    	b["state"]="normal"
    else:
        tkMessageBox.showinfo("Warning", "Please select a folder which contains images")
	b["state"]="disabled"
def runn():
    global x
    result = tkMessageBox.askquestion("Rename", "Are You Sure?", icon='warning')
    if result == 'yes':
	    os.system('cp ./* '+x+'/')
	    os.system('cd '+x+'/ && python renamer.py ./')
	    print("renaming done")
	    os.chdir(x+'/')
	    b["state"]="disabled"
            #os.mkdir('unclassifyable')
	    msgx=tkMessageBox.askquestion('SUb folderization',str(len(imagesx))+" images successfully processed Do you wish to do a sub folderization",icon = 'warning')
	    if msgx == 'yes':
		    with open('retrained_labels.txt','a') as yy:
			yy.write('unclassifyable')
		    with open('retrained_labels.txt') as xx:
			    for line in xx:
				line = line.strip()
				os.system('rm -r '+ line)
				os.mkdir(str(line))
				#os.mkdir('unclassifyable')
				for name in glob.glob('./'+line+'*'):
				    os.system('mv '+name[2:]+' ./'+line+'/')
				os.system('find . -empty -type d -delete')
				os.system('/bin/bash exec.sh')
		    os.system('rm *')
		    tkMessageBox.showinfo("Done", "Sub folderization successfull")
def doSomething():
    result = tkMessageBox.askquestion("Quit", "Are You Sure?", icon='warning')
    if result == 'yes':
	master.destroy()
    
w = Label(master, text="File Path:")
e = Entry(master, text="")
bb = Button(master, text="Browse", command=callback)
b = Button(master, text="Rename", command=runn ,state="disabled")
b.place(x=100,y=100)
#b1["state"] = "disabled"
l.pack(side=TOP)
w.pack(side=LEFT)
e.pack(side=LEFT)
bb.pack(side=LEFT)
b.pack(side=LEFT)



master.protocol('WM_DELETE_WINDOW', doSomething)  # root is your root window
master.mainloop()
