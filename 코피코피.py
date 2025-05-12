#읽기 파이릉르 읽어와서 쓰기파일에 작성, 복사하는 개념

Rfile = open('readpy.txt','r', encoding='UTF-8')
Wfile = open('writepy.txt','w', encoding='UTF-8')

while True:
    Rstr = Rfile.readline ()
    print (Rstr, end ="")
    if (Rstr == ''):
            print ('\n끝!')
            break
    Wfile.writelines (Rstr)


Rfile.close ()
Wfile.close ()