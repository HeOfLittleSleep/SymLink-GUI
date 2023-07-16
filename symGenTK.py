from tkinter import *
#from tkinter import filedialog
import os
#import win32com.shell.shell as shell
import ctypes, sys

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

  os.system(symGenCmd)
  #shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c '+symGenCmd)

#def file_opener():
   #input = filedialog.askopenfile(initialdir="/")
   #print(input)
   #for i in input:
      #print(i)
  
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if is_admin():
    mainWindow = Tk()
    mainWindow.geometry("250x350")
    mainWindow.title("SymLink Generator")
 
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

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

