from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("img1.png")
        bard=bard.resize((100, 100))
        bardjov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image = bardjov)
        label1.image = bardjov
        label1.place(x=20, y=20)

        rot = Image.open("img2.png")
        rot=rot.resize((100, 100))
        rotunda=ImageTk.PhotoImage(bard)
        label2=Label(self, image=rotunda)
        label2.image = rotunda
        label2.place(x=40, y=160)

        minc = Image.open("img3.png")
        minc=minc.resize((100,100))
        mincol = ImageTk.PhotoImage(minc)
        label3=Label(self, image=mincol)
        label3.image=mincol
        label3.place(x=170, y=50)

root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()

