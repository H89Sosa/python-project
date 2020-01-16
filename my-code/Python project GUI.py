# -*- coding: utf-8 -*-

# import tkinter
from tkinter import *


import sounddevice as sd
import soundfile as sf

#filename = 'laugh.mp3'
# Extract data and sampling rate from file
#data, fs = sf.read(filename, dtype='float32')  
#sd.play(data, fs)
#status = sd.wait()

window = Tk()

# Assign a background of the window


bg_photo = PhotoImage(file = "room.png")
label1 = Label(window, image=bg_photo)
label1.image = bg_photo
label1.place(x=0, y=0)

#background_image= PhotoImage(file = "room.png")
#background_label = Label(window, image=background_image).place(x=0, y=0, relwidth=1, relheight=1)
#background_label.image = background_image


# Setting up parameters of the window

window.title('NIGHT OF TERROR')
window.geometry('800x600')
window.configure(background='black')
window.iconbitmap('sangre.png')
window.resizable('false', 'false')


def btnclick():
    """ 
    Function to determine the button A usage.
    It gets the text printed on it, and returns it as a string.
    
    """
    Atext.set(next(funny_b))
    ScreenText.set(next(funny_w))
 

# Frame configuration

#frame_top= Frame(window).grid(row=1, column=0)
#frame_ctr = Frame(window).grid(row=1, column=0)
#frame_btm = Frame(window).grid(row=2, column=0)
#frame_btm_l = Frame(frame_btm).grid(row=0, column=0)
#frame_btm_cl = Frame(window).grid(row=0, column=0)
#frame_btm_cr = Frame(window).grid(row=0, column=0)
#frame_btm_r = Frame(window).grid(row=0, column=0)
    
frame_top= Frame(window).pack()
frame_ctr = Frame(window).pack()
frame_btm = Frame(window).pack()
frame_btm_l = Frame(frame_btm).pack()
#frame_btm_cl = Frame(window).grid(row=0, column=0)
#frame_btm_cr = Frame(window).grid(row=0, column=0)
#frame_btm_r = Frame(window).grid(row=0, column=0)

funny_b = iter(["YES!", "", "", "", "...", "what?", "I'd appreciate", "Thanks!", "OK"])
funny_w = iter(["Are you sure...?", "Preparing Game", "Preparing Game.",
               "Preparing Game..", "Preparing Game...", "Nah, I'm just joking",
               "But if you wish I can execute the game for you", "OKEY!", "...",
               "This game doesn't work at all, sorry", "Wish you luck"])




# Widget Text Variables

Atext = StringVar()
Btext = StringVar()
Ctext = StringVar()
Dtext = StringVar()
RoomName = StringVar()
ScreenText = StringVar()
promptText = StringVar()

# Initial widget values
Atext.set("Start!")
#Btext.set("Button B")
#Ctext.set("Button C")
#Dtext.set("Button D")
RoomName.set("NIGHT OF TERROR")
ScreenText.set("... Do you really wanna play?")


# Widget configuration


#Room = Label(frame_top, textvariable= RoomName, font=("CF Night of terror PERSONAL", 64), fg='red', ).grid(row=0, column=0) 
#String = Label(frame_ctr, textvariable= ScreenText, font=("Mom´sTypewriter", 24), fg='white').grid(row=1, column=0)

#Font won't display because it's downloaded
Room = Label(frame_top, textvariable= RoomName, font=("CF Night of terror PERSONAL", 64), fg='red', bg='black' ).pack(pady=30)
String = Label(frame_ctr, textvariable= ScreenText, font=("Mom´sTypewriter", 24), bg='black', fg='white').pack(pady=200)


btn = Button(frame_btm, text=Atext, command=btnclick, bg='black', fg='red').pack(anchor=CENTER)
#btn2 = Button(frame_btm_cl, text=Btext, bg='black', fg='red').pack()
#btn3 = Button(frame_btm_cr, text=Ctext, bg='black', fg='red').pack()
#btn3 = Button(frame_btm_r, text=Dtext, bg='black', fg='red').pack()


# Initial widget values
Atext.set("Start!")
#Btext.set("Button B")
#Ctext.set("Button C")
#Dtext.set("Button D")
RoomName.set("NIGHT OF TERROR")
ScreenText.set("... Do you really wanna play?")






window.mainloop()
