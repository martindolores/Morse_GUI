from tkinter import *
from tkinter import messagebox
import RPi.GPIO as GPIO
import time

##HARDWARE
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)

##MORSE DICTIONARY
morseDict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '..-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}

##METHODS
def blink(morse):
   i = 0
   for morseLetter in morse:
      for char in morseLetter:
         if char == '-':
            GPIO.output(12, GPIO.HIGH)
            time.sleep(3)
            GPIO.output(12, GPIO.LOW)
            space(i, morseLetter)
            i = i + 1
         elif char == '.':
            GPIO.output(12, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(12, GPIO.LOW)
            space(i, morseLetter)
            i = i + 1
      i = 0

#Checks to see if at the end of a letter, if so sleep 5 seconds
def space(index, str):
   if index == len(str) - 1:
      time.sleep(5)
   else:
      time.sleep(1)

def check_space(text):
    if text.startswith(' ') or text.endswith(' '):
       return True
    else:
       return False

def morse(text):
   strippedText = text.strip()
   if strippedText.count(' ') == 1:
      messagebox.showerror("Error", "Text contains space, please enter only 1 word")
      textBox.delete("1.0", "end")
      return
   elif text.count(' ') == 1 or check_space(text):
      messagebox.showerror("Error", "Text contains space, please try again without space")
      textBox.delete("1.0", "end")
      return
   messagebox.showinfo("Morse code", "Blinking morse...")
   morseLetters = []
   for char in text:
      if char == '\n':
         continue 
      morseLetters.append(morseDict[char.upper()])
   blink(morseLetters)

##EVENT METHODS
def getText():
   maxLength = 12
   text = textBox.get("1.0", "end-1c")
   if len(text) > maxLength:
      messagebox.showerror("Error", "Input cannot be longer than 12 characters")
      textBox.delete("1.0", "end")
   else:
      morse(text)
      textBox.delete("1.0", "end")

##GUI DEFINITIONS
win = Tk()
win.title("Morse Code")
frame = Frame(win)
textBox = Text(frame)
label = Label(frame, text = "Enter text that is less than 12 characters")
button = Button(win, text = "Enter", command = getText)
buttonFrame = Frame(frame)

label.pack(side = "top")
textBox.pack(side="top")
frame.pack()
button.pack()
buttonFrame.pack(side = "bottom")

win.mainloop()
