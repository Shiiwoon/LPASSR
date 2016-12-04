#!/usr/bin/env python3
# coding: utf-8

from Tkinter import Tk, Label, BOTH
import time
import datetime as dt



class ElapsedTimeClock(Label):
	def __init__(self, parent, *args, **kwargs):
		Label.__init__(self, parent, *args, **kwargs)
		self.lastTime = ""
		t = time.localtime()
		self.zeroTime = dt.timedelta(hours=t[3], minutes=t[4], seconds=t[5])
		self.tick()

	 def tick(self):
		# get the current local time from the PC
		now = dt.datetime(1, 1, 1).now()
		elapsedTime = now - self.zeroTime
		time2 = elapsedTime.strftime('%H:%M:%S')
		
		# if time string has changed, update it
		if time2 != self.lastTime:
			self.lastTime = time2
			self.config(text=time2)

	# calls itself every 200 milliseconds
	# to update the time display as needed
	# could use >200 ms, but display gets jerky
	self.after(200, self.tick)


	if __name__ == "__main__":
		root = Tk()
		clock = ElapsedTimeClock(root, font=('times', 20, 'bold'), bg='green')
		clock.pack(fill=BOTH, expand=1)
		root.mainloop()
