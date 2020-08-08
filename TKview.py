from tkinter import *
import os

window = Tk()

def WinSize500():
    window.geometry('500x500')

def WinSize700():
    window.geometry('700x400')

def netw():
    return os.system('ping ya.ru')


window.title('Alt_MTR')

frame = Frame()
frame_file_content = LabelFrame(text='Test_text')

file_name = Entry(frame, width='25')

button_ping = Button(frame, text='Ping')
button_tracert = Button(frame, text='Tracert')

file_content = Text(frame_file_content, bg='#FFFFE0', width='50', height='20', wrap=NONE)

Yscroll = Scrollbar(frame_file_content, command=file_content.yview)
Xscroll = Scrollbar(orient=HORIZONTAL, command=file_content.xview)

file_content.configure(yscrollcommand=Yscroll.set, xscrollcommand=Xscroll.set)

frame.pack()
file_name.pack(side=LEFT)
button_ping.pack(side=LEFT)
button_tracert.pack(side=LEFT)
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