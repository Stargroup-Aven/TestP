import tkinter

def click_calcul():
    num1 = int (entry1.get())
    num2 = int (entry2.get())

    str1 = '' + str(num1)+ '을(를) ' + str(num2)+ '(으)로 나눈 몫은 '+str(num1//num2)+'입니다.'
    str2 = '' + str(num1)+ '을(를) ' + str(num2)+ '(으)로 나눈 나머지는 '+str(num1%num2)+'입니다.'

    label3 = tkinter.Label (chang, text=str1, font=('맑은 고딕', 10))
    label3.place (x=25, y=125)

    label3 = tkinter.Label (chang, text=str2, font=('맑은 고딕', 10))
    label3.place (x=25, y=152)



chang = tkinter.Tk ()
chang.title ('나누는 계산기에요')
chang.geometry ('400x300')

label1 = tkinter.Label (chang, text= '나눠지는 수', font= ('맑은 고딕',10))
label1.place (x=25, y=25)

label2 = tkinter.Label (chang, text= '나누는 수', font= ('맑은 고딕',10))
label2.place (x=35, y=77)

entry1 = tkinter.Entry (width=10)
entry1.place (x=130, y=25)

entry2 = tkinter.Entry (width=10)
entry2.place (x=130, y=77)

calcul = tkinter.Button (chang, text= '계산조져', font= ('Times New Roma',10), command= click_calcul)
calcul.place (x=234, y= 25, width=70, height=70)


chang.mainloop ()
