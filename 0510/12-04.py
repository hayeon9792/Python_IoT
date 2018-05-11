from tkinter import *
window = Tk()

photo1 = PhotoImage(file = "cat2.gif")
label1 = Label(window, image = photo1)

photo2 = PhotoImage(file = "cat3.png")
label2 = Label(window, image = photo2)

photo3 = PhotoImage(file = "cat2.gif")
label3 = Label(window, image = photo3)

photo4 = PhotoImage(file = "cat3.png")
label4 = Label(window, image = photo4)


label1.pack(side = LEFT)
label2.pack(side = LEFT)
label3.pack(side = LEFT)
label4.pack(side = RIGHT)

window.mainloop()
