from tkinter import *

# Main window
MainWindow = Tk()

# Labels
Label1 = Label(MainWindow, text = 'Hey plein de blabla pour que la fen soit grande wesh', fg = 'red')
Label1.pack()

# Button
ButQuit = Button(MainWindow, text = 'Quit', command = MainWindow.destroy, bg='#234')
ButQuit.pack()

# Launch evnt
ButQuit.pack()
MainWindow.mainloop()
