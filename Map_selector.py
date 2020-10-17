# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 17:05:36 2020

@author: Leena
"""

import random
import tkinter as tk

all_maps = ["ASCENT", "BIND", "ICE BOX", "HAVEN", "SPLIT"]

num = len(all_maps)

sel = random.choice(all_maps)

text_1 = ("Official map for the next match is \n\n" + sel)


master = tk.Tk() 
master.geometry("500x500") 

def openNewWindow():
    newWindow = tk.Toplevel(master)
    
    def destroy_all():
        newWindow.destroy()
        master.destroy()
        
    
    newWindow.title("MAP SELECTION")
    greeting = tk.Label(newWindow, text=text_1)
    greeting.config(font=("Arial",44))
    greeting.pack(pady = 10)    
    
    btn = tk.Button(newWindow,  
             text ="OK",  
             command = destroy_all) 

    btn.pack(pady = 10) 
# a button widget which will open a  
# new window on button click 
btn = tk.Button(master,  
             text ="Click to generate VALORANT MAP",  
             command = openNewWindow) 

btn.pack(pady = 10) 

# mainloop, runs infinitely 
tk.mainloop() 
