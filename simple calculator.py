import tkinter as tk  

def evaluate_expression(expression):  
    try:  
        result = eval(expression)  
        entry_var.set(result)  
    except Exception as e:  
        entry_var.set("Error")  

def append_to_expression(character): 
    current_text = entry_var.get()  
    entry_var.set(current_text + character)  

def clear_expression():  
    entry_var.set("")  

app = tk.Tk()  
app.title("Simple Calculator")  

entry_var = tk.StringVar()  
entry = tk.Entry(app, textvariable=entry_var, width=16, font=('Arial', 24), borderwidth=5)  
entry.grid(row=0, column=0, columnspan=4)  

buttons = [  
    '7', '8', '9', '/',  
    '4', '5', '6', '*',  
    '1', '2', '3', '-',  
    'C', '0', '=', '+'  
]  

row_val = 1  
col_val = 0  

for button in buttons:  
    if button == '=':  
        btn = tk.Button(app, text=button, command=lambda: evaluate_expression(entry_var.get()))  
    elif button == 'C':  
        btn = tk.Button(app, text=button, command=clear_expression)  
    else:  
        btn = tk.Button(app, text=button, command=lambda b=button: append_to_expression(b))  
    
    btn.grid(row=row_val, column=col_val, sticky="nsew", padx=5, pady=5)  
    col_val += 1  
    if col_val > 3:  
        col_val = 0  
        row_val += 1  

for i in range(4):  
    app.grid_columnconfigure(i, weight=1)  

app.mainloop()