from tkinter import *

def raise_fr(fr):
	fr.tkraise()

top = Tk()
top.geometry("175x200")
frmain=Frame(top)
frReg = Frame(top)
frSign = Frame(top)

for frame in (frmain,frReg,frSign):
    frame.grid(row=0, column=0, sticky='news')

#MAIN WINDOW
buttReg = Button(frmain,text="Register",command=lambda:raise_fr(frReg)).pack()
buttSign = Button(frmain,text="Sign in",command=lambda:raise_fr(frSign)).pack()

#REGISTER WINDOW
labName = Label(frReg,text="User Name").pack()
entName = Entry(frReg).pack()

labEmail = Label(frReg,text="Email ID").pack()
entEmail = Entry(frReg).pack()

labPass = Label(frReg,text="Password").pack()
entPass = Entry(frReg).pack()

mbCol =  Menubutton (frReg, text="Color", relief=RAISED )
mbCol.menu  =  Menu (mbCol,tearoff = 0 )
mbCol["menu"]  =  mbCol.menu
varBlue  = IntVar()
varRed = IntVar()
mbCol.menu.add_checkbutton (label="Blue",variable=varBlue )
mbCol.menu.add_checkbutton (label="Red",variable=varRed )
mbCol.pack()
labCol = Label(frReg,bg="white")

buttSub1 = Button(frReg,text="SUBMIT").pack()
buttmain1 = Button(frReg,text="BACK",command=lambda:raise_fr(frmain)).pack()

#SIGN IN WINDOW
buttSub2 = Button(frSign,text="SUBMIT").pack()
buttmain2 = Button(frSign,text="BACK",command=lambda:raise_fr(frmain)).pack()

raise_fr(frmain)
top.mainloop()