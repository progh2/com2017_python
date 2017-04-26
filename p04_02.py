import turtle 

number = 60
t = turtle.Turtle()
#t.shape("turtle")
for c in range(number):
    t.circle(100)
    t.right(360 / number)

input("종료하려면 엔터를 누르세요")