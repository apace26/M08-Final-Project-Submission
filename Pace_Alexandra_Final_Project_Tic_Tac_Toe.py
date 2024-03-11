"""
Program: Pace_Alexandra_Final_Project_Tic_Tac_Toe.py
Author: Alexandra Pace
Date: 2/27/2024
Classic Tic-Tac-Toe game
Allows user input through cursor movement and clicking buttons
User selects x or o then chooses where to make their mark
Engages in taking turns with computer
Three marks in a row results in a winner
Winning mark (x/o) displayed through message box as output
"""

import tkinter as tk    # import modules and functions
from tkinter import *
from tkinter import messagebox
import random

window = tk.Tk()    # create window for widgets
window.title('Tic Tac Toe') # create title
window.geometry('800x450')  # set window width and height
window.resizable(False, False)  # keep window at fixed width and height

bg = PhotoImage(file='images/tic_tac_toe_background_800x450.png')   # store background image in variable

my_canvas = Canvas(window, width=800, height=450, borderwidth=0, highlightthickness=0)  # set up canvas
my_canvas.pack()

my_canvas.create_image(0,0, image=bg, anchor="nw")  # display background image on canvas

# function that allows x/o buttons to be placed in grid
# sets x counter variables to 1
# allows show() functions to restrict user selection to x marks
def select_x1():
    global x_counter1   # sets x counter to a global variable to alter same variable name outside of function
    x_counter1 = 1  # changes x counter variable to hold a value of 1
    x_o_1_button.place(x=260, y=80) # place x/o button in grid - changes coordinates
    global x_counter2
    x_counter2 = 1
    x_o_2_button.place(x=367, y=80)
    global x_counter3
    x_counter3 = 1
    x_o_3_button.place(x=473, y=80)
    global x_counter4
    x_counter4 = 1
    x_o_4_button.place(x=260, y=187)
    global x_counter5
    x_counter5 = 1
    x_o_5_button.place(x=367, y=187)
    global x_counter6
    x_counter6 = 1
    x_o_6_button.place(x=473, y=187)
    global x_counter7
    x_counter7 = 1
    x_o_7_button.place(x=260, y=298)
    global x_counter8
    x_counter8 = 1
    x_o_8_button.place(x=367, y=298)
    global x_counter9
    x_counter9 = 1
    x_o_9_button.place(x=473, y=298)
    x_button['state'] = 'disabled'  # disable x selection button
    o_button['state'] = 'disabled'  # disable o selection button

x_button = Button(window, text='X', width=7, height=2, bg='#ffffff', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=select_x1)    # create x selection button
x_button.place(x=600, y=80)

# function that allows x/o buttons to be placed in grid
# allows show() functions to restrict user selection to o marks
def select_o1():
    x_o_1_button.place(x=260, y=80) # place x/o button in grid - changes coordinates
    x_o_2_button.place(x=367, y=80)
    x_o_3_button.place(x=473, y=80)
    x_o_4_button.place(x=260, y=187)
    x_o_5_button.place(x=367, y=187)
    x_o_6_button.place(x=473, y=187)
    x_o_7_button.place(x=260, y=298)
    x_o_8_button.place(x=367, y=298)
    x_o_9_button.place(x=473, y=298)
    x_button['state'] = 'disabled'  # disable x selection button
    o_button['state'] = 'disabled'  # disable o selection button

o_button = Button(window, text='O', width=7, height=2, bg='#ffffff', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=select_o1)    # create o selection button
o_button.place(x=600, y=200)

# function that allows user to exit out of window
def exit_funct():
    window.destroy()

exit_button = Button(window, text='Exit', width=7, height=2, bg='#ffffff', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=exit_funct)    # create exit button
exit_button.place(x=600, y=320)

# disable these x_o buttons on grid
def disable_selection():
    global x_o_1_button
    x_o_1_button.place_forget()
    global x_o_2_button
    x_o_2_button.place_forget()
    global x_o_3_button
    x_o_3_button.place_forget()
    global x_o_4_button
    x_o_4_button.place_forget()
    global x_o_5_button
    x_o_5_button.place_forget()
    global x_o_6_button
    x_o_6_button.place_forget()
    global x_o_7_button
    x_o_7_button.place_forget()
    global x_o_8_button
    x_o_8_button.place_forget()
    global x_o_9_button
    x_o_9_button.place_forget()

# enables buttons x/o buttons to place on grid
def enable():
    x_o_1_button.place(x=260, y=80)
    x_o_2_button.place(x=367, y=80)
    x_o_3_button.place(x=473, y=80)
    x_o_4_button.place(x=260, y=187)
    x_o_5_button.place(x=367, y=187)
    x_o_6_button.place(x=473, y=187)
    x_o_7_button.place(x=260, y=298)
    x_o_8_button.place(x=367, y=298)
    x_o_9_button.place(x=473, y=298)

# simulates the computer selecting a place on the grid to mark
def computer_selection():
    if x_counter1 == 1 or x_counter2 == 1 or x_counter3 == 1 or x_counter4 == 1 or x_counter5 == 1 or x_counter6 == 1 or x_counter7 == 1 or x_counter8 == 1 or x_counter9 == 1: # determines whether to place x or o mark
        global list_x
        if len(list_x) == 0: # checks if list is empty
            pass
        else:
            random.choice(list_x)() # randomly selects position for o on grid
    else:
        global list_o
        if len(list_o) == 0:
            pass
        else:
            random.choice(list_o)() # randomly selects position for x on grid
    
    # checks if three marks of x or o are in row/column/diagonally
    if winX1 == 1 and winX2 == 1 and winX3 == 1:
        messagebox.showinfo("Message", "X has won!") # messagebox alerts user whether x or o has won
        disable_selection() # disables x/o buttons
    elif winX4 == 1 and winX5 == 1 and winX6 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX7 == 1 and winX8 == 1 and winX9 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX1 == 1 and winX4 == 1 and winX7 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX2 == 1 and winX5 == 1 and winX8 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX3 == 1 and winX6 == 1 and winX9 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX1 == 1 and winX5 == 1 and winX9 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    elif winX3 == 1 and winX5 == 1 and winX7 == 1:
        messagebox.showinfo("Message", "X has won!")
        disable_selection()
    else:
        if winO1 == 1 and winO2 == 1 and winO3 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO4 == 1 and winO5 == 1 and winO6 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO7 == 1 and winO8 == 1 and winO9 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO1 == 1 and winO4 == 1 and winO7 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO2 == 1 and winO5 == 1 and winO8 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO3 == 1 and winO6 == 1 and winO9 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO1 == 1 and winO5 == 1 and winO9 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()
        elif winO3 == 1 and winO5 == 1 and winO7 == 1:
            messagebox.showinfo("Message", "O has won!")
            disable_selection()

# random function that was selected by the computer
def rand1():
    x_img_Label1.place(x=260, y=80) # displays x image
    global list_x
    list_x.remove(rand2)    # random functions for x and o removed from list so they are not called again
    list_o.remove(rand1)
    global winX1
    winX1 = 1   # keeps track of whether x or o wins

def rand2():
    o_img_Label1.place(x=260, y=80)
    global list_x
    list_x.remove(rand2)
    list_o.remove(rand1)
    global winO1
    winO1 = 1

def rand3():
    x_img_Label2.place(x=367, y=80)
    global list_x
    list_x.remove(rand4)
    list_o.remove(rand3)
    global winX2
    winX2 = 1

def rand4():
    o_img_Label2.place(x=367, y=80)
    global list_x
    list_x.remove(rand4)
    list_o.remove(rand3)
    global winO2
    winO2 = 1

def rand5():
    x_img_Label3.place(x=473, y=80)
    global list_x
    list_x.remove(rand6)
    list_o.remove(rand5)
    global winX3
    winX3 = 1

def rand6():
    o_img_Label3.place(x=473, y=80)
    global list_x
    list_x.remove(rand6)
    list_o.remove(rand5)
    global winO3
    winO3 = 1

def rand7():
    x_img_Label4.place(x=260, y=190)
    global list_x
    list_x.remove(rand8)
    list_o.remove(rand7)
    global winX4
    winX4 = 1

def rand8():
    o_img_Label4.place(x=260, y=190)
    global list_x
    list_x.remove(rand8)
    list_o.remove(rand7)
    global winO4
    winO4 = 1

def rand9():
    x_img_Label5.place(x=367, y=187)
    global list_x
    list_x.remove(rand10)
    list_o.remove(rand9)
    global winX5
    winX5 = 1

def rand10():
    o_img_Label5.place(x=367, y=187)
    global list_x
    list_x.remove(rand10)
    list_o.remove(rand9)
    global winO5
    winO5 = 1

def rand11():
    x_img_Label6.place(x=473, y=187)
    global list_x
    list_x.remove(rand12)
    list_o.remove(rand11)
    global winX6
    winX6 = 1

def rand12():
    o_img_Label6.place(x=473, y=187)
    global list_x
    list_x.remove(rand12)
    list_o.remove(rand11)
    global winO6
    winO6 = 1

def rand13():
    x_img_Label7.place(x=260, y=298)
    global list_x
    list_x.remove(rand14)
    list_o.remove(rand13)
    global winX7
    winX7 = 1

def rand14():
    o_img_Label7.place(x=260, y=298)
    global list_x
    list_x.remove(rand14)
    list_o.remove(rand13)
    global winO7
    winO7 = 1

def rand15():
    x_img_Label8.place(x=367, y=298)
    global list_x
    list_x.remove(rand16)
    list_o.remove(rand15)
    global winX8
    winX8 = 1

def rand16():
    o_img_Label8.place(x=367, y=298)
    global list_x
    list_x.remove(rand16)
    list_o.remove(rand15)
    global winO8
    winO8 = 1

def rand17():
    x_img_Label9.place(x=473, y=298)
    global list_x
    list_x.remove(rand18)
    list_o.remove(rand17)
    global winX9
    winX9 = 1

def rand18():
    o_img_Label9.place(x=473, y=298)
    global list_x
    list_x.remove(rand18)
    list_o.remove(rand17)
    global winO9
    winO9 = 1

# initialize x counters to 0
x_counter1 = 0
x_counter2 = 0
x_counter3 = 0
x_counter4 = 0
x_counter5 = 0
x_counter6 = 0
x_counter7 = 0
x_counter8 = 0
x_counter9 = 0

# initialize x winning letter to 0
winX1 = 0
winX2 = 0
winX3 = 0
winX4 = 0
winX5 = 0
winX6 = 0
winX7 = 0
winX8 = 0
winX9 = 0

# initialize x winning letter to 0
winO1 = 0
winO2 = 0
winO3 = 0
winO4 = 0
winO5 = 0
winO6 = 0
winO7 = 0
winO8 = 0
winO9 = 0

list_x = [rand2, rand4, rand6, rand8, rand10, rand12, rand14, rand16, rand18]   # creates list that contains random functions that will run when user is x
list_o = [rand1, rand3, rand5, rand7, rand9, rand11, rand13, rand15, rand17]    # creates list that contains random functions that will run when user is o

# functions to determine whether to show x or o
def show_1():
    global winX1
    global winO1
    if x_counter1 == 1: # checks if x button was selected
        x_img_Label1.place(x=260, y=80) # places x on grid
        winX1 = 1   # keeps track of x marks to determine winner
    else:   # checks if o button was selected
        o_img_Label1.place(x=260, y=80) # places o on grid
        winO1 = 1 # keeps track of o marks to determine winner
    disable_selection() # disables x/o buttons
    global list_x
    list_x.remove(rand2)    # random functions removed from list
    list_o.remove(rand1)
    window.after(1000, computer_selection) # after 1 second allow computer to randomly select its place on grid
    window.after(1000, enable)  # enable x/o butons again on grid after machine selects its position

def show_2():
    global winX2
    global winO2
    if x_counter2 == 1:
        x_img_Label2.place(x=367, y=80)
        winX2 = 1
    else:
        o_img_Label2.place(x=367, y=80)
        winO2 = 1
    disable_selection()
    global list_x
    list_x.remove(rand4)
    list_o.remove(rand3)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_3():
    global winX3
    global winO3
    if x_counter3 == 1:
        x_img_Label3.place(x=473, y=80)
        winX3 = 1
    else:
        o_img_Label3.place(x=473, y=80)
        winO3 = 1
    disable_selection()
    global list_x
    list_x.remove(rand6)
    list_o.remove(rand5)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_4():
    global winX4
    global winO4
    if x_counter4 == 1:
        x_img_Label4.place(x=260, y=190)
        winX4 = 1
    else:
        o_img_Label4.place(x=260, y=190)
        winO4 = 1
    disable_selection()
    global list_x
    list_x.remove(rand8)
    list_o.remove(rand7)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_5():
    global winX5
    global winO5
    if x_counter5 == 1:
        x_img_Label5.place(x=367, y=187)
        winX5 = 1
    else:
        o_img_Label5.place(x=367, y=187)
        winO5 = 1
    disable_selection()
    global list_x
    list_x.remove(rand10)
    list_o.remove(rand9)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_6():
    global winX6
    global winO6
    if x_counter6 == 1:
        x_img_Label6.place(x=473, y=187)
        winX6 = 1
    else:
        o_img_Label6.place(x=473, y=187)
        winO6 = 1
    disable_selection()
    global list_x
    list_x.remove(rand12)
    list_o.remove(rand11)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_7():
    global winX7
    global winO7
    if x_counter7 == 1:
        x_img_Label7.place(x=260, y=298)
        winX7 = 1
    else:
        o_img_Label7.place(x=260, y=298)
        winO7 = 1
    disable_selection()
    global list_x
    list_x.remove(rand14)
    list_o.remove(rand13)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_8():
    global winX8
    global winO8
    if x_counter8 == 1:
        x_img_Label8.place(x=367, y=298)
        winX8 = 1
    else:
        o_img_Label8.place(x=367, y=298)
        winO8 = 1
    disable_selection()
    global list_x
    list_x.remove(rand16)
    list_o.remove(rand15)
    window.after(1000, computer_selection)
    window.after(1000, enable)

def show_9():
    global winX9
    global winO9
    if x_counter9 == 1:
        x_img_Label9.place(x=473, y=298)
        winX9 = 1
    else:
        o_img_Label9.place(x=473, y=298)
        winO9 = 1
    disable_selection()
    global list_x
    list_x.remove(rand18)
    list_o.remove(rand17)
    window.after(1000, computer_selection)
    window.after(1000, enable)

# create x/o buttons for grid
x_o_1_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_1)
x_o_1_button.place_forget()

x_o_2_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_2)
x_o_2_button.place_forget()

x_o_3_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_3)
x_o_3_button.place_forget()

x_o_4_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_4)
x_o_4_button.place_forget()

x_o_5_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_5)
x_o_5_button.place_forget()

x_o_6_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_6)    
x_o_6_button.place_forget()

x_o_7_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_7)
x_o_7_button.place_forget()

x_o_8_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_8)
x_o_8_button.place_forget()

x_o_9_button = Button(window, width=9, height=4, bg='#1f1f1f', activebackground='#1f1f1f', borderwidth=0, highlightthickness=0, cursor='hand2', command=show_9)
x_o_9_button.place_forget()

x_image1 = PhotoImage(file='images/x_1_67x72.png')  # store column 1/row 1 x_image1 in variable
x_img_Label1 = tk.Label(window, image=x_image1, borderwidth=0, highlightthickness=0)    # display x_image1 in column 1/row 1 of grid
x_img_Label1.place_forget()

o_image1 = PhotoImage(file='images/o_1_67x72.png')  # store column 1/row 1 o_image1 in variable
o_img_Label1 = tk.Label(window, image=o_image1, borderwidth=0, highlightthickness=0)    # display o_image1 in column 1/row 1 of grid
o_img_Label1.place_forget()

x_image2 = PhotoImage(file='images/x_2_67x72.png')  # store column 2/row 1 x_image2 in variable
x_img_Label2 = tk.Label(window, image=x_image2, borderwidth=0, highlightthickness=0)    # display x_image2 in column 2/row 1 of grid
x_img_Label2.place_forget()

o_image2 = PhotoImage(file='images/o_2_67x72.png')  # store column 2/row 1 o_image2 in variable
o_img_Label2 = tk.Label(window, image=o_image2, borderwidth=0, highlightthickness=0)    # display o_image2 in column 2/row 1 of grid
o_img_Label2.place_forget()

x_image3 = PhotoImage(file='images/x_3_67x72.png')  # store column 3/row 1 x_image3 in variable
x_img_Label3 = tk.Label(window, image=x_image3, borderwidth=0, highlightthickness=0)    # display x_image3 in column 3/row 1 of grid
x_img_Label3.place_forget()

o_image3 = PhotoImage(file='images/o_3_67x72.png')  # store column 3/row 1 o_image3 in variable
o_img_Label3 = tk.Label(window, image=o_image3, borderwidth=0, highlightthickness=0)    # display o_image3 in column 3/row 1 of grid
o_img_Label3.place_forget()

x_image4 = PhotoImage(file='images/x_4_67x72.png')  # store column 1/row 2 x_image4 in variable
x_img_Label4 = tk.Label(window, image=x_image4, borderwidth=0, highlightthickness=0)    # display x_image4 in column 1/row 2 of grid
x_img_Label4.place_forget()

o_image4 = PhotoImage(file='images/o_4_67x72.png')  # store column 1/row 2 o_image4 in variable
o_img_Label4 = tk.Label(window, image=o_image4, borderwidth=0, highlightthickness=0)    # display o_image4 in column 1/row 2 of grid
o_img_Label4.place_forget()

x_image5 = PhotoImage(file='images/x_5_67x72.png')  # store column 2/row 2 x_image5 in variable
x_img_Label5 = tk.Label(window, image=x_image5, borderwidth=0, highlightthickness=0)    # display x_image5 in column 2/row 2 of grid
x_img_Label5.place_forget()

o_image5 = PhotoImage(file='images/o_5_67x72.png')  # store column 2/row 2 o_image5 in variable
o_img_Label5 = tk.Label(window, image=o_image5, borderwidth=0, highlightthickness=0)    # display o_image5 in column 2/row 2 of grid
o_img_Label5.place_forget()

x_image6 = PhotoImage(file='images/x_6_67x72.png')  # store column 3/row 2 x_image6 in variable
x_img_Label6 = tk.Label(window, image=x_image6, borderwidth=0, highlightthickness=0)    # display x_image6 in column 3/row 2 of grid
x_img_Label6.place_forget()

o_image6 = PhotoImage(file='images/o_6_67x72.png')  # store column 3/row 2 o_image6 in variable
o_img_Label6 = tk.Label(window, image=o_image6, borderwidth=0, highlightthickness=0)    # display o_image6 in column 3/row 2 of grid
o_img_Label6.place_forget()

x_image7 = PhotoImage(file='images/x_7_67x72.png')  # store column 1/row 3 x_image7 in variable
x_img_Label7 = tk.Label(window, image=x_image7, borderwidth=0, highlightthickness=0)    # display x_image7 in column 1/row 3 of grid
x_img_Label7.place_forget()

o_image7 = PhotoImage(file='images/o_7_67x72.png')  # store column 1/row 3 o_image7 in variable
o_img_Label7 = tk.Label(window, image=o_image7, borderwidth=0, highlightthickness=0)  # display o_image7 in column 1/row 3 of grid  
o_img_Label7.place_forget()

x_image8 = PhotoImage(file='images/x_8_67x72.png')  # store column 2/row 3 x_image8 in variable
x_img_Label8 = tk.Label(window, image=x_image8, borderwidth=0, highlightthickness=0)    # display x_image8 in column 2/row 3 of grid
x_img_Label8.place()

o_image8 = PhotoImage(file='images/o_8_67x72.png')  # store column 2/row 3 o_image8 in variable
o_img_Label8 = tk.Label(window, image=o_image8, borderwidth=0, highlightthickness=0)    # display o_image8 in column 2/row 3 of grid
o_img_Label8.place_forget()

x_image9 = PhotoImage(file='images/x_9_67x72.png')  # store column 3/row 3 x_image9 in variable
x_img_Label9 = tk.Label(window, image=x_image9, borderwidth=0, highlightthickness=0)    # display x_image9 in column 3/row 3 of grid
x_img_Label9.place_forget()

o_image9 = PhotoImage(file='images/o_9_67x72.png')  # store column 3/row 3 o_image9 in variable
o_img_Label9 = tk.Label(window, image=o_image9, borderwidth=0, highlightthickness=0)    # display o_image9 in column 3/row 3 of grid
o_img_Label9.place_forget()

window.mainloop()   # execute mainloop()