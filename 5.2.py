from tkinter import *
import RPi.GPIO as GPIO
from gpiozero import LED
import tkinter.font
GPIO.setmode(BCM)

win = Tk()
win.title("LED_TOGGLER");
font_settings = tkinter.font.Font(family = "Ariel", size = 16, weight = "bold")

redled = LED(12)
yellowled = LED(13)
greenled = LED(16)
val = IntVar()

def led_toggler():
    var = val.get()
    if var == 1:
        redled.on()
        yellowled.off()
        greenled.off()
        
    elif var == 2:
        redled.off()
        yellowled.on()
        greenled.off()

    else:
        redled.off()
        yellowled.off()
        greenled.on()

def programclose():
    GPIO.cleanup()
    win.destroy()
    


REDBUTTON = Radiobutton( win, text = "Turn On RED LED", font = font_settings, variable = val, val = 1, command = led_toggler, height = 2, width = 10)
REDBUTTON.grid( row = 0, column = 1)

YELLOWBUTTON = Radiobutton( win, text = "Turn On YELLOW LED", font = font_settings, variable = val, val = 2, command = led_toggler, height = 2, width = 10)
YELLOWBUTTON.grid( row = 1, column = 1)

GREENBUTTON = Radiobutton( win, text = "Turn On GREEN LED", font = font_settings, variable = val, val = 3, command = led_toggler, height = 2, width = 10)
GREENBUTTON.grid( row = 2, column = 1)

CLOSEBUTTON = Radiobutton( win, text = "EXIT", font = font_settings,command = programclose, height = 2, width = 10)
CLOSEBUTTON.grid( row = 3, column = 1)


win.mainloop()



    



