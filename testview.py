from tkinter import *

# !/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    import Tkinter as tkinter
except ImportError:  # Python 3
    import tkinter

root = tkinter.Tk()
text = tkinter.Text(root)
text.pack()
text.insert('end', u"строка сразу видна")
root.after(1000, text.insert, 'end', u"\nчерез секунду")
root.after(2000, text.insert, 'end', u"\nчерез две")
root.after(3210, root.destroy)  # exit

root.mainloop()