from tkinter import *
#import tkFileDialog
import os

def generate_symlink():
  symName = strSymName.get()
  symTarget = strSymTarget.get()
  symLocation = strSymLocation.get()
  print(symName, symTarget, symLocation)

  #file = open("user.txt", "w")
  #file.write(firstname_info)
  #file.write(lastname_info)
  #file.write(age_info)
  #file.close()
  #print(" User ", firstname_info, " has been registered successfully")

  #firstname_entry.delete(0, END)
  #lastname_entry.delete(0, END)
  #age_entry.delete(0, END)
  
mainwindow = Tk()
mainwindow.geometry("250x350")
mainwindow.title("SymLink Generator")
#heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3")
#heading.pack()
 
symLNameLabel = Label(text = "Symlink Name",)
symLTargetLabel = Label(text = "SymLink Target",)
symLLocationLabel = Label(text = "Symlink Location",)
symLNameLabel.place(x = 15, y = 70)
symLTargetLabel.place(x = 15, y = 140)
symLLocationLabel.place(x = 15, y = 210)


strSymName = StringVar()
strSymTarget = StringVar()
strSymLocation = StringVar()

symLNameEntry = Entry(textvariable = strSymName, width = "30")
symLTargetEntry = Entry(textvariable = strSymTarget, width = "30")
symLLocationEntry = Entry(textvariable = strSymLocation, width = "30")

symLNameEntry.place(x = 15, y = 100)
symLTargetEntry.place(x = 15, y = 180)
symLLocationEntry.place(x = 15, y = 240)

genSym = Button(mainwindow,text = "Generate SymLink", width = "30", height = "2", command = generate_symlink, bg = "grey")
genSym.place(x = 15, y = 290)

mainwindow.mainloop()
