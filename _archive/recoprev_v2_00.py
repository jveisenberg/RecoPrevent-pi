#!/usr/bin/python3
#
# DISPLAY=:0.0 ./recoprev_v1_01.py
#
import tkinter as tk
import time as tm
from PIL import ImageTk as itk
from datetime import datetime

# myPointZero = tm.struct_time(tm_year=2018, tm_mon=8, tm_mday=30, tm_hour=10, tm_min=0, tm_sec=0)
myPointZero = '2018-08-30'
myWTitle='RecoPrevent'
myWwidth=800
myWheight=480

p_top_x='30'
p_top_y='0'
p_bot_x='100'
p_bot_y='10'

mybg='black'
myfg='grey'
myFont='helvetica'+' '
myFontXXS='10'
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
    clock_label['text'] = clock_time
    timetozero_label['text'] = str(days_between(date_time, myPointZero)) + " Tage"
    myW.after(200, display_time)

myW=tk.Tk()
myW.title(myWTitle)
myW.configure(bg=mybg) # to set the windows wide background
screenwidth = myW.winfo_screenwidth()
screenheight = myW.winfo_screenheight()
#myW.geometry("%dx%d+%d+%d" % (myWwidth, myWheight, 0, 0))
myW.geometry()
#screenwidth / 2 - myWwidth, 50))

# frame top
top_frame = tk.Frame(myW, bg=mybg)
mid_frame = tk.Frame(myW, bg=mybg)
bot_frame = tk.Frame(myW, bg=mybg)
top_frame.grid(row=0, ipady='10')
mid_frame.grid(row=1, ipady='10')
bot_frame.grid(row=2, ipady='10')

wd_label = tk.Label(top_frame, font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_top_x)
wd_label.grid(row=0, column=0)
week_label = tk.Label(top_frame, font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_top_x)
week_label.grid(row=0, column=1)
date_label = tk.Label(top_frame, font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_top_x)
date_label.grid(row=0, column=2)
clock_label = tk.Label(top_frame, font=myFont+myFontS, bg=mybg, fg=myfg, padx=p_top_x)
clock_label.grid(row=0, column=3)

# frame middle
timetozero_label=tk.Label(mid_frame, font=myFont+myFontXL, bg=mybg, fg=myfg)
timetozero_label.grid()

# frame bottom
img1=itk.PhotoImage(file='smiley_A.png')
smil1=tk.Label(bot_frame, text="Smiley 1", font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_bot_x, pady=p_bot_y, image=img1)
smil1.grid(row=0, column=0)

img2=itk.PhotoImage(file='smiley_B.png')
smil2=tk.Label(bot_frame, text="Smiley 2", font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_bot_x, pady=p_bot_y, image=img2)
smil2.grid(row=0, column=1)

img3=itk.PhotoImage(file='smiley_C.png')
smil3=tk.Label(bot_frame, text="Smiley 3", font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_bot_x, pady=p_bot_y, image=img3)
smil3.grid(row=0, column=2)

img4=itk.PhotoImage(file='smiley_D.png')
smil4=tk.Label(bot_frame, text="Smiley 4", font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_bot_x, pady=p_bot_y, image=img4)
smil4.grid(row=0, column=3)

img5=itk.PhotoImage(file='smiley_E.png')
smil5=tk.Label(bot_frame, text="Smiley 5", font=myFont+myFontXS, bg=mybg, fg=myfg, padx=p_bot_x, pady=p_bot_y, image=img5)
smil5.grid(row=0, column=4)

# call the content
display_time()

# main loop
#myW.attributes("-fullscreen", True)
myW.mainloop()
