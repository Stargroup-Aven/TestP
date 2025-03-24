import tkinter

root= tkinter.Tk ()
root.title ('CU투모로우')
root.geometry ('850x350')

#calcul...
total = 0
total -= 900*10
total += 1800*2
total += 4000*4
total += 1500
total += 2000*4
total += 1800*5
print("오늘 총 매출액은 ", total, "원입니다")

#Basic Setting
menu1 = tkinter.Label (root, text='메뉴1', font = ('맑은고딕',10))
menu2 = tkinter.Label (root, text='메뉴2', font = ('맑은고딕',10))
menu3 = tkinter.Label (root, text='메뉴3', font = ('맑은고딕',10))
menu4 = tkinter.Label (root, text='메뉴4', font = ('맑은고딕',10))
menu5 = tkinter.Label (root, text='메뉴5', font = ('맑은고딕',10))
menu6 = tkinter.Label (root, text='메뉴6', font = ('맑은고딕',10))

menu1.place (x=110 ,y=60)
menu2.place (x=230 ,y=60)
menu3.place (x=350 ,y=60)
menu4.place (x=470 ,y=60)
menu5.place (x=590 ,y=60)
menu6.place (x=710 ,y=60)

Sell = tkinter.Label (root, text = '판매 수량', font = ('맑은고딕',10))
Buy = tkinter.Label (root, text = '구매 수량', font = ('맑은고딕',10))

Sell.place (x=10 ,y=110)
Buy.place (x=10 ,y=180)

Calcul = tkinter.Button (root, text='계산해볼까요~~~', font= ('맑은고딕',10))
Calcul.place (x=50, y= 250, width=750, height=30)

#entrySetting

M1_sell = tkinter.Entry (width=5)
M1_sell = tkinter.Entry (width=5)
M1_sell = tkinter.Entry (width=5)
M1_sell = tkinter.Entry (width=5)
M1_sell = tkinter.Entry (width=5)
M1_sell = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)


root.mainloop ()

