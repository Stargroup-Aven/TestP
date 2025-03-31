import tkinter

root = tkinter.Tk ()
root.title ('캔버스')
canvas = tkinter.Canvas (root, width=800,height=600,bg="magenta")
#갖다붙여... 0,0부터 쫙다...
canvas.pack ()


bgimg = tkinter.PhotoImage(file='miko.png')
canvas.create_image(402,300,image=bgimg)

root.mainloop ()