#!/usr/bin/env python
# -*- coding:utf8 -*-
import tkinter as tk

import os


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.filePath = os.path.split(os.path.realpath(__file__))[0] + "\\py_cache.txt"

        if not os.path.exists(self.filePath):
            self.f = open(self.filePath, mode="w")
            self.countTimes = 0
        else:
            self.f = open(self.filePath, mode="r")
            self.countTimes = int(str(self.f.read()))

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.btn = tk.Button(self)
        self.btn["text"] = "点击计数一次(" + str(self.countTimes) + ")"
        self.btn["command"] = self.say_hi
        self.btn.pack(side="top")

    def say_hi(self):
        self.countTimes += 1
        open(self.filePath, mode="w").write(str(self.countTimes))
        self.f.flush()
        self.btn["text"] = "点击计数一次(" + str(self.countTimes) + ")"


root = tk.Tk()
app = Application(master=root)
app.mainloop()
