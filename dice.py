import random
import tkinter as tk
from tkinter import ttk
from tkinter.constants import BOTTOM, CENTER, COMMAND, LEFT, RIGHT, TOP, END


INPUT_FONT= ("Verdana", 22)

def roll_die():
    num = random.randrange(1,7)
    entry.delete(0, END)
    entry.insert(0, num)

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Replace')
    root.geometry('620x330')
    root.resizable(0, 0)

    # layout on the root window
    # root.columnconfigure(0, weight=4)
    # root.columnconfigure(1, weight=1)
    button = ttk.Button(root, width=25, text="Roll the die", command=roll_die)
    button.grid()

    entry = ttk.Entry(root, width=25, font=INPUT_FONT)
    entry.grid()
    entry.insert(0, "0")


    root.mainloop()
