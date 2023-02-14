import time
import random
from select import select
from tkinter import *
from turtle import back
import tkinter.font as tkFont

running = True

clicked_speed = 2000

def set_speed(set):
    global clicked_speed
    quiz_speed = int(clicked.get())
    match quiz_speed:
        case 1:
            conc_z = 999
            clicked_speed = quiz_speed + conc_z
            return clicked_speed
        case 2:
            conc_z = 1998
            clicked_speed = quiz_speed + conc_z
            return clicked_speed
        case 3:
            conc_z = 2997
            clicked_speed = quiz_speed + conc_z
            return clicked_speed
        
def practice_key_of_c():
    c = ["C","Dm","Em","F","G","Am"]
    if running:
        list1.insert(END, random.choice(c))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_c)

def practice_key_of_d():
    d = ["D","Em","F#m","G","A","Bm"]
    if running:
        list1.insert(END, random.choice(d))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_d)      

def practice_key_of_e():
    e = ["E","F#m","G#m","A","B","C#m"]
    if running:
        list1.insert(END, random.choice(e))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_e)

def practice_key_of_f():
    f = ["F","Gm","Am","Bb","C","Dm"]
    if running:
        list1.insert(END, random.choice(f))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_f)

def practice_key_of_g():
    g = ["G","Am","Bm","C","D","Em"]
    if running:
        list1.insert(END, random.choice(g))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_g)

def practice_key_of_a():
    a = ["A","Bm","C#m","D","E","F#m"]
    if running:
        list1.insert(END, random.choice(a))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_a)

def practice_key_of_b():
    b = ["G","Am","Bm","C","D","Em"]
    if running:
        list1.insert(END, random.choice(b))
        list1.see(END)
        window.after(clicked_speed, practice_key_of_b)

def stop_quiz():
    global running
    running = False

def start_quiz():
    global running
    running = True

def delete():
    list1.delete(0, END)

def on_enter(e):
    b11['background'] = 'black'

def on_leave(e):
    b11['background'] = 'black'

window = Tk()
window.geometry("480x150")
window['bg'] = 'black'

large_font = tkFont.Font(size = 83)
list1 = Listbox(window, height = 1, width = 4, font = large_font, bg="black", fg='white')
list1.grid(row = 2, column = 0, rowspan = 9, columnspan = 1)
scrollbar = Scrollbar(window)
list1.config(yscrollcommand = scrollbar.set)

b1 = Button(window, text="key of c", width = 14, command=practice_key_of_c, bg="black", fg='white').grid(row = 2, column = 3)
b2 = Button(window, text="key of d", width = 14, command=practice_key_of_d, bg="black", fg='white').grid(row = 3, column = 3)
b3 = Button(window, text="key of e", width = 14, command=practice_key_of_e, bg="black", fg='white').grid(row = 4, column = 3)
b4 = Button(window, text="key of f", width = 14, command=practice_key_of_f, bg="black", fg='white').grid(row = 5, column = 3)
b5 = Button(window, text="key of g", width = 14, command=practice_key_of_g, bg="black", fg='white').grid(row = 6, column = 3)
b6 = Button(window, text="key of a", width = 14, command=practice_key_of_a, bg="black", fg='white').grid(row = 2, column = 4)
b7 = Button(window, text="key of b", width = 14, command=practice_key_of_b, bg="black", fg='white').grid(row = 3, column = 4)
b10 = Button(window, text="start", width = 14, command=start_quiz, bg="black", fg='green').grid(row = 4, column = 4)
b8 = Button(window, text="stop", width = 14, command=stop_quiz, bg="black", fg='red').grid(row = 5, column = 4)
b9 = Button(window, text="clear", width = 14, command=delete, bg="black", fg='white').grid(row = 6, column = 4)

options = [1, 2, 3]

clicked = StringVar()
clicked.set("select speed")

b11 = OptionMenu(window, clicked, *options, command = set_speed)
b11.grid(row = 6, column = 4)
b11.config(bg='black', fg='white', activebackground='black', activeforeground='white')
b11.bind('<Enter>', on_enter)
b11.bind('<Leave>', on_leave)

window.wm_title("guitar quiz")
window.mainloop()