Secrettxt = open ('낄낄낄 어디 한번 읽어보시지!.txt', 'w', encoding="UTF-8")

while True :
    inStr = input('(속닥속닥)··· ')
    if inStr == "" :
        break

for ch in inStr :
    num = ord(ch)
    num = num + 100
    Chtxt = chr(num)
    secure += Chtxt


Secrettxt.writelines(secure)
Secrettxt.close()
print('--- secure.txt 암호화 완료 ---')