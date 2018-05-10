'''
## 변수 선언 부분
ticket, sel, person = 0, 0, 0


## 메인(main) 코드 부분
ticket = int(input("1.이용권 2.입장권 : "))
if ticket == 1:
    sel = int(input("1.주간권 2.야간권 3.2일권 : "))
elif ticket == 2:
    sel = int(input("1.주간권 2.야간권 : "))
person = int(input("1.대인 2.청소년 3.소인/경로 : "))

if ticket == 1:
    if sel == 1:
        if person == 1:
            pass
        elif person == 2:
            pass
        elif person == 3:
            pass
    elif sel == 2:
        if person == 1:
            pass
        elif person == 2:
            pass
        elif person == 3:
            pass
    elif sel == 3:
        if person == 1:
            pass
        elif person == 2:
            pass
        elif person == 3:
            pass

elif ticket == 2:
    if sel == 1:
        if person == 1:
            pass
        elif person == 2:
            pass
        elif person == 3:
            pass
    elif sel == 2:
        if person == 1:
            pass
        elif person == 2:
            pass
        elif person == 3:
            pass
else :
    print("1 또는 2를 입력해주세요")

'''

'''
i, hap = 0,0

num_1 = int(input("시작값을 입력하세요 : "))
num_2 = int(input("끝값을 입력하세요 : "))

for i in range(num_1,num_2+1,1):
    hap=hap+i

print("%d에서 %d까지의 합 : %d" % (num_1, num_2, hap))
'''

'''
i, hap = 0, 0
num1, num2, num3 = 0, 0, 0
rept = 0
while rept<5:
    num1 = int(input("시작값 입력 : "))
    num2 = int(input("끝값 입력 : "))
    num3 = int(input("증가값 입력 : "))

    i = num1

    while i < (num2+1):
        hap = hap + i
        i = i + num3

    print("%d에서 %d까지 %d씩 증가함 값의 합 : %d\n" % (num1, num2, num3, hap))

    hap = 0
    rept = rept + 1
'''
'''
for i in range(1,100):
    print("for문을 %d번 실행했습니다." % i)
    if i == 5:
        break
i=1
while i<100:
    print("for문을 %d번 실행했습니다." % i)
    if i == 5:
        break
    i = i + 1

print(i)
'''


# aa = []
# for i in range(0, 100):
#     aa.append(i)
#
# print(len(aa))
# print(aa)
#
# for i in range(0, len(aa)):
#     print(aa[i], end=" ")
#     if i%10 == 9:
#         print("")

# aa = [10,20,30,40]
# print(aa[2:3])
# print(aa[2:2])

# import re
# hap = 0
# ss = input("연산할 문자열을 입력하세요. : ")
#
# ss_list = re.split("\+|-", ss)
# print(ss_list)
# for i in range(0,len(ss_list)):
#     hap += int(ss_list[i])
#
# print("계산 결과는 %d입니다." % hap)


# def plus(v1, v2):
#     result = 0
#     result = v1 + v2
#     return result
#
# def sub(v1, v2):
#     return v1 - v2
#
# def mux(v1, v2):
#     return v1 * v2
#
# def div(v1, v2):
#     return v1 / v2
#
# print("100과 200의 plus() 함수 결과는 %d" % plus(100, 200))
# print("100과 200의 sub() 함수 결과는 %d" % sub(100, 200))
# print("100과 200의 mux() 함수 결과는 %d" % mux(100, 200))
# print("100과 200의 div() 함수 결과는 %f" % div(100, 200))

# def make_array_1(row):
#     array_1 = []
#     val = 1
#
#     for k in range(0, row):
#         array_1.append(val)
#         val = (val+1) * 10
#
#     return array_1
#
# def print_array_1(array_1):
#     for k in range(0, len(array_1)):
#         print("%3d" % array_1[i], end=" ")
#     print("")
#
# def make_array_2(col, row):
#     array_1=[]
#     array_2=[]
#     val = 1
#
#     for i in range(0, col):
#         for k in range(0, row):
#             array_1.append(val)
#             val += 1
#         array_2.append(array_1)
#         array_1 = []
#
#     return array_2
#
# def print_array_2(array_2):
#     col = len(array_2)
#     row = len(array_2[0])
#     for i in range(0, col):
#         for k in range(0, row):
#             print("%3d" % array_2[i][k], end=" ")
#         print("")
#
# list2_col = int(input("행의 값을 입력하세요: "))
# list2_row = int(input("열의 값을 입력하세요: "))
#
# list2 = make_array_2(list2_col, list2_row)
# print_array_2(list2)
#
# list1 = make_array_1(list2_row)
# print_array_1(list1)
#
# while True:
#     sel = input("\n1. 숫자 검색, 2. 숫자 변경, 3. 리스트 출력, 4. 종료 : ")
#
#     if sel == "1":
#         search = int(input("검색할 숫자를 입력하세요.(1~%d) : " % (list2_col * list2_row)))
#         for i in range(0, list2_col):
#             if list2[i].count(search) != 0:
#                 c = list2[i].index(search)
#                 print("%d은 %d행 %d열에 있습니다." % (search, i, c))
#             else:
#                 if i == list2_col-1:
#                     print("찾는 숫자가 없습니다.")
#
#     elif sel == "2":
#         change = input("변경할 행과 열을 입력하세요.(행x열) : ")
#         value = int(input("변경할 값을 입력하세요. : "))
#         change_1 = int(change[0])
#         change_2 = int(change[2])
#         list2[change_1][change_2] = value
#         print("")
#
#     elif sel == "3":
#         print_array_2(list2)
#
#     elif sel == "4":
#         break
#     else :
#         print("잘못 입력하셨습니다. 다시 입력해주세요")

def total_func(list_total):
    kor = int(list_total[2])
    eng = int(list_total[3])
    math = int(list_total[4])
    return str(kor + eng + math)


def avg_func(list_total):
    total = int(list_total[5])
    str_avg = "%.1f\n" % (total / 3)
    return str_avg


def score_func():
    while True:
        score = input("학생이름과 성적을 입력하세요. : ")
        outList = score.split('/')
        if len(outList) == 4:
            outList.append(total_func(outList))
            outList.append(avg_func(outList))
            break
        else:
            print("다시 입력하세요. ex) 나강사/67/98/90")
            continue
    return outList


def print_array_2(array_2):
    for i in range(0, len(array_2)):
        for k in range(0, len(array_2[i])):
            print("%s\t" % array_2[i][k], end=" ")
        print("")


def add_total_avg(inList):
    inList[5] = total_func(inList)
    inList[6] = avg_func(inList)
    # print(inList)
    return inList


inFp = None
inList, inStr = [], ""
lineNum = 1
scoreList = []

with open("C:/Users/student/PycharmProjects/Python_IoT/score.csv", "r") as inFp:
    inList = inFp.readlines()
    print(inList)

# 2차원 배열로 변경
for i in range(0, len(inList)):
    studList = inList[i].split(',')
    scoreList.append(studList)
print_array_2(scoreList)
# print(scoreList)

# 합계 및 평균 추가
for i in range(1, len(scoreList)):
    studList = add_total_avg(scoreList[i])
    print(studList)
    scoreList[i] = studList

print_array_2(scoreList)
# print(scoreList)

'''
outList = [];
for i in range(0, len(scoreList)) :
    studStr = ",".join(scoreList[i]);
    outList.append(studStr);
print(outList);

with open("C:/Users/student/PycharmProjects/Python_IoT/score_result.csv", "w") as outFp :
    for inStr in outList :
        outFp.writelines(inStr);
'''


'''
def total_func(list_total):
    kor = int(list_total[1])
    eng = int(list_total[2])
    math = int(list_total[3])
    return str(kor+eng+math)

def avg_func(list_total):
    total = int(list_total[4])
    return str(total/3)

def score_func():
    while True:
        score = input("학생이름과 성적을 입력하세요. : ")
        outList = score.split('/')
        if len(outList) == 4:
            # print(outList)
            outList.append(total_func(outList))
            # print(outList)
            outList.append(avg_func(outList))
            # print(outList)
            break
        else :
            print("다시 입력하세요. ex) 나강사/67/98/90")
            continue
    return outList

def print_array_2(array_2):
    for i in range(0, len(array_2)):
        for k in range(0, len(array_2[i])):
            print("%5s\t" % array_2[i][k], end=" ")
        print("")

score_card = [["number", "name", "kor", "eng", "math", "total", "avg"]]

while True:
    sel = input("1. 입력  2. 출력   3. 종료 : ")

    if sel == '1':
        list_score = score_func()
        print(list_score)
        list_score.insert(0, str(len(score_card)))
        score_card.append(list_score)
    elif sel == '2':
        print_array_2(score_card)
    elif sel == '3':
        break
    else :
        print("잘못 입력하셨습니다. 다시 입력해주세요")
'''