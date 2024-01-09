from tkinter import *

root = Tk()
root.title("my GUI")
root.geometry("250x150")
img = PhotoImage(Image.open(r'C:\Users\USER\Desktop\image-16.jpg'))
panel = Label(root, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")
root.mainloop()
