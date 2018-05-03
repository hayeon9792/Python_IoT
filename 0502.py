"""
print(0x74E5, '=' , bin(0x74E5))
print(0x0143, '=', bin(0x0143))
print(bin(0x74E5|0x0143))
"""

"""
0000 0001 (0d1)
-> 반전
1111 1110
-> +1
1111 1111

반대의 부호를 찾고 싶을 때-> ~a + 1;
"""
"""
a = 0b0000000;

for i in range(0, 8) :
    print(bin(a));
    if (i == 4) :
        print(" ")
    a |= (1<<i);

a = 100
result = 0
i = 0

for i in range(1,5) :
    result = a<<i
    print("%d << %d = %d" %(a,i,result))

for i in range(1,5) :
    result = a>>i
    print('%d >> %d = %d' % (a,i, result))

# Python Tutor

a = 200
if a<100 :
    print("100보다 작군요.");
    print("참이면 이 문장도 보이겠죠?");
else :
    print("100보다 크다");
    print("거짓이면 이 문장 보인다.")

a = int(input("a = "));
b = int(input("b = "));

if a>b :
    print("a가 b보다 크다.");
elif a<b :
    print("b가 a보다 크다.");
else :
    print("a와 b가 같다.");


"""
'''
score = int(input("점수 입력: "));

if (score>=90) :
    print("A");
elif (score>=80 and score<90) :
    print('B');
elif (score>=70 and score<80) :
    print('C');
elif (score>=60 and score<70) :
    print('D');
else :
    print('F');

'''
'''
# 변수 선언
a,b,ch = 0, 0, ""

a = int(input('a = '));
ch = str(input('operator = '));
b = int(input('b = '));

if (ch == '+') :
    print("%d + %d = %d" % (a, b, a+b));
elif (ch == '-') :
    print("%d - %d = %d" % (a, b, a-b));
elif (ch == '*') :
    print("%d * %d = %d" % (a, b, a*b));
elif (ch == '/') :
    print("%d / %d = %d" % (a, b, a/b));
elif (ch == '%') :
    print("%d %% %d = %d" % (a, b, a%b));
elif (ch == "//") :
    print("%d // %d = %d" % (a, b, a//b));
elif (ch == '**') :
    print("%d ** %d = %d" % (a, b, a**b));
else :
    print("알 수 없는 연산자입니다.");

'''

'''
# 변수 선언

ins, a, b, op = 0, 0, 0, ""
# 4비트까지만,

ins = int(input("1. 논리연산을 하시겠습니끼?\n2. 산술연산을 하시겠습니까?\n"
                "3. 시프트 연산을 하시겠습니까?\n번호 입력: "));

if ins == 1 :
    print("논리연산을 선택하셨습니다.");
    a = str(input("첫번째 4비트 값을 입력하세요 : "));
    op = str(input("계산 할 연산자를 입력하세요: "));
    b = str(input("두번째 4비트 값을 입력하세요 : "));

    a = int(a,2);
    b = int(b,2);

    if (op == '&') :
        print("{0:04b} & {1:04b} = {2:04b}".format(a, b, a & b));
    elif (op == '|'):
        print("{0:04b} | {1:04b} = {2:04b}".format(a, b, a | b));
    elif (op == '^'):
        print("{0:04b} ^ {1:04b} = {2:04b}".format(a, b, a ^ b));
    else :
        print("알 수 없는 연산자입니다.");

elif ins == 2 :

    a = str(input('a = '));
    op = str(input('operator = '));
    b = str(input('b = '));

    if (op == '+'):
        print("%d + %d = %d" % (a, b, a + b));
    elif (op == '-'):
        print("%d - %d = %d" % (a, b, a - b));
    elif (op == '*'):
        print("%d * %d = %d" % (a, b, a * b));
    elif (op == '/'):
        print("%d / %d = %d" % (a, b, a / b));
    elif (op == '%'):
        print("%d %% %d = %d" % (a, b, a % b));
    elif (op == "//"):
        print("%d // %d = %d" % (a, b, a // b));
    elif (op == '**'):
        print("%d ** %d = %d" % (a, b, a ** b));
    else:
        print("알 수 없는 연산자입니다.");

elif (ins == 3) :
    num = 0;

    print("시프트연산을 선택하셨습니다.");
    a = int(input("첫번째 4비트 값을 입력하세요 : "), 2);
    op = str(input("계산 할 연산자를 입력하세요: "));
    num = int(input("시프트 횟수를 입력하세요 : "));

    if (op == '<<') :
        print("{0:b} << {1:d} = {2:b} 입니다.".format(a, num, a << num));
    elif (op == '>>'):
        print("{0:b} >> {1:d} = {2:b} 입니다.".format(a, num, a >> num));
    else:
        print("알 수 없는 연산자입니다.");


else :
    print("'1' 또는 '2'만 입력할 수 있습니다.");

'''
'''
fruit = ['사과', '배', '딸기', '포도'];
print(fruit[0]);
'''

'''
## 변수 선언 ##
sel, ans, munStr, num1, num2 = 0, 0, "", 0, 0

## main func. ##
sel = int(input(" 1. 수식 계산기\n 2. 두 수 사이 합계\n 입력 : "));

if (sel == 1) :
    numStr = input(" *** 수식을 입력하세요 : ");
    ans = eval(numStr); # 수식을 문자열로 받아서 계산해주는 함수
    print(" '%s = %5.1f' "% (numStr, ans));
elif (sel == 2) :
    num1 = int(input(" *** 첫 번째 숫자 입력: "));
    num2 = int(input(" *** 두 번째 숫자 입력: "));
    for i in range(num1, num2+1) :
        ans+=i;
    print(" '%d + ... + %d = %d' " % (num1, num2, ans));
else :
    print(" '1' 또는 '2'만 입력할 수 있습니다.");
'''
'''
i, num_p, T, T1, T2, buf, cost = 0, 0, 0, 0, 0, 0, 0

T = int(input(" 1. 이용권\n 2. 입장권\n => "));
num_p = int(input(" *** 총 인원 수 : "));

# 다 처리할 때까지
while i < num_p :

    buf = 0;

    ## 이용권
    if (T == 1) :
        T1 = int(input(" 1. 주간권(1일권)\n 2. 야간권(17시~)\n 3. 2일권\n =>"));

        ## 주간권
        if(T1 == 1) :
            T2 = int(input(" 1. 대인\n 2. 청소년\n 3. 소인/경로\n => "));
            buf = int(input(" *** 인원 수: "));

            i += buf;

            if(T2 == 1) :
                cost += (buf*52000);
            elif (T2 == 2) :
                cost += (buf * 44000);
            elif (T2 == 3):
                cost += (buf * 41000);
            else :
                print("E: 다시 선택해 주세요.");

        ## 야간권
        elif(T1 == 2) :
            T2 = int(input(" 1. 대인\n 2. 청소년\n 3. 소인/경로\n => "));
            buf = int(input(" *** 인원 수: "));

            i += buf;

            if (T2 == 1) :
                cost += (buf * 43000);
            elif (T2 == 2) :
                cost += (buf * 37000)
            elif (T2 == 3):
                cost += (buf * 34000);

            else :
                print("E: 다시 선택해 주세요.");

        ## 2일권
        elif (T == 3):
            T2 = int(input(" 1. 대인\n 2. 청소년\n 3. 소인/경로\n => "))
            buf = int(input(" *** 인원 수: "));

            i += buf;

            if (T2 == 1) :
                cost += (buf * 81000);
            elif (T2 == 2) :
                cost += (buf * 68000)
            elif (T2 == 3):
                cost += (buf * 64000);
            else :
                print("E: 다시 선택해 주세요.");

        else:
            print("E: 다시 선택해 주세요.");

    ##          이용권 종료 입장권 시작          ##
    ## 입장권
    elif (T == 2):
        T1 = int(input(" 1. 주간권(1일권)\n 2. 야간권(17시~)\n =>"));

        ## 주간권
        if (T1 == 1):
            T2 = int(input(" 1. 대인\n 2. 청소년\n 3. 소인/경로\n => "));
            buf = int(input(" *** 인원 수: "));

            i += buf;

            if (T2 == 1) :
                cost += (buf * 43000);
            elif (T2 == 2) :
                cost += (buf * 36000)
            elif (T2 == 3):
                cost += (buf * 33000);
            else :
                print("E: 다시 선택해 주세요.");

        ## 야간권
        elif (T1 == 2):
            T2 = int(input(" 1. 대인\n 2. 청소년\n 3. 소인/경로\n => "));
            buf = int(input(" *** 인원 수: "));

            i += buf;

            if (T2 == 1) :
                cost += (buf * 35000);
            elif (T2 == 2) :
                cost += (buf * 32000)
            elif (T2 == 3):
                cost += (buf * 30000);
            else :
                print("E: 다시 선택해 주세요.");

        else:
            print("E: 다시 선택해 주세요.");

print("총 %d명 %d 원 입니다." % (num_p, cost));
'''

'''
for i in range(0,3,2) :
    print("Hello");


for i in range(0, 5, 1) :
    if(i != 4) :
        print("%d " % (i+1), end =""); # \n 없애고 싶을 때
    else :
        print("%d" % (i + 1));



a, b, sum = 0, 0, 0

a = int(input("시작값: "));
b = int(input("끝값: "));

for i in range(a, b+1) :
    sum+=i;

print("%d부터 %d까지의 합 : %d" %(a,b,sum));
'''

for i in range(2, 10, 1):
    for j in range(1, 10, 1):
        if (j != 9):
            print("%2d X%2d = %2d" % (i, j, i * j), end="\t\t");
        else:
            print("%2d X%2d = %2d" % (i, j, i * j), end="");
    print("")
