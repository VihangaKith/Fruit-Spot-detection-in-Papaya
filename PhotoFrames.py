import cv2
import time
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import glob
r = tk.Tk()

#-------------------------------interface------------------------------------------------------------
output_loc = 'D:\\Education\\3rd Year\\3rd Year Project\\Project\\Papaw\\data\\'
def opefile():
   result = filedialog.askopenfilename(initialdir="/", title="select file", filetypes=(("MP4 files", ".mp4"),
                                                                                      ("all files", "*.*")))
   print(result)

   label = Label(r, text="Video path\n").pack()

   labe2 = Label(r, text=result).pack()
   button2 = tk.Button(r, text='Convert', width=25, command=r.destroy).pack()

   vidcap = cv2.VideoCapture(result)

   def getFrame(sec, output_loc):
       vidcap.set(cv2.CAP_PROP_POS_MSEC, sec * 1000)
       hasFrames, image = vidcap.read()
       if hasFrames:
           cv2.imwrite(output_loc + "frame " + str(sec) + " sec.jpg", image)  # save frame as JPG file
           print("Converting...", sec, "second")
       return hasFrames

   sec = 0
   frameRate = 10

   success = getFrame(sec, output_loc)
   while success:
       sec = sec + frameRate
       sec = round(sec, 2)
       success = getFrame(sec, output_loc)
       os.startfile(output_loc)
r.title('Import Video...')
button1 = tk.Button(r, text='Open', width=50, command=opefile).pack()

r.geometry("550x150")
r.mainloop()



#-----------------------------------location------------------------------------------------------------------



#os.rmdir(output_loc)
#os.mkdir("D:\\Education\\3rd Year\\3rd Year Project\\Project\\Papaw\\data\\")


#--------------------------------frame dividing------------------------------------------------------



#---------------------------------Select Image----------------------------------------------------------------------

root = Tk()
root.geometry("550x500")
root.resizable(width=True, height=True)

def openfn():
    filename = filedialog.askopenfilename(title='open', filetypes=(("Image files", ".jpg"),
                                                                                      ("all files", "*.*")))
    return filename
def open_img():
    x = openfn()
    img = Image.open(x)

    #****************************************************************
    #****************************************************************
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
btn = Button(root, text='open image', command=open_img).pack()

root.mainloop()

#-----------------cascading-----------------------------------------------------------------------------------------


