# # 클래스 정의 부분
# class Car :
#     color = "";
#     speed = 0;
#     name = ""; # name 속성 추가
#
#     def upSpeed(self, value) :
#         self.speed += value;
#         if(self.speed >= 150) :
#             self.speed = 150;
#
#     def downSpeed(self, value) :
#         self.speed -= value;
#         if(self.speed < 0) :
#             self.speed = 0;
#
# # 메인 코드 부분
# myCar1 = Car(); #인스턴스 생성
# myCar1.color = "빨강";
# myCar1.speed = 0;
#
# myCar2 = Car();
# myCar2.color = "파랑";
# myCar2.speed = 0;
#
# myCar3 = Car();
# myCar3.color = "노랑";
# myCar3.speed = 0;
#
# myCar1.upSpeed(200);
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." %(myCar1.color , myCar1.speed));
#
# myCar2.upSpeed(60);
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." %(myCar2.color , myCar2.speed));
#
# myCar3.upSpeed(0);
# print("자동차3의 색상은 %s이며, 현재 속도는 %dkm 입니다." %(myCar3.color , myCar3.speed));

# class Car :
#     color = "";
#     speed = 0;
#     name = ""; # name 속성 추가
#     num = 0;
#
#     def __init__(self) :
#         self.color = "빨강";
#         self.speed = 0;
#         self.num = self.num + 1;
#
# myCar1 = Car();
# myCar2 = Car();
# myCar3 = Car();
# print("%d %d %d"%(myCar1.num, myCar2.num, myCar3.num));


# class Car :
#     color = "";
#     speed = 0;
#
#     def __init__(self, value1, value2) :
#         self.color = value1;
#         self.speed = value2;
#
# #메인 코드 부분
# myCar1 = Car("빨강", 30);
# myCar2 = Car("파랑", 60);
#
# print("자동차1의 색상은 %s이며, 현재 속도는 %dkm 입니다." %(myCar1.color , myCar1.speed));
# print("자동차2의 색상은 %s이며, 현재 속도는 %dkm 입니다." %(myCar2.color , myCar2.speed));
#


# # 클래스 선언
# class Car :
#     color = "" # 인스턴스 변수
#     speed = 0; # 인스턴스 변수
#     count = 0; # 클래스 변수
#
#     def __init__(self):
#         self.speed = 0;
#         Car.count += 1; # className.변수이름 으로 접근
#
#     def __del__(self):
#
#
# # 변수 선언
# myCar1, myCar2 = None, None;
#
# # 메인 코드 부분
# myCar1 = Car();
# myCar1.speed = 30;
# print("자동차1의 현재 속도는 %dkm 이며, 현재 생산된 자동차의 수는 %d이다." %(myCar1.speed , Car.count));
#
# myCar2 = Car();
# myCar2.speed = 60;
# print("자동차2의 현재 속도는 %dkm 이며, 현재 생산된 자동차의 수는 %d이다." %(myCar2.speed , myCar2.count));
# print("자동차2의 현재 속도는 %dkm 이며, 현재 생산된 자동차의 수는 %d이다." %(myCar2.speed , Car.count));
#
# # 소멸자 => del
#
# del myCar1;
# print("%d"%myCar2.speed);
# print("%d"%myCar1.speed);


# class Car :
#     speed = 0;
#
#     def upSpeed(self, value) :
#         self.speed += value;
#         if(self.speed >= 150) :
#             self.speed = 150;
#
#     def downSpeed(self, value) :
#         self.speed -= value;
#         if(self.speed < 0) :
#             self.speed = 0;
#
# class Sedan(Car) :
#     seatNum = 0; # 새로 추가한 속성
#
#     def getSeatNum(self) :
#         return self.seatNum;
#
# class Truck(Car) :
#     capacity = 0; # 새로 추가한 속성
#
#     def getCapacity(self) :
#         return self.capacity;
#
# # 변수 선언
# sedan1, truck1 = None, None;
#
# # 메인 코드 부분
# sedan1 = Sedan();
# truck1 = Truck();
#
# sedan1.upSpeed(100);
# truck1.upSpeed(80);
#
# sedan1.seatNum = 5;
# truck1.capacity = 50;
#
# print("승용차의 속도는 %dkm, 좌석의 수는 %d개 입니다." % (sedan1.speed, sedan1.getSeatNum()));
# print("트럭의 속도는 %dkm, 총 중량은 %d톤 입니다." % (truck1.speed, truck1.getCapacity()));


