import tkinter as tk
import time as tm
from PIL import Image, ImageTk
from datetime import datetime

# myPointZero = tm.struct_time(tm_year=2018, tm_mon=8, tm_mday=30, tm_hour=10, tm_min=0, tm_sec=0)
myPointZero = '2018-08-30'
myWTitle='RecoPrevent'
myWwidth=800
myWheight=480

mybg='black'
myfg='grey'
myFont='helvetica'+' '
myFontXS='20'
myFontS='40'
myFontM='60'
myFontL='80'
myFontXL='100'
myFontXXL='120'

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)
    
def display_time():
    clock_time = tm.strftime('%H:%M:%S')
    wd_time = tm.strftime('%A')
    week_number = tm.strftime('W %W')
    date_time = tm.strftime('%Y-%m-%d')
    wd_label['text'] = wd_time
    week_label['text'] = week_number
    date_label['text'] = date_time
    timetozero_label['text'] = days_between(date_time, myPointZero)
    clock_label['text'] = clock_time
    myW.after(200, display_time)

myW=tk.Tk()
myW.title(myWTitle)
myW.configure(bg=mybg) # to set the windows wide background
screenwidth = myW.winfo_screenwidth()
screenheight = myW.winfo_screenheight()
myW.geometry("%dx%d+%d+%d" % (myWwidth, myWheight, 0, 0))

#screenwidth / 2 - myWwidth, 50))

wd_label = tk.Label(myW, font=myFont+myFontXS, bg=mybg, fg=myfg)
wd_label.grid(row=0, column=0)
week_label = tk.Label(myW, font=myFont+myFontXS, bg=mybg, fg=myfg)
week_label.grid(row=0, column=1)
date_label = tk.Label(myW, font=myFont+myFontXS, bg=mybg, fg=myfg)
date_label.grid(row=0, column=2)
clock_label = tk.Label(myW, font=myFont+myFontXS, bg=mybg, fg=myfg)
clock_label.grid(row=0, column=4)

timetozero_label=tk.Label(myW, font=myFont+myFontXS, bg=mybg, fg=myfg)
timetozero_label.grid(row=1, column=0)

display_time()

imag1=Image.open("smiley_A.png") #.convert("RGB")
dspl1=ImageTk.PhotoImage(imag1)
smil1=tk.Label(myW, bg=mybg, fg=mybg, image=dspl1)
smil1.grid(row=2,column=0)

imag2=Image.open("smiley_B.png") #.convert("RGB")
dspl2=ImageTk.PhotoImage(imag2)
smil2=tk.Label(myW, bg=mybg, fg=mybg, image=dspl2)
smil2.grid(row=2,column=1)

imag3=Image.open('smiley_C.png') #.convert("RGB")
dspl3=ImageTk.PhotoImage(imag3)
smil3=tk.Label(myW, bg=mybg, fg=mybg, image=dspl3)
smil3.grid(row=2,column=2)

imag4=Image.open('smiley_D.png') #.convert("RGB")
dspl4=ImageTk.PhotoImage(imag4)
smil4=tk.Label(myW, bg=mybg, fg=mybg, image=dspl4)
smil4.grid(row=2,column=3)

imag5=Image.open('smiley_E.png') #.convert("RGB")
dspl5=ImageTk.PhotoImage(imag5)
smil5=tk.Label(myW, bg=mybg, fg=mybg, image=dspl5)
smil5.grid(row=2,column=4)

myW.mainloop()
