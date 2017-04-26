import turtle 

t = turtle.Turtle()
t.shape("turtle")
x1 = int(input("큰 원의 중심좌표 x1: ")) 
y1 = int(input("큰 원의 중심좌표 y1: ")) 
r1 = int(input("큰 원의 반지름: "))
x2 = int(input("작은 원의 중심좌표 x2: ")) 
y2 = int(input("작은 원의 중심좌표 y2: ")) 
r2 = int(input("작은 원의 반지름: "))
t.penup() #원 그리기 
t.goto(x1, y1) 
t.pendown() 
t.circle(r1)
t.penup() #원 그리기 
t.goto(x2, y2) 
t.pendown() 
t.circle(r2)

#  구현 
d2 = (x1 - x2 )** 2 + (y1 - y2) ** 2
d = d2 ** 0.5

if d <= r1 :
    print("작은 원이 큰원 안에 있습니다.")
else:
    print("작은 원이 큰원 밖에 있습니다.")
    
input("종료하려면 엔터를 누르세요")