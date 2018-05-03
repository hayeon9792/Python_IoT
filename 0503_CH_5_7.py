

'''
n, m, num = 0, 0, 1

print("배열을 만들어 봅시다.");
n = int(input("행의 크기 : "));
m = int(input("열의 크기 : "));

for i in range(0, n) :
    for j in range(0,m) :
        print("%2d" % num, end = " ");
        num += 1;
    print("");
'''

'''
i, num = 1, 0
n = int(input("1부터 n까지의 합, n = "));
while i <= n :
    num += i;
    i += 1;

print("1부터 %d까지의 합 = %d" %(n, num));
'''

# True, False

# ctrl + alt + i
# 자동 코드 정렬

'''
for i in range(1, 100) :
    print("for문을 %d번 실행했습니다." % i );
    if i == 5 :
        break;

print("")

i = 1;
while i < 101 :
    print("for문을 %d번 실행했습니다." % i );
    if i == 5 :
        break;
    i += 1;
'''

'''
hap,  i = 0, 0
for i in range(1,101) :
    hap += i;

    if hap >= 1000 :
        break
print("1~100의 합에서 최초로 1000이 넘는 위치: %d" % i);
'''

'''
for i in range(0,3,1) :
    for k in range(0,2,1) :
        print("파이썬은 꿀(i값 :%d, k값: %d)" % (i,k));
'''

# 리스트 추가 -> arr.append(값)
"""
리스트 함수

append() : 제일 뒤에 항목 추가
pop() : 제일 뒤의 항목 빼고, 삭제
sort() : 정렬
reverse() : 역순
index() : 지정 값 찾아서 위치 반환
insert() : 지정 위치에 값 insert
remove() : 지정 값 삭제, 여러 개면 처음 것만 삭제
extend() : 리스트 뒤에 리스트 추가, 리스트의 더하기 연산
count() : 지정 값의 개수 센다
del() : 리스트에서 해당 위치 항목 삭제
len() : 리스트의 길이 반환

"""


'''
a = 0;
arr = [];

print("입력: ");

for i in range(0, 10) :
    a = int(input());
    arr.append(a);

for i in range(0, 10) :
    print("%d " % arr[i], end = "");

print("");

'''

'''
i = 0;
aa = [];
bb = [];
value = 0;
'''

'''
aa = [0 for i in range(100)];

for i in range(0, 100) :
    aa.append(value);
    value += 2;

for i in range(0, 100) :
    bb.append(aa[99-i]);

print(aa);
print(bb);
'''


''''
aa = [10, 20, 30]
aa[1:2] = [200, 201]; # [10, 200, 201, 30]
# 1부터 1개를 바꾸는 것
print(aa)

aa = [10, 20, 30, 40, 50]
aa[1:4] = [];
# 1부터 3개를 삭제하는 것
print(aa)
'''


'''
myList = [30, 10, 20];
print("현재 리스트 : %s "% myList);

myList.append(40)
print("append(40) 후의 리스트 : %s" %myList);

print("pop()으로 추출한 값 : %s" %myList.pop());
print("pop() 후의 리스트 : %s" % myList);

myList.sort();
print("sort() 후의 리스트 : %s"% myList);

myList.reverse();
print("reverse() 후의 리스트 : %s" %myList);

print("20 값의 위치: %d" %myList.index(20));

# insert(index, element)
myList.insert(2, 222)
print("insert(2, 222) 후의 리스트 : %s" % myList);

myList.remove(222);
print("remove(222) 후의 리스트 : %s" % myList);

myList.extend([77, 88, 77]);
print("extend([77, 88, 77]) 후의 리스트 : %s" %myList);

print("77 값의 개수 : %d" % myList.count(77));
'''

import random

numbers = []

for num in range(0,10) :
    numbers.append(random.randrange(1,100));

print("생성된 리스트 ", numbers);

# sort() 이용
'''
numbers.sort();
print("가장 큰 수는 %d이고, 가장 작은 수는 %d 이다. "% (numbers[9], numbers[0]));
'''

# bubble sort 이용
'''
for i in range(0, 9) :
    for j in range(i, 9) :
        if numbers[j]>numbers[j+1] :
            temp = numbers[j];
            numbers[j+1] = numbers[j];
            numbers[j+1] = temp;

print("%s" % numbers);
'''

# selection sort 이용
# 앞부터 가장 작은 값 or 가장 큰 값 찾아서 위치 교환
'''
for i in range(0, 10) :
    temp = numbers[i]; # 첫 값도 저장
    idx = i; # 첫 인덱스 저장
    for j in range(i, 10) : # 다음 인덱스부터 끝까지 탐색하면서 지금 값(temp)보다 작은 값
                            #  만나면 idx랑 temp값 갱신
        if numbers[j] < temp :
            idx = j;
            temp = numbers[j];
    numbers[idx] = numbers[i];
    numbers[i] = temp;
print("%s" % numbers);
'''

# insertion sort 이용
# 가장 작은 값을 찾아서 앞에 넣기

for i in range(0, 10) :



'''
import random

arr1 = []
arr2 = []

for num in range(0,10) :
    arr1.append(random.randrange(1,100));
    arr2.append(random.randrange(1, 100));

arr1.extend(arr2)

print("생성된 리스트 %s" % arr1);
'''