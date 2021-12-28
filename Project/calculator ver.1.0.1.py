import tkinter as tk
from tkinter import messagebox
from tkinter import *


window = tk.Tk()
window.geometry('401x572')
window.title("เครื่องคิดเลขอัจฉริยะ รุ่น ver. 1.0.1")

number = 0
equal = 0

def selection():
    choice = var.get()
    if choice == 1:
        lbl_Basehead.configure(text="คำนวณเลขฐาน 2")
    
    elif choice == 2:

        lbl_Basehead.configure(text="คำนวณเลขฐาน 8")
    elif choice == 3:

        lbl_Basehead.configure(text="คำนวณเลขฐาน 10")
    elif choice == 4:

        lbl_Basehead.configure(text="คำนวณเลขฐาน 16")

def btn_plus_clicked():
    global equal
    number = int(number_input.get())
    equal = equal + number
    number_2.config(text=bin(equal))
    print(equal)
    number_8.config(text=oct(equal))
    print(equal)
    number_10.config(text=(equal))
    print(equal)
    number_16.config(text=hex(equal))
    print(equal)
    number_input.delete(0, 'end')

def btn_minus_clicked():
    global equal
    number = int(number_input.get())
    equal = equal - number
    number_2.config(text=bin(equal))
    print(equal)
    number_8.config(text=oct(equal))
    print(equal)
    number_10.config(text=equal)
    print(equal)
    number_16.config(text=hex(equal))
    print(equal)
    number_input.delete(0, 'end')

def btn_mutiply_clicked():
    global equal
    number = int(number_input.get())
    equal = equal * number
    number_2.config(text=bin(equal))
    print(equal)
    number_8.config(text=oct(equal))
    print(equal)
    number_10.config(text=equal)
    print(equal)
    number_16.config(text=hex(equal))
    print(equal)
    number_input.delete(0, 'end')

def btn_equal_clicked():
    global equal
    number = int(number_input.get())
    number_2.config(text=bin(number))
    print(number)
    number_8.config(text=oct(number))
    print(number)
    number_10.config(text=number)
    print(number)
    number_16.config(text=hex(number))
    print(number)

def btn_clear_clicked():
    global equal
    equal = 0
    number_2.config(text=bin(equal))
    print(equal)
    number_8.config(text=oct(equal))
    print(equal)
    number_10.config(text=equal)
    print(equal)
    number_16.config(text=hex(equal))
    print(equal)
    number_input.delete(0, 'end')

var = IntVar()
btn_2 = tk.Radiobutton(window,text="ฐาน 2",variable=var, value=1,command=selection)
btn_2.place(x=20,y=70,width=70,height=25)

btn_8 = tk.Radiobutton(window,text="ฐาน 8",variable=var, value=2,command=selection)
btn_8.place(x=110,y=70,width=70,height=25)

btn_10 = tk.Radiobutton(window,text="ฐาน 10",variable=var, value=3,command=selection)
btn_10.place(x=200,y=70,width=70,height=25)

btn_16 = tk.Radiobutton(window,text="ฐาน 16",variable=var, value=4,command=selection)
btn_16.place(x=290,y=70,width=70,height=25)

lbl_Head = tk.Label(window,text="โปรแกรมอัจฉริยะ ver. 1.0.1")
lbl_Head.place(x=110,y=20,width=158,height=30)

lbl_Basehead = tk.Label(window,text="คำนวณเลขฐาน ...")
lbl_Basehead.place(x=120,y=130,width=144,height=30)

number_input = tk.Entry(window,text="ใส่เลข")
number_input.place(x=20,y=170,width=340,height=32)

btn_plus = tk.Button(window,text="+",command=btn_plus_clicked)
btn_plus.place(x=20,y=230,width=70,height=25)

btn_minus = tk.Button(window,text="-",command=btn_minus_clicked)
btn_minus.place(x=110,y=230,width=70,height=25)

btn_mutiply = tk.Button(window,text="x",command=btn_mutiply_clicked)
btn_mutiply.place(x=200,y=230,width=70,height=25)

btn_mutiply = tk.Button(window,text="=",command=btn_equal_clicked)
btn_mutiply.place(x=300,y=230,width=70,height=25)

btn_clear = tk.Button(window,text="CE",command=btn_clear_clicked)
btn_clear.place(x=20,y=290,width=343,height=30)

lbl_Equalhead = tk.Label(window,text="ผลลัพธ์")
lbl_Equalhead.place(x=20,y=340,width=339,height=30)

lbl_2 = tk.Label(window,text="ฐาน 2")
lbl_2.place(x=20,y=380,width=70,height=25)

lbl_8 = tk.Label(window,text="ฐาน 8")
lbl_8.place(x=110,y=380,width=70,height=25)

lbl_10 = tk.Label(window,text="ฐาน 10")
lbl_10.place(x=200,y=380,width=70,height=25)

lbl_16 = tk.Label(window,text="ฐาน 16")
lbl_16.place(x=290,y=380,width=70,height=25)

number_2 = tk.Label(window,text="ผลลัพธ์ 2")
number_2.place(x=20,y=430,width=75,height=30)

number_8 = tk.Label(window,text="ผลลัพธ์ 8")
number_8.place(x=110,y=430,width=70,height=25)

number_10 = tk.Label(window,text="ผลลัพธ์ 10")
number_10.place(x=200,y=430,width=77,height=30)

number_16 = tk.Label(window,text="ผลลัพธ์ 16")
number_16.place(x=290,y=430,width=83,height=30)

window.mainloop()