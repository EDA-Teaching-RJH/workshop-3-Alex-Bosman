
# text based story thing lol

# inventory system - several items? use an array so user can type in input
# health bar - 
# simple crafting system? - 
# need specific items to progress
# list all details in a room
# commands [take, drop, inventory, look, score, quit, north, south, east, west, yes, no, health]

# room a - starter room [summary: ] [doors to: b, c, d] [items:] [enemies: none] 
# room b -  room [summary: ] [doors to: a] [items:] [enemies:]
# room c -  room [summary: ] [doors to: a, e] [items:] [enemies:] 
# room d -  room [summary: ] [doors to: a] [items:] [enemies:] 

# room e -  room [summary: ] [doors to: ] [items:] [enemies:] 
# room f -  room [summary: ] [doors to: ] [items:] [enemies:] 
# room g -  room [summary: ] [doors to: ] [items:] [enemies:]
# room h -  room [summary: ] [doors to: end, ] [items:] [enemies:] 

# testing



import tkinter as tk
from tkinter import ttk


class mainWindow:
    def __init__(self, root):
        root.geometry("800x600")
        btn = ttk.Button(root, text="hello")
        btn.pack()



if __name__ == "__main__":
    root = tk.Tk()
    w = mainWindow(root)
    root.mainloop()