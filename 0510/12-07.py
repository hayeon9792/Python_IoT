from tkinter import *
window = Tk()
window.title("제주도")

count = 0
photo_list = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif", 
	      "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif", "jeju10.gif", 
	      "jeju11.gif", "jeju12.gif", "jeju13.gif", "jeju14.gif"]

def myFunc() :
	global count
	if (count>13) :
		count = 0
	else :
		count += 1
	photo = PhotoImage(file = "GIF/" + photo_list[count])
	label1.configure(image = photo)
	label1.photo = photo

photo1 = PhotoImage(file = "GIF/" + photo_list[count])
label1 = Label(window, image = photo1)

label1.pack()

button1 = Button(window, text="사진 변경", command = myFunc)

button1.pack()

window.mainloop()