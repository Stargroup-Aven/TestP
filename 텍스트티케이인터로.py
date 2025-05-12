import tkinter

root = tkinter.Tk ()

file = open("tst.txt",'r',encoding="UTF-8")


strFile = file.readline()
root.geometry (strFile[:-1])

strFile = file.readline()
root.title (strFile[:-1])


root.mainloop ()

file.close
