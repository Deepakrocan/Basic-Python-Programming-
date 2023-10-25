# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 12:23:13 2023

@author: MCA-05
"""


import tkinter as tk
def calculate():
    try:
        num1 = float (entry1.get())
        num2 = float (entry2.get())
        result=num1+num2
        result_text.set(f"Result:{result}")
    except ValueError:
        result_text.set("invalid input")
window = tk.Tk()
window.title("simple calculator")  
entry1=tk.Entry(window,width=20,font=("Arial",16))
entry1.grid(row=0,column=0,padx=20,pady=10)
entry2=tk.Entry(window,width=20,font=("Arial",16))
entry2.grid(row=1,column=0,padx=20,pady=10)
calculate_button=tk.Button(window,text="calculate",width=20,height=2,command=calculate)
calculate_button.grid(row=2,column=0,padx=10,pady=10)
result_text=tk.StringVar()
result_label=tk.Label(window,textvariable=result_text,font=("Arial",16)) 
result_label.grid(row=3,column=0,padx=10,pady=10)
window.mainloop()