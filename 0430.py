# 한 줄 주석
"""
20180430 Day-1
여러 줄 주석
"""

"""
print("Hello world!")
a = 100
b = 100
result = a+b
print(a + b)
print(a, "+", b , "=" , result)
"""

"""
restart shell => ctrl + f6
변수의 자료형 확인 => type(a)
"""

"""
a = 100
b = 50
result=a+b
print(a,"+",b,"=",result)
result=a-b
print(a,"-",b,"=",result)
result=a*b
print(a,"*",b,"=",result)
result=a/b
print(a,"/",b,"=",result)
"""
"""
# print("a = ")
a = int(input("a = ")) # 형 변환 필요
# print("b = ")
b = int(input("b = "))
result=a+b
print(a,"+",b,"=",result)
result=a-b
print(a,"-",b,"=",result)
result=a*b
print(a,"*",b,"=",result)
result=a/b
print(a,"/",b,"=",result)
"""
'''
## GUI module import ##
from tkinter import *

window = None
canvas = None
x1, y1, x2, y2 = None, None, None, None

def mouseClick(event):
    global x1,y1
    x1=event.x
    y1=event.y
    print("Click: ", x1, ",", y1)

def mouseDrop(event):
    x2 = event.x
    y2 = event.y
    print("Drop: ", x2,",", y2)
    #이 시점에 선이 그려짐
    canvas.create_line(x1,y1,x2,y2,width=5,fill = "red")

window = Tk()
window.title("그림판 비슷한 프로그램")
canvas = Canvas(window, height = 300, width = 300)
# Interrupt 방식으로 마우스 입력 받음
canvas.bind("<Button-1>", mouseClick)
print("print: ", x2, ",", y2)
canvas.bind("<ButtonRelease-1>", mouseDrop)
canvas.pack()
# 마우스 누르고 떼기 전까지 while(1)
window.mainloop()
'''

'''
print("글자","100")
print("숫자","%d" % 100)
a=100
b=10
c=a+b
print("%d  + %d = %d" %(a,b,c))

## FORMAT ##
# 멤버 함수 단축키 -> ctrl + space
# .format(0,1,2, ... )-> 안에 인덱스로 접근
print("{0:d} {1:5d} {2:05d}".format(123,123,123))
print("{0:x} {1:5x} {2:05x}".format(123,123,123))
print("{1:d} {0:10d} {2:010d}".format(123,456,789))
# binary 프린트 할 때 편하다 ***
# 문자열 표현 할 때, " ", ' ' 둘 다 가능

print("\n줄바꿈\n연습")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 '강조'되는 효과2")
print("\\\\\\ 역슬래쉬 세 개 출력")
print(r "\n \t \" \\ 를 그대로 출력")
'''
'''
    a = int(input("하루 수업 시간: "))
    b = int(input("주 몇 일 수업? : "))
    c = int(input("몇 달: "))
    a = a * b * 4 * c
    print("총 %d 시간 수업" % a)
    print("3학점 짜리 수업-> 주 3시간 수업, 4개월")
    print("3학점 짜리 수업 총 %d 시간 수업" % (3 * 4 * 4))
'''


Ks= int(input("국어 성적: "))
Es = int(input("영어 성적: "))
Ms = int(input("수학 성적: "))
print("총점은 %d이고, 평균은 %.2f점 입니다." % ((Ks+Es+Ms) , (Ks+Es+Ms)/3 ))


