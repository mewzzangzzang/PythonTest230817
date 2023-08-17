#파이썬 모듈 기반 형식(라이브러리 = 도구 모음집)

import turtle
import random

## 함수 선언 부분 ##
#들여쓰기. 파이썬 . 의무.

def  screenLeftClick(x, y):
    # global 전역, static 비슷.
    global r, g, b
    # turtle 인스턴스 초기화는 아래에서 진행 했을 것
    #pencolor, 매개변수 rgb값을 받아서, 선색
    turtle.pencolor((r, g, b))
    #pendown, 선을 그리겠다

    r = random.random()
    g = random.random()
    b = random.random()

    # 크기변경하기
    tSize = random.randrange(1, 10)
    # 거북이 모양크기
    turtle.shapesize(tSize)

    #거북이 회전
    turtle.left(30)

    #거북이 도장찍기
    turtle.stamp()
    
    turtle.pendown()
    # goto  매개변수 좌표값으로 이동.
    turtle.goto(x, y)

    turtle.color(r,g,b)

#우클릭시, 가능.
def  screenRightClick(x, y):
    #penup, 선을 안그리고
    turtle.penup()
    #해당 좌표로 이동 x,y
    turtle.goto(x, y)

#휠 클릭시 rgb전역으로 설정된 색 사용 선언부분
def  screenMidClick(x, y):
    global r, g, b
    # 1~9까지 랜덤한 정수 선택
    tSize = random.randrange(1, 10)
    #spapesize 거북이 모양, 크기
    turtle.shapesize(tSize)
    #색상 랜덤을 이용해서, 할당.rgb, 0~255사이
    r = random.random()
    g = random.random()
    b = random.random()
    print(f"랜덤 색 조회 r: {r} , g:{g} , b:{b}")

## 변수 선언 부분 ##
pSize = 10
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

#이벤트 핸들러 역할. onscreenClick
turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
