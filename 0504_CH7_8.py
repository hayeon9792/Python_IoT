'''

a = [10, 20, 30];
print(a);

a[1:2] = ['a','b','c'];
print(a);

a = [10, 20, 30];
print(a);

a[1] = ['a','b','c'];
print(a);

'''

'''
parking = [];
top, carName, outCar = 0, "A", "";
sel = 9;

while(sel!=3) :
    sel = int(input("<1>자동차 넣기 <2>자동차 빼기 <3>끝 :"));

    if( sel == 1) :
        n = 0
        n = int(input("몇 대? : "));

        if(n+top>5) :
            print("만차 (여유공간: %d)" % (5-top));
        else :
            for i in range(0,n) :
                parking.append(carName);
                print("'%s' 자동차 들어감, 현재 : %s " % (parking[top+i], parking));
                carName = chr(ord(carName)+1);
            top += n;


    elif(sel == 2) :
        n = 0
        n = int(input("몇 대? : "));

        if(top-(n-1)<0) :
            print("다시 확인해주세요");
        else :
            for i in range(0,n) :
                if(top-i >= 0):
                    print("'%s' 자동차 뺌, " % parking[top-i], end = "");
                parking.pop();
                if((top-i)>0) :
                    print("현재 : %s" % (parking));
                else :
                    print("차가 없습니다.")
            top -= n;

    else :
        print("'1' '2' '3' 만 입력해주세요.");
'''

# 이중 배열

# 4*5의 2차원 리스트를 만들고 0부터 3의 배수를 입력하고 출력해보세요.
'''
list1 = [];
list2 = [];
value = 0;

for i in range(0,4) :
    for j in range(0,5) :
        list1.append(value);
        value += 3;
    list2.append(list1);
    list1 = [];

for i in range(0,4) :
    for j in range(0,5) :
        if(j != 4) :
            print("%2d " % list2[i][j], end = "");
        else :
            print("%2d" % list2[i][j], end = "");
    print("");
    
'''

foods = { "떡볶이" : "오뎅",
          "짜장면" : "단무지",
          "라면" : "김치",
          "피자" : "피클"};

while(True) :
    myfood = input(str(list(foods.keys())) + " 중 좋아하는 것은?(종료: '끝' 입력) : ");
    if myfood in foods :
        print(" <%s> 궁합 음식은 <%s> 입니다." %(myfood, foods.get(myfood)));
    elif myfood == "끝" :
        break;
    else :
        print("그런 음식이 없습니다.");