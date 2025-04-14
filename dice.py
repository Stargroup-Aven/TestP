import random
count = 0

dice1 = 0
dice2 = 0
dice3 = 0

while True :
    count += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice3 = random.randint(1,6)
    print ('데구르르...')
    print('...')
    print (dice1,dice2,dice3, '!\n')
    if (dice1 == dice2) and (dice2 == dice3) :
        break

print("3개 주사위는 모두", dice1, "!!")
print("같은 숫자가 나오기까지", count, "번 던졌습니다!")
if count < 5 :
    print ('운이 좋으시네요~~~ 복권 함 긁어보심이??')
elif count < 10 :
    print ('이야, 운이 좋으시네요~') 
elif count < 20 :
    print ('아, 진짜 준수하신데요?')
elif count < 30 :
    print ('뭐, 나쁘진 않죠~')
elif count < 40 :
    print ('적당하네요, 평균보단 낮지만?')
elif count < 50 :
    print ('그럭저럭...')
elif count < 60 :
    print ('...음')
else :
    print ('습, 혹시 오늘 아침에 새똥이라도 맞으셨나요??')