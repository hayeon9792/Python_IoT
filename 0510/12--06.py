from tkinter import *
from tkinter import messagebox

# 함수 정의 부분
def myFunc() :
	messagebox.showinfo("고양이 버튼", "고양이가 귀엽죠?")

# 메인 코드 부분
window = Tk()

photo = PhotoImage(file = "cat3.png");
button1 = Button(window, image = photo, command = myFunc)

button1.pack()

window.mainloop()
