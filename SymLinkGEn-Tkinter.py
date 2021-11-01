from tkinter import *
#from tkinter import filedialog
import os

def generate_symlink():
  symName = strSymName.get()
  symTarget = strSymTarget.get()
  symLocation = strSymLocation.get()
  symGenCmd =  'mklink /D "' + symLocation + '\\' + symName + '"' + ' "' + symTarget + '"'

  print(symGenCmd)
  #print(symName, symTarget, symLocation)

  symLNameEntry.delete(0, END)
  symLTargetEntry.delete(0, END)
  symLLocationEntry.delete(0, END)

#def file_opener():
   #input = filedialog.askopenfile(initialdir="/")
   #print(input)
   #for i in input:
      #print(i)
  
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
