from tkinter import *


window = Tk()
window.geometry("300x350")



def color_change(number):
    print(number)


def sim_ver2():

    x1 = float(entryx.get())
    y1 = float(entryy.get())
    c1 = float(entry_equal.get())

    x2 = float(entryx2.get())
    y2 = float(entryy2.get())
    c2 = float(entry_equal2.get())

    # Using Cramer's rule:
    # The coefficient matrix is D
    D = (x1 * y2) - (x2 * y1)

    # x-Matrix is defined as Dx
    Dx = (c1 * y2) - (c2 * y1)

    # y-Matrix is defined as Dy
    Dy = (x1 * c2) - (x2 * c1)

    # Value of x
    X = Dx / D

    # Value of y
    Y = Dy / D

    entry_value_x.insert(0, X)
    entry_value_y.insert(0, Y)

def but_click(number):
    current1 = entryx.get()
    entryx.delete(0, END)
    entryx.insert(0, str(current1) + str(number))

def but_click_2(number):
    current1 = entryy.get()
    entryy.delete(0, END)
    entryy.insert(0, str(current1) + str(number))
    entryy.config(bg='red')

def but_click_3(number):
    current1 = entry_equal.get()
    entry_equal.delete(0, END)
    entry_equal.insert(0, str(current1) + str(number))

def but_click_4(number):
    current1 = entryx2.get()
    entryx2.delete(0, END)
    entryx2.insert(0, str(current1) + str(number))

def but_click_5(number):
    current1 = entryy2.get()
    entryy2.delete(0, END)
    entryy2.insert(0, str(current1) + str(number))

def but_click_6(number):
    current1 = entry_equal2.get()
    entry_equal2.delete(0, END)
    entry_equal2.insert(0, str(current1) + str(number))


def next(number):

    b1.config(command=lambda: buttom_list[number](1))
    b2.config(command=lambda: buttom_list[number](2))
    b3.config(command=lambda: buttom_list[number](3))

    b4.config(command=lambda: buttom_list[number](4))
    b5.config(command=lambda: buttom_list[number](5))
    b6.config(command=lambda: buttom_list[number](6))

    b7.config(command=lambda: buttom_list[number](7))
    b8.config(command=lambda: buttom_list[number](8))
    b9.config(command=lambda: buttom_list[number](9))

    b0.config(command=lambda: buttom_list[number](0))
    b_dot.config(command=lambda: buttom_list[number]('.'))
    b_minus.config(command=lambda: buttom_list[number]('-'))

    b_next = Button(window, text='>>', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=lambda: next(number + 1))
    b_next.place(y=150, x=45)

    b_back = Button(window, text='<<', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=lambda: next(number - 1))
    b_back.place(y=150)

    if number == 5:
        b_next = Button(window, text='>>', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), state=DISABLED)
        b_next.place(y=150, x=45)

def back(number):

    b1.config(command=lambda: buttom_list[number](1))
    b2.config(command=lambda: buttom_list[number](2))
    b3.config(command=lambda: buttom_list[number](3))

    b4.config(command=lambda: buttom_list[number](4))
    b5.config(command=lambda: buttom_list[number](5))
    b6.config(command=lambda: buttom_list[number](6))

    b7.config(command=lambda: buttom_list[number](7))
    b8.config(command=lambda: buttom_list[number](8))
    b9.config(command=lambda: buttom_list[number](9))

    b0.config(command=lambda: buttom_list[number](0))
    b_dot.config(command=lambda: buttom_list[number]('.'))
    b_minus.config(command=lambda: buttom_list[number]('-'))

    b_next = Button(window, text='>>', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=lambda: next(number + 1))
    b_next.place(y=150, x=45)

    b_back = Button(window, text='<<', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=lambda: next(number - 1))
    b_back.place(y=150)



    if number == 0:
        b_back = Button(window, text='<<', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), state=DISABLED)
        b_back.place(y=150)


def clear():
    entryx.delete(0, END)
    entryy.delete(0, END)
    entry_equal.delete(0, END)

    entryx2.delete(0, END)
    entryy2.delete(0, END)
    entry_equal2.delete(0, END)

    entry_value_x.delete(0, END)
    entry_value_y.delete(0, END)


# Defining labels
lab_main = Label(window, text='Sim Equations', font=('arial black', 16, 'bold'), relief='solid', bg='red')

# Equation 1
labx1 = Label(window, text='x', font=('bold', 12))
laby1 = Label(window, text='y', font=('bold', 12))
lab_equal1 = Label(window, text='=', font=('bold', 12))

# Equation 2
labx2 = Label(window, text='x', font=('bold', 12))
laby2 = Label(window, text='y', font=('bold', 12))
lab_equal2 = Label(window, text='=', font=('bold', 12))

# Answers
labx3 = Label(window, text='x', font=('bold', 12))
laby3 = Label(window, text='y', font=('bold', 12))

# Defining entry boxes

entryx = Entry(window, width=10, borderwidth=5)
entryy = Entry(window, width=10, borderwidth=5)
entry_equal = Entry(window, width=10, borderwidth=5)

entryx2 = Entry(window, width=10, borderwidth=5)
entryy2 = Entry(window, width=10, borderwidth=5)
entry_equal2 = Entry(window, width=10, borderwidth=5)

entry_value_x = Entry(window, width=8, borderwidth=5)
entry_value_y = Entry(window, width=8, borderwidth=5)

# Defining the buttons

b1 = Button(window, text='1', width=5, padx=10, pady=5, bg='red', font=('bold', 12), command=lambda: but_click(1))
b2 = Button(window, text='2', width=5, padx=10, pady=5, bg='yellow', font=('bold', 12), command=lambda: but_click(2))
b3 = Button(window, text='3', width=5, padx=10, pady=5, bg='red', font=('bold', 12), command=lambda: but_click(3))

b4 = Button(window, text='4', width=5, padx=10, pady=5, bg='light green', font=('bold', 12), command=lambda: but_click(4))
b5 = Button(window, text='5', width=5, padx=10, pady=5, bg='green', font=('bold', 12), command=lambda: but_click(5))
b6 = Button(window, text='6', width=5, padx=10, pady=5, bg='light green', font=('bold', 12), command=lambda: but_click(6))

b7 = Button(window, text='7', width=5, padx=10, pady=5, bg='aqua', font=('bold', 12), command=lambda: but_click(7))
b8 = Button(window, text='8', width=5, padx=10, pady=5, bg='white', font=('bold', 12), command=lambda: but_click(8))
b9 = Button(window, text='9', width=5, padx=10, pady=5, bg='aqua', font=('bold', 12), command=lambda: but_click(9))
b0 = Button(window, text='0', width=5, padx=20, pady=6, bg='black', fg='white', font=('bold', 12), command=lambda: but_click(0))

b_dot = Button(window, text='.', width=3, padx=10, pady=5, bg='white', font=('bold', 16), command=lambda: but_click('.'))
b_minus = Button(window, text='-', width=3, padx=10, pady=5, bg='blue', font=('bold', 16), command=lambda: but_click('-'))

b_solve = Button(window, text='Solve', width=5, padx=1, pady=1, bg='black', fg='white', font=("arial black", 16, 'bold'), command=lambda: sim_ver2())
b_clear = Button(window, text='clear', width=5, padx=10, pady=1, bg='red', font=('bold', 14), command=lambda: clear())
b_next = Button(window, text='>>', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=(lambda: next(0)))
b_back = Button(window, text='<<', width=3, padx=5, pady=0, bg='yellow', font=('bold', 13), command=lambda: back(0))

buttom_list =[but_click, but_click_2, but_click_3, but_click_4, but_click_5, but_click_6]
entry_list =[entryx, entryy, entryx2, entryy2, entry_equal, entry_equal2]


# Placing of Lab_main
lab_main.place(x=60)
labx1.place(y=60, x=80)
laby1.place(y=60, x=175)
lab_equal1.place(y=60, x=200)

labx2.place(y=120, x=80)
laby2.place(y=120, x=175)
lab_equal2.place(y=120, x=200)

labx3.place(y=160, x=259)
laby3.place(y=220, x=255)

# Placing entry boxes
entryx.place(y=60, x=5)
entryy.place(y=60, x=100)
entry_equal.place(y=60, x=226)

entryx2.place(y=120, x=5)
entryy2.place(y=120, x=100)
entry_equal2.place(y=120, x=226)

entry_value_x.place(y=180, x=235)
entry_value_y.place(y=243, x=235)
# Placing buttons on gui

b1.place(y=180)
b2.place(y=180, x=75)
b3.place(y=180, x=150)

b4.place(y=223)
b5.place(y=223, x=75)
b6.place(y=223, x=150)

b7.place(y=266)
b8.place(y=266, x=75)
b9.place(y=266, x=150)
b0.place(y=308)

b_dot.place(y=308, x=95)
b_minus.place(y=308, x=160)

b_solve.place(y=308, x=225)
b_clear.place(y=268, x=225)
b_next.place(y=150, x=45)
b_back.place(y=150)



window.mainloop()