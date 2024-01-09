#importing 
from tkinter import *

#calling Tk() method
#вызываем Tk метод
root = Tk() 
#its used for creating gui window 
# gui - graphic user interface


#title() method is used to change the title 
#title() используется для изменения заголовка 
root.title("Zagolovok")

#geometry() method is used to resize the Gui Window
root.geometry("250x250")

#maxsize() method is used for define the maximum size of the window
root.maxsize(300,300)

#minsize() method is used for define the minimum size of the window
root.minsize(200,200)

#mainloop() is used to load the GUI Window
root.mainloop()
