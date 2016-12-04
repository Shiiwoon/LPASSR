#!/usr/bin/env python3
# coding: utf-8

from tkinter import *
class MainWindow(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.grid()

app = MainWindow()
app.master.title('Title here ...!')
#app.master.iconbitmap('icon.ico')
app.mainloop()
