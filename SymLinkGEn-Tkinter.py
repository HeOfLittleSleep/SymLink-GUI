from tkinter import *
#from tkinter import filedialog
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
  
mainWindow = Tk()
mainWindow.geometry("250x350")
mainWindow.title("SymLink Generator")
#heading = Label(text = "Python Form", bg = "grey", fg = "black", width = "500", height = "3")
#heading.pack()
 
symLNameLabel = Label(text = "Symlink Name",)
symLTargetLabel = Label(text = "SymLink Target",)
symLLocationLabel = Label(text = "Symlink Location",)
symLNameLabel.place(x = 15, y = 10)
symLTargetLabel.place(x = 15, y = 55)
symLLocationLabel.place(x = 15, y = 100)


strSymName = StringVar()
strSymTarget = StringVar()
strSymLocation = StringVar()

symLNameEntry = Entry(textvariable = strSymName, width = "30")
symLTargetEntry = Entry(textvariable = strSymTarget, width = "30")
symLLocationEntry = Entry(textvariable = strSymLocation, width = "30")

symLNameEntry.place(x = 15, y = 30)
symLTargetEntry.place(x = 15, y = 75)
symLLocationEntry.place(x = 15, y = 120)

genSym = Button(mainWindow,text = "Generate SymLink", width = "30", height = "2", command = generate_symlink, bg = "grey")
genSym.place(x = 15, y = 290)

#browseTarget = Button(mainWindow, text ='...', command = lambda:file_opener())
#browseTarget.place()

mainWindow.mainloop()
