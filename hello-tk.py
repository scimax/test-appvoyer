from tkinter import *

from PIL import Image
im = Image.open("27972c514309f9787684df8c8082f53d.png")
im.show()

root = Tk()
w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()


