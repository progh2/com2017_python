import turtle 
from turtle import textinput

number = int(textinput("질문", "몇 각형을 원하시나요?")
t = turtle.Turtle()
#t.shape("turtle")
for c in range(number):
    t.forward(100)
    t.right(360 / number)

input("종료하려면 엔터를 누르세요")