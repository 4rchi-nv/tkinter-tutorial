#importing 
from tkinter import *

#calling Tk() method
root = Tk() 
#its used for creating gui window 

#title() method is used to change the title 
root.title("Zagolovok")

#geometry() method is used to resize the Gui Window
root.geometry("250x250")

#maxsize() method is used for define the maximum size of the window
root.maxsize(300,300)

#minsize() method is used for define the minimum size of the window
root.minsize(200,200)

#mainloop() is used to load the GUI Window
root.mainloop()
