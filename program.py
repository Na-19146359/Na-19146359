from cProfile       import label
from pickle         import FROZENSET
from tkinter        import *
from tkinter        import filedialog
from tkinter.ttk import Frame, Button, Style
from PIL import  Image,ImageTk
import os
import tkinter as tk
from PIL                import  Image,ImageTk
from tensorflow.keras.models import Sequential, Model, load_model, save_model
import matplotlib.pyplot as plt

import cv2
import numpy as np

model = load_model('D:/AI/pneumonia.h5')
classes = ['Bacteria','Virus','normal']


def showimage():
    global fln
    fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File", filetypes=(("PNG File","*.png"),("JPG File","*.jpg"), ("ALL Files","*.*")))
    img = Image.open(fln)
    img.thumbnail((300,300))
    img = ImageTk.PhotoImage(img)
    lbl3.configure(image= img)
    lbl3.image = img



root = Tk()
root.title("Recognize Body Parts")
root.geometry("800x600")
# lbl1 = Label(root)
# lbl2 = Label(root)

frm = Frame(root)
frm.pack(side=BOTTOM, padx=15, pady=15)

lbl = Label(root,
            text = "Nhận diện bệnh về phổi bằng ảnh X-ray", 
            fg= "yellow", 
            font=("Arial", 30), 
            background="green"
            )
lbl.pack(padx=10, pady= 10)

lbl3 = Label(root)
lbl3.pack()

root.style = Style()
root.style.theme_use("clam")

btn = Button(frm,text = "Browser Image", command= showimage)
btn.pack(side=tk.LEFT,padx= 30)

btn1 = Button(frm,text = "Recognize")
btn1.pack(side=tk.LEFT,padx= 30, pady = 10)

btn3 = Button(frm,text = "Clear")
btn3.pack(side=tk.LEFT,padx=30)

btn2 = Button(frm,text = "Exit",command=lambda: exit())
btn2.pack(side=tk.LEFT,padx=30)

root.mainloop()