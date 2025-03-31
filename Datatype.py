var1 = '''
나는 
파이썬을
열공 중입니다.'''
print (var1)

var2 = '나는\n파이썬을\n열공 중입니다.'
print (var2)

var3 = '나는\n\"파이썬을\"\n열공 중입니다.'
print (var3)

var2 = '나는\t파이썬을\t열공 중입니다.'
print (var2)

#글자 길이 차이 비교

#문자열 받기
Bar1 = input('첫 번째 문자열 ==>')
Bar2 = input('두 번째 문자열 ==>')

#문자열 길이를 숫자로.\/ 변수 = len(문자열 변수명)
len1 = len(Bar1)
len2 = len(Bar2)

#문자열 1 길이 - 문자열2 길이=diff -> 출력
diff = len1 - len2
print ('두 문자열의 길이 차이는', diff, '입니다.' )

#only 영문. 대문자 / 소문자 변환.
# upper() / lower()

SS = 'Pen Pineapple Apple Pen'
PPAP1 = SS.upper ()
print (PPAP1)
PPAP2 = SS.lower ()
print (PPAP2)

#변수명.isupper() = 문자열이 모두 대문자일 시 Ture
#변수명.islower() = 문자열이 모두 소문자일 시 Ture

sss= 'PPAP'
print (sss.isupper())
print (sss.islower())

#변수명.count('') = 문자열 내에서 어떠한 글자가 몇 번 등장하였는지 확인.

toll = '전부 잃거나... 아니면 전부 얻거나! 친구, 게임은 시작됐어. 나와 거래하자. 넌 거절할 수 없어. 이유는 없고... 선택의 여지도 없지.'
print (toll.count('.'))

#변수명.fint ('', A) = 어떠한 글자가 문자열의 몇 번째 위치에 있는지 찾는. A번째 부터 시작. A를 입력하지 않을 경우 0번부터 시작

print (toll.find ('거래'))
print (toll.find ('전부'))
print (toll.find ('전부', 6))

#문자열 내의 값 출력하기. print (변수명[인덱스 위치])
print(toll[22]+toll[23]+toll[20])

#문자열 거꾸로 출력하기. (기억할 것은 end ='')
tako = input('원본 문자열 ==>')
takolen = len (tako)
print ('반대문자열 ==>', end='')

print (tako[3], end= '')
print (tako[2], end= '')
print (tako[1], end= '')
print (tako[0], end= '')