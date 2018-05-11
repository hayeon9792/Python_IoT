'''
inFp = None;
inStr=""

inFp = open("C:/Users/student/PycharmProjects/Python_IoT/data1.txt","r", encoding = "utf-8");

inStr = inFp.readline();
print(inStr, end="");

inStr = inFp.readline();
print(inStr, end="");

inStr = inFp.readline();
print(inStr, end="");

inFp.close()
'''
'''
inFp = None
inStr = ""

inFp = open("C:/Users/student/PycharmProjects/Python_IoT/data1.txt","r", encoding = "utf-8");

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end="");

inFp.close();
'''

'''
inFp = None
inStr = ""

inFp = open("C:/Users/student/PycharmProjects/Python_IoT/score.csv","r");

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    print(inStr, end="");

inFp.close();

# 2차원 배열로 변경
for i in range(0, len(inList)) :
    studList = inList[i].split('.');
    scoreList.append(studList);
print_array_2(scoreList);

# 합계 및 평균 추가
for i in range(1, len(scoreList)) :
    studList = add_total_avg(scoreList[i]);
    print(studList);
    scoreList[i] = studList

print_array_2(scoreList);
'''
'''
outFp = None;
outStr = "";

outFp = open("C:/Users/student/PycharmProjects/Python_IoT/data1.txt","w", encoding = "utf-8");

while True :
    outStr = input("내용 입력: ");
    if outStr != "" :
        outFp.writelines(outStr + "\n");
    else :
        break;

outFp.close();
print("---정상적으로 파일에 써졌음---");
'''
'''
inFp, outFp = None, None;
inStr = ""

inFp = open("C:/Windows/win.ini", "r", encoding="utf-8");
outFp = open("C:/Temp/data3.txt","w", encoding = "utf-8");

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr);

inFp.close();
outFp.close();
print(" --- 정상적으로 파일이 복사되었음 -- ");
'''

from tkinter import *

window = None;
canvas = None;
XSIZE, YSIZE = 256, 256;

window = Tk();
window.title("흑백 사진 보기");
canvas = Canvas(window, height = XSIZE, width = YSIZE);

paper = PhotoImage(width = XSIZE, height = YSIZE);
canvas.create_image((XSIZE/2, YSIZE/2), image = paper, state = "normal");

fp = open('C:/Temp/Citrus.raw','rb');

for i in range(0,XSIZE) :
    for k in range(0, YSIZE) :
        data = int(ord(fp.read(1)))
        paper.put("#%02x%02x%02x" % (data, data, data), (k,i));

fp.close();

canvas.pack();
window.mainloop();