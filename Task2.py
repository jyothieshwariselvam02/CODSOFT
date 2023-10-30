import tkinter as tk 
from tkinter import Tk

calculate = "" 

def add_calc(symbol):
    global calculate
    calculate += str(symbol)
    txt_rslt.delete(1.0,"end")
    txt_rslt.insert(1.0,  calculate)

def eval_calc():
    global calculate 
    try:
        rslt = str(eval(calculate))
        calculate = ""
        txt_rslt.delete(1.0, "end")
        txt_rslt.insert(1.0, rslt)
    except:
        clr_fld()
        txt_rslt.insert(1.0, "Error")
        
def clr_fld():
    global calculate 
    calculate = ""
    txt_rslt.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

txt_rslt = tk.Text(root, height = 2, width = 16, font = ("Arial", 24))
txt_rslt.grid(columnspan = 5)

btn_1 = tk.Button(root, text = "7", command =lambda: add_calc(7), width = 5, font = ("Arial",14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text = "8", command =lambda: add_calc(8), width = 5, font = ("Arial",14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text = "9", command =lambda: add_calc(9), width = 5, font = ("Arial",14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text = "+", command =lambda: add_calc('+'), width = 5, font = ("Arial",14))
btn_4.grid(row=2, column=4)
btn_5 = tk.Button(root, text = "4", command =lambda: add_calc(4), width = 5, font = ("Arial",14))
btn_5.grid(row=3, column=1)
btn_6 = tk.Button(root, text = "5", command =lambda: add_calc(5), width = 5, font = ("Arial",14))
btn_6.grid(row=3, column=2)
btn_7 = tk.Button(root, text = "6", command =lambda: add_calc(6), width = 5, font = ("Arial",14))
btn_7.grid(row=3, column=3)
btn_8 = tk.Button(root, text = "-", command =lambda: add_calc('-'), width = 5, font = ("Arial",14))
btn_8.grid(row=3, column=4)
btn_9 = tk.Button(root, text = "1", command =lambda: add_calc(1), width = 5, font = ("Arial",14))
btn_9.grid(row=4, column=1)
btn_10 = tk.Button(root, text = "2", command =lambda: add_calc(2), width = 5, font = ("Arial",14))
btn_10.grid(row=4, column=2)
btn_11 = tk.Button(root, text = "3", command =lambda: add_calc(3), width = 5, font = ("Arial",14))
btn_11.grid(row=4, column=3)
btn_12 = tk.Button(root, text = "*", command =lambda: add_calc('*'), width = 5, font = ("Arial",14))
btn_12.grid(row=4, column=4)
btn_13 = tk.Button(root, text = "(", command =lambda: add_calc('('), width = 5, font = ("Arial",14))
btn_13.grid(row=5, column=1)
btn_14 = tk.Button(root, text = "0", command =lambda: add_calc(0), width = 5, font = ("Arial",14))
btn_14.grid(row=5, column=2)
btn_15 = tk.Button(root, text = ")", command =lambda: add_calc(')'), width = 5, font = ("Arial",14))
btn_15.grid(row=5, column=3)
btn_16 = tk.Button(root, text = "/", command =lambda: add_calc('/'), width = 5, font = ("Arial",14))
btn_16.grid(row=5, column=4)
btn_clr = tk.Button(root, text = "CLR", command = clr_fld, width = 11, font = ("Arial", 14))
btn_clr.grid(row=6, column=1, columnspan=2)
btn_eql = tk.Button(root, text = "=", command = eval_calc, width = 11, font = ("Arial", 14))
btn_eql.grid(row=6, column=3, columnspan=2)

root.mainloop()

