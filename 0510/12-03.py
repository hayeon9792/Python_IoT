

# Label(어디다?, 이 글씨를 출력, font, fg=foreground(글씨색),
# bg = background(배경색), anchor = SE(남동쪽 배치))

from tkinter import *
window = Tk()

label1 = Label(window, text = "SWEDU 공부 열심히")
label2 = Label(window, text = "열심히", font = ("궁서체", 30), fg="blue")
label3 = Label(window, text="공부중입니다.",bg="magenta", width=20, height=4,
anchor=SE)

label1.pack() # 라벨과 같은 위젯은 pack() 함수를 통해 화면에 출력
label2.pack()
label3.pack()

window.mainloop()