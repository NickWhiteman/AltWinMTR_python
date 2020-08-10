from tkinter import *
import os
import time
from contextlib import redirect_stdout
import io
import sys
import pyperclip

window = Tk()

def WinSize500():
    window.geometry('500x500')

def WinSize700():
    window.geometry('700x400')

def netw():
    return str(os.system('ping -c 4 ya.ru'))

def non1():
    return file_content.insert('end', f"\n {(print(func))}")

def joja():
    return 'jejejejejeje'

def ClearClicked():
    file_content.delete(1.0, END)

func = netw()
    
window.title('Alt_MTR')

frame = Frame()
frame_file_content = LabelFrame(text='Test_text')

file_name = Entry(frame, width='25')

button_ping = Button(frame, text='Ping', command=non1)
button_tracert = Button(frame, text='Tracert')
button_clear = Button(frame, text = 'Clear', command=ClearClicked)

# посидеть подумать еще немного насчет более простым методом вывода
file_content = Text(frame_file_content, bg='#FFFFE0', width='50', height='20', wrap = None)

#Разметка
Yscroll = Scrollbar(frame_file_content, command=file_content.yview)
Xscroll = Scrollbar(orient=HORIZONTAL, command=file_content.xview)

file_content.configure(yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set)

frame.pack()
file_name.pack(side=LEFT)
button_ping.pack(side=LEFT)
button_tracert.pack(side=LEFT)
button_clear.pack(side=LEFT)
frame_file_content.pack(fill=BOTH, expand=1)
file_content.pack(side=LEFT, fill=BOTH, expand=1)
Yscroll.pack(side=LEFT, fill=Y)
Xscroll.pack(side=BOTTOM, fill=X)

#menu
menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label="500x500", command=WinSize500)
new_item.add_command(label="700x400",command=WinSize700)
menu.add_cascade(label='Size', menu=new_item)
window.config(menu=menu)

window.mainloop()