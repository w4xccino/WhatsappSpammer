import webbrowser, time, pyautogui
import tkinter as tkk
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Auto Python GUI")

number = StringVar()


def send():
    result = textbox.get("1.0", "end")
    webbrowser.open('https://web.whatsapp.com/send?phone=' + number.get())
    time.sleep(5)
    for i in range(int(spinbox.get())):
        pyautogui.write(result)


Label(root, text='Number').grid(row=0, column=0)
Entry(root, textvariable=number).grid(row=1, column=0)
Label(root, text='Choose Times').grid(row=0, column=1)
spinbox = Spinbox(root, from_= 1, to=100)
spinbox.grid(row=1, column=1)

Label(root, text='Message').grid(row=2, column=0)
textbox = Text(root, height=10, width=20)
textbox.grid(row=3, column=0)

button = Button(root, text="Send", command=send).grid(row=4, column=1)

root.mainloop()
