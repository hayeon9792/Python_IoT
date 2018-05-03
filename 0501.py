a = 0xFF
b = 0o77
c = 0b1111
print(a, b, c)
# print("%x, %o, %b" % (a,b,c))
print("0x{0:x} 0o{1:o} 0b{2:b}".format(a, b, c))

a = 3.14
b = 3.14e5
print(a, b)

a, b = 9, 2
print(a ** b, a % b, a // b)  # 제곱, 나머지, 소수점 버리는 나누기
""".
#include <stdio.h>
#include <memory.h>

typedef struct _tagHeap{
    int capacity; // 힙의 용량
    int heap_size; // 현재 힙 사이즈 -> insert 위치 => size-1
    int maxHeap[100001];
    _tagHeap()
    {
        capacity=0;
        h_size=0;
        memset(maxHeap, -1,sizeof(maxHeap));
    }
}Heap;

int pick(Heap *h) { return h->maxHeap[h->h_size-1]; }

void insertHeap(Heap *h, int data)
{
    // 사이즈가 용량 초과하면-> error
    if(h->h_size>=h->capacity)
    {
        //printf("E: 용량초과\n");
        return;
    }

    h->maxHeap[h->h_size]=data;
    // 사이즈 어디서 올릴지 잘 생각하기

    int cur = h->h_size++; //위치 저장 후 증가

    while(cur>0) //****** 불확실
    {
        int par = (cur-1)/2; // 값 swap 할 부모 위치

        // 부모의 값이 내 값보다 작으면(MAX HEAP 속성) 교환
        if(h->maxHeap[par] < h->maxHeap[cur])
        {
            int temp = h->maxHeap[cur];
            h->maxHeap[cur] = h->maxHeap[par];
            h->maxHeap[par] = temp;

            cur = par;
        }
        // 크면 return
        else return;    
    }
}

void deleteHeap(Heap *h)
{
    if(h->h_size <= 0)
    {
        //printf("E: 힙 사이즈 = 0\n");
        return;
    }
    // 빼내야 할 값 -> 루트 값
    int data = h->maxHeap[0];
    printf(" %d", data);
    h->h_size--;
    int cur = h->h_size; // 마지막 값

    // 마지막 값-> 루트 값에 넣고, -1로 바꾼다.
    int temp = h->maxHeap[cur];
    h->maxHeap[cur] = -1;
    h->maxHeap[0] = temp;

    cur = 0;
    left = (cur+1)*2;
    right = left+1;

    // 지금 사이즈 update 된 상태! => 마지막 요소 인덱스 = h->h_size-1
    // 자식이 없을 때까지-> 오른쪽 자식 없으면 왼쪽자식 확인, 있으면 둘 비교, 바꿀 자식 선택 
    // 만약 swap 조건 아니면 그대로 종료
    while(left < h->h_size) // left가 h->h_size 와 같거나, 크면 cur는 자식이 없다.
    {
        int sel = 0; //선택할 자식 인덱스
        if(right >= h->h_size) //오른쪽 존재X
            sel = left;
        else
        {
            if(right > left) sel = right; // 오른쪽이 더 크면 오른쪽이랑 바꿔줌 (maxHeap 정책)
            else sel = left;
        }

        if(sel > h->maxHeap[cur]) //자식이 더 크면
        {
            //swap!
            int temp = h->maxHeap[cur];
            h->maxHeap[cur] = h->maxHeap[sel];
            h->maxHeap[sel] = temp;
        }
        else
            return;

        cur = sel;
        left = (cur+1)*2;
        right = left+1;
    }
}

int main()
{
    int N;
    Heap* h;
    scanf("%d", &N);

    for(int i =0; i<N;i++)
        {
            int a;
            scanf("%d", &a);
            insertHeap(h,a);
        }
    for(int i=0;i<N;i++)
    {
        deleteHeap(h);
    }
    printf("\n");

    return;
}
"""

"""
#include <stdio.h>
#include <memory.h>

typedef struct _tagHeap{
    int capacity; // 힙의 용량
    int heap_size; // 현재 힙 사이즈 -> insert 위치 => size-1
    int maxHeap[100001];
    _tagHeap()
    {
        capacity=0;
        h_size=0;
        memset(maxHeap, -1,sizeof(maxHeap));
    }
}Heap;

int pick(Heap *h) { return h->maxHeap[h->h_size-1]; }

void insertHeap(Heap *h, int data)
{
    // 사이즈가 용량 초과하면-> error
    if(h->h_size>=h->capacity)
    {
        //printf("E: 용량초과\n");
        return;
    }

    h->maxHeap[h->h_size]=data;
    // 사이즈 어디서 올릴지 잘 생각하기

    int cur = h->h_size++; //위치 저장 후 증가
    //int left = (cur+1)*2;
    //int right = left+1;

    while(cur>0)
    {
        int par = (cur-1)/2; // 값 swap 할 부모 위치

        // 부모의 값이 내 값보다 작으면(MAX HEAP 속성) 교환
        if(h->maxHeap[par] > h->maxHeap[cur])
        {
            int temp = h->maxHeap[cur];
            h->maxHeap[cur] = h->maxHeap[par];
            h->maxHeap[par] = temp;

            cur = par;
        }
        // 크면 return
        else return;    
    }
}

void deleteHeap(Heap *h)
{
    if(h->h_size <= 0)
    {
        //printf("E: 힙 사이즈 = 0\n");
        return;
    }
    // 빼내야 할 값 -> 루트 값
    int data = h->maxHeap[0];
    printf(" %d", data);
    h->h_size--;
    int cur = h->h_size; // 마지막 값

    // 마지막 값-> 루트 값에 넣고, -1로 바꾼다.
    int temp = h->maxHeap[cur];
    h->maxHeap[cur] = -1;
    h->maxHeap[0] = temp;

    cur = 0;
    left = (cur+1)*2;
    right = left+1;

    // 지금 사이즈 update 된 상태! => 마지막 요소 인덱스 = h->h_size-1
    // 자식이 없을 때까지-> 오른쪽 자식 없으면 왼쪽자식 확인, 있으면 둘 비교, 바꿀 자식 선택 
    // 만약 swap 조건 아니면 그대로 종료
    while(left < h->h_size) // left가 h->h_size 와 같거나, 크면 cur는 자식이 없다.
    {
        int sel = 0; //선택할 자식 인덱스
        if(right >= h->h_size) //오른쪽 존재X
            sel = left;
        else
        {
            if(right > left) sel = right; // 오른쪽이 더 크면 오른쪽이랑 바꿔줌 (maxHeap 정책)
            else sel = left;
        }

        if(sel > h->maxHeap[cur])
        {
            //swap!
            int temp = h->maxHeap[cur];
            h->maxHeap[cur] = h->maxHeap[sel];
            h->maxHeap[sel] = temp;
        }
        else
            return;

        cur = sel;
        left = (cur+1)*2;
        right = left+1;
    }
}

int main()
{
    int N;
    Heap* h;
    scanf("%d", &N);

    for(int i =0; i<N;i++)
        {
            int a;
            scanf("%d", &a);
            insertHeap(h,a);
        }
    for(int i=0;i<N;i++)
    {
        deleteHeap(h);
    }
    printf("\n");

    return;
}
"""
"""
a = '''파이썬
만세'''
a
print(a)

print("%10s" %"파이썬")

"""
"""
## 변수 선언 부분
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

## main ##
money = int(input("교환할 돈: "))

c500 = money//500
money %= 500

c100 = money//100
money%=100

c10 = money//10
money%=10

print("\n 500원 %d개" % c500)
print("\n 100원 %d개" % c100)
print("\n 50원 %d개" % c50)
print("\n 10원 %d개" % c10)
print("\n 못 바꾼 잔돈 %d원" % money)
"""
"""
## 변수 선언 부분
money, c500, c100, c50, c10 = 0, 0, 0, 0, 0

## main ##
money = int(input("교환할 돈: "))

c500 = money//50000
money %= 50000

c100 = money//10000
money%=10000

c50 = money//5000
money%=5000

c10 = money//1000
money%=1000

print("\n 오만원짜리 ==> %d장" % c500)
print("\n 만원짜리 ==> %d장"  % c100)
print("\n 오천원짜리 ==> %d장"  % c50)
print("\n 천원짜리 ==> %d장"  % c10)
print("\n 못 바꾼 돈 ==> %d원"  % money)
"""

# sec 입력 받고, 몇시간, 몇분 몇초인지 출력

## 변수 선언 ##
u_min = 60;
u_hour = u_min * 60;
u_day = u_hour * 24;

sec, min, hour, day, buf_s, buf_m, buf_h = 0, 0, 0, 0, 0, 0, 0;

sec = int(input("초 입력: "));

min = sec // 60;
buf_s = sec % 60;

hour = min // 60;
buf_m = min % 60;

day = hour // 24;
buf_h = hour % 24

# print("%d초 = %d일 %d시간 %d분 %d초" % (sec, day, buf_h, buf_m, buf_s));
print("")

