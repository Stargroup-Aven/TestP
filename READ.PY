

#파일 open 변수명 설정 / encoding ="UTF-8" 을 입력하여 한국어 인식할 수 있도록 설정
file = open('READ_THIS_TEXT!.txt','r', encoding='UTF-8')
#읽을 문자열을 위한 변수 선언
inStr = ''

#문자열 읽기, readline() / 한 줄씩 읽는 명령어. 
'''
inStr = file.readline()
print (inStr, end='')
'''
#무한반복으로 활용
'''
while True : 
    inStr = file.readline()
    print (inStr, end = "")
    if (inStr == ''):
        print ('\n끝!')
        break
'''

#파일 내 문자를 리스트로 한꺼번에 저장. 변수명.readlines ()
filelist = []
index = 0

filelist = file.readlines ()
print(filelist)
for range in filelist :
    print (index, ":",filelist[index],end ='')
    index = index + 1

#변수명.close 로 닫기
file.close()


