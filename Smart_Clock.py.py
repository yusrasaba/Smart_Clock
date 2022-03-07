from datetime import datetime
from time import strftime
from tkinter import *

root = Tk()
root.title("Smart Clock")

def hour24_format():
    str1 = strftime('%H:%M:%S %p')
    Label1.config(text=str1)
    Label1.after(1000, hour24_format)

def hour12_format():
    str2 = strftime('%I:%M:%S %p')
    Label2.config(text=str2)
    Label2.after(1000, hour12_format)

Label1 = Label(root, font=('ds-digital', 65), background="black", foreground="cyan")
Label1.pack(anchor='center')
hour24_format()

Label2 = Label(root, font=('ds-digital', 65), background="black", foreground="cyan")
Label2.pack(anchor='center')
hour12_format()

root.mainloop()
