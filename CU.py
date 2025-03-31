import tkinter

root= tkinter.Tk ()
root.title ('CU투모로우')
root.geometry ('850x350')

#계산식이...
def Calcul () :
    M1_s = int(M1_sell.get())
    M2_s = int(M2_sell.get())
    M3_s = int(M3_sell.get())
    M4_s = int(M4_sell.get())
    M5_s = int(M5_sell.get())
    M6_s = int(M6_sell.get())
    M1_b = int(M1_buy.get())
    M2_b = int(M2_buy.get())
    M3_b = int(M3_buy.get())
    M4_b = int(M4_buy.get())
    M5_b = int(M5_buy.get())
    M6_b = int(M6_buy.get())
    
    total = 0
    total += 1800* int(M1_s)
    total += 1400* int(M2_s)
    total += 1800* int(M3_s)
    total += 4000* int(M4_s)
    total += 1500* int(M5_s)
    total += 2000* int(M6_s)
    total -= 500* int(M1_b)
    total -= 900* int(M2_b)
    total -= 800* int(M3_b)
    total -= 3500* int(M4_b)
    total -= 700* int(M5_b)
    total -= 1000* int(M6_b)
    Str_total = "오늘 총 매출액은 "+str(total)+"원입니다."
    P_total = tkinter.Label (root, text=Str_total, font= ('맑은고딕', 10))
    P_total.place (x=50, y=300)

#Basic Setting
menu1 = tkinter.Label (root, text='캔커피', font = ('맑은고딕',10))
menu2 = tkinter.Label (root, text='삼각김밥', font = ('맑은고딕',10))
menu3 = tkinter.Label (root, text='바나나 우유', font = ('맑은고딕',10))
menu4 = tkinter.Label (root, text='도시락', font = ('맑은고딕',10))
menu5 = tkinter.Label (root, text='콜라', font = ('맑은고딕',10))
menu6 = tkinter.Label (root, text='새우깡', font = ('맑은고딕',10))

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

#entry Setting

M1_sell = tkinter.Entry (width=5)
M2_sell = tkinter.Entry (width=5)
M3_sell = tkinter.Entry (width=5)
M4_sell = tkinter.Entry (width=5)
M5_sell = tkinter.Entry (width=5)
M6_sell = tkinter.Entry (width=5)
M1_buy = tkinter.Entry (width=5)
M2_buy = tkinter.Entry (width=5)
M3_buy = tkinter.Entry (width=5)
M4_buy = tkinter.Entry (width=5)
M5_buy = tkinter.Entry (width=5)
M6_buy = tkinter.Entry (width=5)

M1_sell.place (x=110,y=110)
M2_sell.place (x=230,y=110)
M3_sell.place (x=350,y=110)
M4_sell.place (x=470,y=110)
M5_sell.place (x=590,y=110)
M6_sell.place (x=710,y=110)

M1_buy.place (x=110,y=180)
M2_buy.place (x=230,y=180)
M3_buy.place (x=350,y=180)
M4_buy.place (x=470,y=180)
M5_buy.place (x=590,y=180)
M6_buy.place (x=710,y=180)

#계산
Calcul = tkinter.Button (root, text='계산', font= ('맑은고딕',10), command=Calcul)
Calcul.place (x=50, y= 250, width=750, height=30)


root.mainloop ()

