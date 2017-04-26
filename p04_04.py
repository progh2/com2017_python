
number = int(input("정수를 입력하시오: "))
result = 1
for i in range(number, 0, -1):
    result = result* i
print( "%d !은 %d 이다." % ( number ,  result ))
