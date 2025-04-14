for i in range(0,10,2):
    print ('아아악',i)

for i in range (51, 101, 3):
    print (i," ",  end='')

print ()

#팩토리얼계산기 1~n 사이의 곱 계산
N=5
res = 1
for i in range (1,N+1,1):
    res = res * i
print (res)


# 1000~2000 사이 홀수의 합.

result = 0

for i in range (1001, 2001, 2):
    result = result + i
    print (i)
print (result)    


#중첩 for문 -> i가 1번 실행될 때, K는 두 번 실행됨.
for i in range (0,3,1):
    for k in range(0,2,1):
        #print ("i:", i , ' k:', k)
        pass

#실습 2번

for num1 in range (2,10,1): #단
    print ('\n구구단 ',num1,'단')
    for num2 in range (1,10,1): # 곱해지는 수
        print (num1, "x",num2 ,'=\t', num1*num2, )

i=0
while (i < 5):
    print(i)
    i=i+1

res = 0
for i in range (1, 101, 1):
    if i % 4 == 0:
        continue
    elif i % 3 == 0:
        continue
    res = res + i 

print (res)