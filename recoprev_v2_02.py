#!/usr/bin/python3
#
# DISPLAY=:0.0 ./recoprev_vx_yz.py
#
# start from venus development environment as ssh with a bash script
# ssh csalow@venus.local /home/csalow/Desktop/strRecoPrev.sh
## #!/bin/bash
## cd /home/csalow/altii-drive/me/dev/recoprevent
## DISPLAY=:0.0 ./recoprev_v2_00.py &
#
# for RPi
# Fonts: sudo apt install ttf-mscorefonts-installer
#
# for MACOS
# PIL: sudo pip3 install Pillow
#
import tkinter as tk
import time as tm
import csv
from PIL import ImageTk as itk
from datetime import datetime
from os import path

GlbStatus = 'waiting for input'

# myPointZero = tm.struct_time(tm_year=2018, tm_mon=8, tm_mday=30, tm_hour=10, tm_min=0, tm_sec=0)
myPointZero = '2018-08-30'
myWTitle = 'RecoPrevent 2.01'
myWwidth = 800
myWheight = 480

p_top_x = '25'
p_top_y = '10'
smil_w = '150'
smil_h = '150'

frame_pad_x = '0'
frame_pad_y = '5'
mybg = 'black'
myfg = 'grey'
myFont = 'arial' + ' '
myFontXXS = '10'
myFontXS = '20'
myFontS = '40'
myFontM = '60'
myFontL = '80'
myFontXL = '100'
myFontXXL = '120'

def smiley_logger(event=None, smiley=0, filename='smiley_logger.csv'):
    global GlbStatus
    # print("Single Click, Button-l")
    print("Event: ", event)
    timestamp = tm.strftime('%Y-%m-%d %H:%M:%S')
    print(timestamp, smiley)
    if not (path.exists(filename)):
        with open(filename, mode='w') as logger_file:
            writer = csv.writer(logger_file, delimiter=',')
            writer.writerow(['Timestamp', 'SmileyEvent'])
            writer.writerow([timestamp, smiley])
        logger_file.close()
        GlbStatus = str(timestamp) + ', Smiley ' + str(smiley)
    else:
        with open(filename, mode='a') as logger_file:
            writer = csv.writer(logger_file, delimiter=',')
            writer.writerow([timestamp, smiley])
        logger_file.close()
        GlbStatus = str(timestamp) + ', Smiley ' + str(smiley)

def quit(event):
    print("Exit Button, so let's stop")
    import sys; sys.exit()

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)


def display_time():
    clock_time = tm.strftime('%H:%M:%S')
    wd_time = tm.strftime('%A')
    week_number = tm.strftime('KW %W')
    date_time = tm.strftime('%Y-%m-%d')
    wd_label['text'] = wd_time
    week_label['text'] = week_number
    date_label['text'] = date_time
    clock_label['text'] = clock_time
    timetozero_label['text'] = str(days_between(date_time, myPointZero))  # + " Tage"
    status_label['text'] = GlbStatus
    # print(GlbStatus)
    myW.after(200, display_time)


#check_logger_file('smiley_logger.csv')

myW = tk.Tk()
myW.title(myWTitle)
myW.configure(bg=mybg)  # to set the windows wide background
screenwidth = myW.winfo_screenwidth()
screenheight = myW.winfo_screenheight()

if (screenwidth == 800) and (screenheight == 480):
    myW.geometry("%dx%d+%d+%d" % (myWwidth, myWheight, 0,0))
    myW.attributes("-fullscreen", True)
else:
    myW.geometry("%dx%d+%d+%d" % (myWwidth, myWheight, screenwidth / 2 - myWwidth, screenheight / 2 - myWheight))

# frame top
top_frame = tk.Frame(myW, bg=mybg)
mid_frame = tk.Frame(myW, bg=mybg)
bot_frame = tk.Frame(myW, bg=mybg)
status_frame = tk.Frame(myW, bg=mybg)
top_frame.grid(row=0, ipadx=frame_pad_x, ipady=frame_pad_y)
mid_frame.grid(row=1, ipadx=frame_pad_x, ipady=frame_pad_y)
bot_frame.grid(row=2, ipadx=frame_pad_x, ipady=frame_pad_y)
status_frame.grid(row=3)

wd_label = tk.Label(top_frame, font=myFont + myFontXS, bg=mybg, fg=myfg, padx=p_top_x, pady=p_top_y)
wd_label.grid(row=0, column=0)
date_label = tk.Label(top_frame, font=myFont + myFontXS, bg=mybg, fg=myfg, padx=p_top_x, pady=p_top_y)
date_label.grid(row=0, column=1)
week_label = tk.Label(top_frame, font=myFont + myFontXS, bg=mybg, fg=myfg, padx=p_top_x, pady=p_top_y)
week_label.grid(row=0, column=2)
clock_label = tk.Label(top_frame, font=myFont + myFontS, bg=mybg, fg=myfg, padx=p_top_x, pady=p_top_y)
clock_label.grid(row=0, column=3)

# frame middle
timetozero_label = tk.Label(mid_frame, font=myFont + myFontXL, bg=mybg, fg=myfg)
timetozero_label.grid()

# frame bottom
img1 = itk.PhotoImage(file='smiley_A.gif')
smil1 = tk.Label(bot_frame, image=img1, width=smil_w, height=smil_h, bg=mybg)
smil1.grid(row=0, column=0)
smil1.bind('<Button-1>', lambda event: smiley_logger(event, smiley=1)) #, filename='smiley_logger.csv'))

img2 = itk.PhotoImage(file='smiley_B.gif')
smil2 = tk.Label(bot_frame, image=img2, width=smil_w, height=smil_h, bg=mybg)
smil2.grid(row=0, column=1)
smil2.bind('<Button-1>', lambda event: smiley_logger(event, smiley=2))

img3 = itk.PhotoImage(file='smiley_C.gif')
smil3 = tk.Label(bot_frame, image=img3, width=smil_w, height=smil_h, bg=mybg)
smil3.grid(row=0, column=2)
smil3.bind('<Button-1>', lambda event: smiley_logger(event, smiley=3))

img4 = itk.PhotoImage(file='smiley_D.gif')
smil4 = tk.Label(bot_frame, image=img4, width=smil_w, height=smil_h, bg=mybg)
smil4.grid(row=0, column=3)
smil4.bind('<Button-1>', lambda event: smiley_logger(event, smiley=4))

img5 = itk.PhotoImage(file='smiley_E.gif')
smil5 = tk.Label(bot_frame, image=img5, width=smil_w, height=smil_h, bg=mybg)
smil5.grid(row=0, column=4)
smil5.bind('<Button-1>', lambda event: smiley_logger(event, smiley=5))

#
# show the status if there is any
status_label = tk.Label(status_frame, font=myFont + myFontXXS, bg=mybg, fg=myfg)
status_label.grid(row=0, column=0)
status_label.bind('<Button-1>', quit)

# call the content
display_time()

# main loop
myW.mainloop()
