
grades = []
number =int(input("입력 할 수의 개수를 입력하세요: "))

for i in range(number):
    grades.append(int(input("정수를 입력하시오: ")))

print( "평균= %.1f" % (sum(grades) / len(grades)) )
