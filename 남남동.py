import tkinter
root = tkinter.Tk ()
root.title ('이것은 나침반이오!!!!!!!')
root.geometry ('450x450')

def wmi ():
    master['text'] = '나를 두고 어디를 간 것이오!!!!!!!!!!!!!!!!!!!!!!!!!!!'

def click_button () :
    Dong = tkinter.Label (root, text= '동', font=('궁서체', 20))
    SoeI = tkinter.Label (root, text= '서', font=('궁서체', 20))
    Namm = tkinter.Label (root, text= '남', font=('궁서체', 20))
    Buck = tkinter.Label (root, text= '북', font=('궁서체', 20))
    Dong.place (x= 300,y= 200)
    SoeI.place (x= 100,y= 200)
    Buck.place (x= 200,y= 100)
    Namm.place (x= 200,y= 300)

    txt = write.get ()
    str1 = txt
    labeltxt = tkinter.Label (root, text = str1, font= ('궁서체', 20))
    labeltxt.place (x=300, y= 300)


master = tkinter.Button (root, text= '관리자 나리!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', font= ('궁서체', 10), command=wmi)

master.place (x= 30,y= 400)

btn = tkinter.Button (root, text='눌러' , font = ('궁서체', 8), command=click_button)
btn.place (x= 200, y= 200, width=32, height=32)


write = tkinter.Entry (width = 15)
write.place (x=160, y= 350)

root.mainloop ()