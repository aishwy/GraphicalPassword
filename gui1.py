from Tkinter import *
from databse import insert


def raise_fr(fr):
    print 'raising'+str(fr)
    fr.tkraise()

top = Tk()
top.geometry("175x300")
fr_main = Frame(top)
frReg = Frame(top)
frSign = Frame(top)

for frame in (fr_main, frReg, frSign):
    frame.grid(row=0, column=0, sticky='news')

# MAIN WINDOW
buttReg = Button(fr_main, text="Register", command=lambda: raise_fr(frReg)).pack()
buttSign = Button(fr_main, text="Sign in", command=lambda: raise_fr(frSign)).pack()

# REGISTER WINDOW
labName = Label(frReg, text="User Name").pack()
entName = Entry(frReg)
entName.pack()

labEmail = Label(frReg, text="Email ID").pack()
entEmail = Entry(frReg)
entEmail.pack()

labPass = Label(frReg, text="Password").pack()
entPass = Entry(frReg)
entPass.pack()

labCol = Label(frReg, bg="white")
mbCol = Menubutton(frReg, text="Color", relief=RAISED)
mbCol.menu = Menu(mbCol, tearoff=0)
mbCol["menu"] = mbCol.menu

Color=None
def opt(item):
    Color=item
    labCol.configure(bg=item)

mbCol.menu.add_command(label="Blue", command=lambda: opt("Blue"))
mbCol.menu.add_command(label="Red", command=lambda: opt("Red"))
mbCol.pack()
labCol.pack()


def submit():
    insert(entName.get(), entEmail.get(), entPass.get(), Color)

buttSub1 = Button(frReg, text="SUBMIT", command=submit).pack()
butt_main1 = Button(frReg, text="BACK", command=lambda: raise_fr(fr_main)).pack()

# SIGN IN WINDOW
buttSub2 = Button(frSign, text="SUBMIT").pack()
butt_main2 = Button(frSign, text="BACK", command=lambda: raise_fr(fr_main)).pack()

raise_fr(fr_main)
top.mainloop()
