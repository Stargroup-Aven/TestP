import tkinter
import random

# 제비 결과 리스트 설정
luck = ['대길','중길', '길' ,'흉','대흉']

#좌표 함수
def mouseMove(event):
    x = event.x
    y = event.y
    labelMouse ["text"]= str(x)+','+str(y)

#제비뽑기 함수
def Roll ():
    Result ['text'] = (random.choice (luck))
    
#창 생성
root = tkinter.Tk ()
root.title ('캔버스')

#캔버스 생성! root와의 연결 + 라이브러리에 canvas의 데이터 등록!
canvas = tkinter.Canvas (root, width=800,height=600,bg="skyblue")
#갖다붙여... 0,0부터 쫙다... 
canvas.pack ()

#객채지향 - 데이터와 데이터 사이의 관계를 설정한다는 뜻. ex root가 캔버스와 연결된 위의 사례와 같이.

#파일을 가지고 온 뒤(PhotoImage), 캔버스에 이미지를 넣기(canvas.creat_image)
Bg = tkinter.PhotoImage(file='miko.png')
canvas.create_image (400,300,image=Bg)

root.bind ('<Motion>', mouseMove)
labelMouse = tkinter.Label(root, text=',', font=('맑은 고딕', 10))

#라벨, 버튼 배치+커맨드에 함수 입력
Result= tkinter.Label (root, text= '??', font=('맑은 고딕', 80))
Bing= tkinter.Button (root, text= '제비뽑기' , font= ('맑은 고딕',30), fg='skyblue', command=Roll)
Result.place (x=440,y=90)
Bing.place (x=413 , y=400 , height=80, width=180)

#좌표
root.bind ("<Motion>", mouseMove)
labelMouse = tkinter.Label (root, text=",", font= ('맑은 고딕', 10))
labelMouse.pack ()

#최종 실행
root.mainloop ()    