'''
cnt, n, m, arr, arr2 = 1, 0, 0, [], [];

n = int(input("행의 크기: "));
m = int(input("열의 크기: "));

print("- 크기가 %dX%d 일 경우" %(n,m));

for i in range(0, n) :
    for j in range(0, m) :
        arr2.append(cnt);
        cnt += 1;
    arr.append(arr2);
    arr2 = [];

ins = 0;

while(1) :
    ins = int(input("1. 숫자 검색, 2. 숫자 변경, 3. 리스트 출력, 4. 종료 : "));

    if(ins == 1) :
        ins2 = 0;
        ins2 = int(input("검색할 숫자를 입력하세요 (1~%d) : " % (n*m)));

        for i in range(0, n) :
            for j in range (0,m) :
                if(arr[i][j]==ins2) :
                    print("%d은 %d행 %d열에 있습니다." % (ins2, i, j));
                    break;

    elif(ins == 2) :
        ins2, insstr = 0, "";
        insstr = input("변경할 행과 열을 입력하세요.(행X열) : ");
        liststr = list(insstr);
        ins2 = int(input("변경할 값을 입력하세요. : " ));

        for i in range(0, n) :
            for j in range (0,m):
                if(i == int(liststr[0]) and j == int(liststr[2])) :
                    print("%d행 %d열의 값이 %d로 변경되었습니다." % (i, j, ins2));
                    arr[i][j] = ins2;
                    break;

    elif (ins == 3) :
        for i in range(0, n) :
            for j in range (0,m):
                print("%2d  " % arr[i][j], end="");
            print("")

    elif(ins == 4) :
        break;

    else :
        print("'1'~'4' 의 숫자만 입력하세요. ");

    print("");

'''

'''
coffee = 0;

def coffee_machine(button) :
    print()
    print("# 1. (자동으로) 뜨거운 물을 준비한다.");
    print("# 2. (자동으로) 종이컵을 준비한다.");

    if button == 1:
        print("# 3. (자동으로) 보통 커피를 탄다.");
    elif button == 2:
        print("# 3. (자동으로) 설탕 커피를 탄다.");
    elif button == 3:
        print("# 3. (자동으로) 블랙 커피를 탄다.");
    else :
        print("# 3. (자동으로) 아무거나 탄다.");

    print("# 4. (자동으로) 물을 붓는다.");
    print("# 5. (자동으로) 스푼으로 저어서 녹인다.");
    print();01

coffee = int(input("어떤 커피를 드릴까요? (1:보통 2:설탕 3:블랙)"));
coffee_machine(coffee);
print("손님~ 커피 나왔습니다.");
'''