#파일쓰기!
Wfile = open('Openthis!.txt','w', encoding='UTF-8')
Wstr = ""

Wstr ='아 뿨스'
Wfile.writelines (Wstr+'\n')
Wstr ='아 택씌'
Wfile.writelines (Wstr+'\n')
Wstr ='Aㅏ 오뢘즤'
Wfile.writelines (Wstr+'\n')
Wstr =input("\n다음은 직접 써보시지 ==>")
Wfile.writelines (Wstr+'\n')

while True :
    Wstr =input("그 아래도 써보렴==>")
    if Wstr == "끝":
        print ('아 ㅇㅋ')
        break
    Wfile.writelines (Wstr+'\n')
    

Wfile.close()