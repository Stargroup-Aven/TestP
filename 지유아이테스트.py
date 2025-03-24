import tkinter

#버튼 클릭 판정
def click_btn () :
    button['text'] = '함부르크 햄부기'

#사용자 입력값 받기
def Click_b () :
    txt = entry.get ()
    str1 = txt
    labeltxt = tkinter.Label (root, text = str1, font= ('궁서체', 20))
    labeltxt.place (x=200, y= 350)

# 윈도우 생성
root = tkinter.Tk ()
root.title ('누를티비?')
root.geometry ('500x500')   
#텍스트 배치
label = tkinter.Label (root, text='햄부기햄북어', font=('궁서체',24))
label.place (x=150, y=130)

button = tkinter.Button (root, text='햄부가티온앤 온', font=('궁서체', 24), command=click_btn)
button.place (x=120, y=200)

cha = tkinter.Label (root, text='을 차려오라고 하지 않았느냐', font=('궁서체',24))
cha.place (x=50, y=300)

entry = tkinter.Entry (width=20)
entry.place (x=20, y=20)

bet = tkinter.Button (text='문자열내놔', font=('궁서체', 24), command=Click_b)
bet.place (x= 150, y= 400)


root.mainloop ()