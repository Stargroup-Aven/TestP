import tkinter

root = tkinter.Tk ()
root.title ('얼레')
root.geometry ('280x160')

def avgg():
    pyt = float (python.get())
    mob = float (mobile.get())
    exc = float (mobile.get())
    avg = ((pyt * B) + (mob * A0) + (exc * A)) / (pyt+ mob + exc)
    result = tkinter.Label (root, text='평균 학점 : '+str(avg), font=('맑은 고딕',8))
    result.place (x=130,y=120)

python = tkinter.Entry (width=4)
mobile = tkinter.Entry (width=4)
excel = tkinter.Entry (width=4)

python.place (x=150,y=40)
mobile.place (x=150,y=65)
excel.place (x=150,y=90)

python.insert (0, '3.0')
mobile.insert (0, '3.0')
excel.insert (0, '3.0')

text1 = tkinter.Label (root, text='성적',font=('맑은 고딕',8))
text2 = tkinter.Label (root, text='과목(이수학점)',font=('맑은 고딕',8))
text3 = tkinter.Label (root, text='파이썬(3)',font=('맑은 고딕',8))
text4 = tkinter.Label (root, text='모바일(2)',font=('맑은 고딕',8))
text5 = tkinter.Label (root, text='엑셀(1)',font=('맑은 고딕',8))

text1.place (x=150,y=15)
text2.place (x=50,y=15)
text3.place (x=50,y=40)
text4.place (x=50,y=65)
text5.place (x=50,y=90)

calcul = tkinter.Button (width=5, text=('계산') , font= ('맑은 고딕',8), command= avgg)
calcul.place (x=50,y=120, width=60, height=25)
A = 4.5
A0 = 4.0
B = 3.5

root.mainloop ()
