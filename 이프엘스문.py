num = int(input("숫자 ==> "))

if num % 2 == 0:
    print('짝수요')
else:
    print('홀수요')



num2 = int (input('숫자 입력 ->'))

if num2 < 100 :
    print ('100보다 작고요')
elif num2 < 1000:
    print ('100보단 큰데 1000보단 작고요')
else :
    print('이야 이건 1000보다 큰데요')

if num2 < 1000:
    if num2 < 100 :
        print('백보다 작앙')
    else:
        print ('백보단 큰데 천보단 작아잉')
else:
    print ('천보다 좀 큰...?')



grade = int(input('당신의 성적은? : '))

if grade>=90 :
    print ('A', end= '')
elif grade>=80 :
    print('B', end= '')
elif grade>=70 :
    print('C', end= '')
elif grade>=60 :
    print('D', end= '')
else:
    print('F',end= '')
print ('학점입니당')