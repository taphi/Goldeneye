#!/usr/bin/python

import Tkinter
import Image,ImageTk,tkFileDialog,sys,tkMessageBox,cv
import main
#import MySQLdb
from Tkinter import *


class mainWindow(Tkinter.Tk):
	def __init__(self,parent):
		Tkinter.Tk.__init__(self,parent)
		self.parent=parent
		self.initialize()

        def initialize(self):
                self.grid()

                self.backImage = ImageTk.PhotoImage(file="images/1.gif")
                self.background = Tkinter.Label(self,image=self.backImage,bg="black")
                self.background.grid(row=0,column=0,columnspan=2,rowspan=2)

                self.grid_columnconfigure(0,weight=1)
                #self.resizable(True,False)

                menubar=Tkinter.Menu(self)
                filemenu = Tkinter.Menu(menubar,tearoff=0)
                filemenu.add_command(label="Change Parameters",command=self.changePara)
                filemenu.add_separator()
                filemenu.add_command(label="Quit",command=self.quit)

                menubar.add_cascade(label="File",menu=filemenu)

                helpmenu = Tkinter.Menu(menubar,tearoff=0)
                helpmenu.add_command(label="About Project",command=self.aboutProj)
                menubar.add_cascade(label="Help",menu=helpmenu)

                self.config(menu=menubar)

                self.b1 = Tkinter.Button(self, text="Load Image", command=self.loadImage,bg="white")
                self.b1.grid(row=3,column=0, sticky=Tkinter.W+Tkinter.E)

                self.b2 = Tkinter.Button(self, text="Search for Record", command=self.queryDatabase,bg="white")
                self.b2.grid(row=3,column=1, sticky=Tkinter.W+Tkinter.E)


	## query DB
	def database(self):
		db = MySQLdb.connect(host='141.219.193.136', user='root', db='maindb')
		curs = db.cursor()
		return curs

	def changePara(self):
		cpara = Tkinter.Toplevel()
		cpara.title("Advanced Configuration Options")
		cpara.geometry('400x140+0+0')

		self.f = open('defaultpara.txt');
                self.lines = self.f.readlines()
                self.f.close()

		self.HD = StringVar()
		self.HD.set(self.lines[0])

		self.MFR = StringVar()
                self.MFR.set(self.lines[1])
	
		self.HTO = StringVar()
                self.HTO.set(self.lines[2])

		self.UP = StringVar()
                self.UP.set(self.lines[3])

		#### Use arrays ####
		L1 = Tkinter.Label(cpara, text="Hamming Distance:")
		L1.grid(sticky=E)
		E1 = Tkinter.Entry(cpara, bd=2)
		E1.grid(row=0, column=1)
		D1 = Tkinter.Label(cpara, textvariable=self.HD)
		D1.grid(row=0, column=3)

		L2 = Tkinter.Label(cpara, text="Median Filter Radius:")
		L2.grid(sticky=E)
		E2 = Tkinter.Entry(cpara, bd=2)
		E2.grid(row=1, column=1)
		D2 = Tkinter.Label(cpara, textvariable=self.MFR)
                D2.grid(row=1, column=3)

		L3 = Tkinter.Label(cpara, text="Hough Transform Option:")
		L3.grid(sticky=E)
		E3 = Tkinter.Entry(cpara, bd=2)
		E3.grid(row=2, column=1)
		D3 = Tkinter.Label(cpara, textvariable=self.HTO)
                D3.grid(row=2, column=3)

		L4 = Tkinter.Label(cpara, text="Unspecified Parameter:")
		L4.grid(sticky=E)
		E4 = Tkinter.Entry(cpara, bd=2)
		E4.grid(row=3, column=1)
		D4 = Tkinter.Label(cpara, textvariable=self.UP)
                D4.grid(row=3, column=3)

        	button = Tkinter.Button(cpara, text="Submit", command=self.paraSubmit,bg="white")
       		button.grid(row=6, column=1, pady=10)

	def paraSubmit(self):
               	tkMessageBox.showinfo("Iris Processing", "Test")

	def queryDatabase(self):
		query = Tkinter.Toplevel()
                query.title("Patient Information")
                query.geometry('250x180+0+0')
               
                #db = MySQLdb.connect(host='141.219.193.136', user='root', passwd='admin', db='Goldeneye')
                #curs = db.cursor()
               
                self.QL1 = Tkinter.Label(query, text="First Name:")
                self.QL1.grid(sticky=E)
                self.QE1 = Tkinter.Entry(query, bd=2)
                self.QE1.grid(row=0, column=1)
 
                self.QL2 = Tkinter.Label(query, text="Last Name:")
                self.QL2.grid(sticky=E)
                self.QE2 = Tkinter.Entry(query, bd=2)
                self.QE2.grid(row=1, column=1)
 
                self.QL3 = Tkinter.Label(query, text="SSN:")
                self.QL3.grid(sticky=E)
                self.QE3 = Tkinter.Entry(query, bd=2)
                self.QE3.grid(row=2, column=1)
 
#               self.btype = StringVar(query)
#               self.btype.set("A")
               
#               self.QL4 = Tkinter.Label(query, text="Blood type:")
#               self.QL4.grid(sticky=E)
#               self.QE4 = Tkinter.OptionMenu(query, self.btype, "A", "B", "AB", "O")
#               self.QE4.config(bg="white")
#               self.QE4.grid(row=3, column=1, sticky=W)
 
#               self.gender = StringVar(query)
#               self.gender.set("Male")        
 
#               self.QL5 = Tkinter.Label(query, text="Gender:")
#               self.QL5.grid(sticky=E)
#               self.QE5 = Tkinter.OptionMenu(query, self.gender, "Male", "Female")
#               self.QE5.config(bg="white")
#               self.QE5.grid(row=4, column=1, sticky=W)
 
                button = Tkinter.Button(query, text="Query", command=self.passFunction,bg="white")
                button.grid(row=8, column=1, pady=10)
 
	def passFunction(self):    
		func = Tkinter.Toplevel()
                func.title("Patient Record")
                func.geometry('400x400+0+0')
               
                db = MySQLdb.connect(host='141.219.193.136', user='root', passwd='admin', db='Goldeneye')
                cursor = db.cursor()
               
                self.FirstName = self.QE1.get()
                self.LastName = self.QE2.get()
                self.ssn = self.QE3.get()
 
#               cursor.execute ("""SELECT pat_face FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
#                self.FACEresults = StringVar()
#                self.FACEresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_firstname, pat_middleinitial, pat_lastname FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.NAMEresults = StringVar()
                self.NAMEresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_street, pat_city, pat_state, pat_zip FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.ADDresults = StringVar()
                self.ADDresults.set(cursor.fetchone())
       
                cursor.execute ("""SELECT pat_phone FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.PHONEresults = StringVar()
                self.PHONEresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_bloodtype FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.BLOODresults = StringVar()
                self.BLOODresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_weight FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.WEIGHTresults = StringVar()
                self.WEIGHTresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_hieght FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.HEIGHTresults = StringVar()
                self.HEIGHTresults.set(cursor.fetchone())
 
                cursor.execute ("""SELECT pat_face FROM PATIENT WHERE pat_firstname=%s AND pat_lastname=%s AND pat_id=%s""",(self.FirstName,self.LastName,self.ssn))
                self.PATFACEresults = StringVar()
                self.PATFACEresults.set(cursor.fetchone())
 
 
                db.close()
 
#               FACENAME = Tkinter.Label(func, text='Patient Information:')
#                FACENAME.grid(sticky=W)
#                FACENAME = Tkinter.Label(func, textvariable=self.FACEresults)
#                FACENAME.grid(row=0, column=1, sticky=W)
               
                PATINFO = Tkinter.Label(func, text='Patient Information:')
                PATINFO.grid(row=0, column=0, sticky=W)
 
                PATNAME = Tkinter.Label(func, text='Name: ')
                PATNAME.grid(sticky=W)
                PATNAME = Tkinter.Label(func, textvariable=self.NAMEresults)
                PATNAME.grid(row=1, column=1, sticky=W)
 
                PATADDRESS = Tkinter.Label(func, text='Address:')
                PATADDRESS.grid(sticky=W)
                PATADDRESS = Tkinter.Label(func, textvariable=self.ADDresults)
                PATADDRESS.grid(row=2, column=1, sticky=W)
 
                PATPHONE = Tkinter.Label(func, text='Phone Number: ')
                PATPHONE.grid(sticky=W)
                PATPHONE = Tkinter.Label(func, textvariable=self.PHONEresults)
                PATPHONE.grid(row=3, column=1, sticky=W)
 
                PATBLOOD = Tkinter.Label(func, text='Blood Type: ')
                PATBLOOD.grid(sticky=W)
                PATBLOOD = Tkinter.Label(func, textvariable=self.BLOODresults)
                PATBLOOD.grid(row=4, column=1, sticky=W)
 
                PATWEIGHT = Tkinter.Label(func, text='Weight: ')
                PATWEIGHT.grid(sticky=W)
                PATWEIGHT = Tkinter.Label(func, textvariable=self.WEIGHTresults)
                PATWEIGHT.grid(row=5, column=1, sticky=W)
 
                PATHEIGHT = Tkinter.Label(func, text='Height: ')
                PATHEIGHT.grid(sticky=W)
                PATHEIGHT = Tkinter.Label(func, textvariable=self.HEIGHTresults)
                PATHEIGHT.grid(row=6, column=1, sticky=W)
 
                PATFACE = Tkinter.Label(func, text='FACE: ')
                PATFACE.grid(sticky=W)
                PATFACE = Tkinter.Label(func, textvariable=self.PATFACEresults)
                PATFACE.grid(row=7, column=1)
 	
	def aboutProj(self):
		aproj = Tkinter.Toplevel()
		aproj.title("Project Goldeneye")
		aproj.geometry('275x275+0+0')

		message = "Project Members: \nMatt Masseth, Joe Vella, Ricky Barber\n\nDetails:\n- Research the iris recognition process\n\n- Find improvements in the process\n(new algorithms and techniques)\n\n- Implement those improvements in \na software environment\n\n- Convert image to Iris Code, and \nprovide a method to compare \n\n- Research possible hardware solutions"
		Tkinter.Label(aproj,text=message).pack()

	def loadImage(self):
		imgPath = tkFileDialog.askopenfilename()
		loadImage = ImageTk.PhotoImage(file=imgPath)

		self.background.destroy()
		self.b1.destroy()
		self.b2.destroy()

		self.title("Iris Processing")

		self.newimage = Tkinter.Label(self, image=loadImage)
		self.newimage.loadImage=loadImage
		self.newimage.grid(row=0,column=0,rowspan=2,columnspan=2)

		self.button = Tkinter.Button(self, text="Process Image",command=lambda i=imgPath: self.processImage(i) ,bg="white")
		self.button.grid(row=2,column=0,columnspan=2,sticky=Tkinter.S+Tkinter.N)

	def processImage(self,path):
		self.newimage.destroy()
		self.title("Iris Processed")
		self.button.destroy()

		newImageObject = main.main(path)
		newImage = newImageObject.thresholdedImage
		centerx = newImageObject.xPoint
		centery = newImageObject.yPoint
		radius = newImageObject.rPoint

		loadImage = ImageTk.PhotoImage(newImage)
		self.newimage = Tkinter.Label(self, image=loadImage)
		self.newimage.loadImage=loadImage
		self.newimage.pack()
		#self.newimage.grid(row=0,column=0,rowspan=2,columnspan=2)

		self.pupilCenter = Tkinter.Label(self, text="Center: " + str(centerx) + "," + str(centery))
		self.pupilCenter.pack()
		#pupilCenter.grid(row=2,column=0,columnspan=2)

		self.pupilRadius = Tkinter.Label(self, text="Radius: " + str(radius))
		self.pupilRadius.pack()
		#pupilCenter.grid(row=3,column=0,columnspan=2)	

		self.button = Tkinter.Button(self, text="Close",command=self.quit,bg="white")
		self.button.pack(side=RIGHT)
		#self.button.grid(row=4,column=0,columnspan=2)

		self.button2 = Tkinter.Button(self, text="Main Menu",command=self.mainmenu,bg="white")
		self.button2.pack(side=LEFT)

	def mainmenu(self):
		self.newimage.destroy()
		self.pupilCenter.destroy()
		self.pupilRadius.destroy()
		self.button.destroy()
		self.button2.destroy()
		self.initialize()
		
if __name__ == "__main__":
	root = mainWindow(None)
	root.title("Goldeneye Iris Scanner")
	root.mainloop()

