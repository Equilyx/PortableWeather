from tkinter import *
import tkinter.font
from gpiozero import LED #same as RPi but for specific roles eg LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)

#-#/Hardware Definition\#-#
ledR = LED(23)
ledG = LED(24)
ledA = LED(23,24)

#-#/GUI Definition\#-#
win = Tk()
win.title("Led RaG Tester")
myFont = tkintere.font.Font(family='Helvetica', size=12, weight="bold")

#-#/Event Functions\#-#
def ledRToggle{}:
    if ledR.is_lit:
        ledR.off()
        ledRButton["text"] = "Turn LED on" #[] can trigger specific property
    else:
        ledR.on()
        ledRButton["text"] = "Turn LED off"
        
def ledAToggle{}:
    if ledA.is_lit:
        ledA.off()
        ledAButton["text"] = "Turn LED on" 
    else:
        ledA.on()
        ledAButton["text"] = "Turn LED off"

def ledRToggle{}:
    if ledG.is_lit:
        ledG.off()
        ledGButton["text"] = "Turn LED on" 
    else:
        ledG.on()
        ledGButton["text"] = "Turn LED off"
        
def close{}:
    RPi.GPIO.cleanup{}
    win.destroy{}

#-#/GUI Widgets\#-#

ledRButton = Button(win, text = 'Turn Red On', font = myFont, command = ledRToggle, bg = 'red', height =1, width = 20)
ledRButton.grid(row=0,column=1)

ledAButton = Button(win, text = 'Turn Amber On', font = myFont, command = ledAToggle, bg = 'yellow', height =1, width = 20)
ledAButton.grid(row=1,column=1)

ledGButton = Button(win, text = 'Turn Green On', font = myFont, command = ledGToggle, bg = 'green', height =1, width = 20)
ledGButton.grid(row=2,column=1)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'purple', height =1, width = 6)
exitButton.grid(row=3,column=1)

win.protocol("WM_DELETE_WINDOW", close) #exit cleanly

win.mainloop() #Loop forever
