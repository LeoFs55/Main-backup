import tkinter as tk
from tkinter import messagebox

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        messagebox.showerror("Erro", "Expressão inválida")
        expression = ""
        input_text.set(expression)

window = tk.Tk()
window.geometry("400x450")
window.resizable(0, 0)
window.title("Calculadora Tkinter")

# Variável global
expression = ""

# StringVar para atualizar a tela da calculadora
input_text = tk.StringVar()

# Frame para a tela da calculadora
input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

btns_frame = tk.Frame(window, width=400, height=450, bg="grey")
btns_frame.pack()
# Tela da calculadora
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10) # aumenta a altura da entrada

# Frame para os botões

# Primeira linha
clear = tk.Button(btns_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = tk.Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)

# Segunda linha
seven = tk.Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
eight = tk.Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(8)).grid(row=1, column=1, padx=1, pady=1)
nine = tk.Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
multiply = tk.Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# Terceira linha
four = tk.Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(4)).grid(row=2, column=0, padx=1, pady=1)
five = tk.Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(5)).grid(row=2, column=1, padx=1, pady=1)
six = tk.Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(6)).grid(row=2, column=2, padx=1, pady=1)
minus = tk.Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("-")).grid(row=2, column=3, padx=1, pady=1)

# Quarta linha
one = tk.Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(1)).grid(row=3, column=0, padx=1, pady=1)
two = tk.Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(2)).grid(row=3, column=1, padx=1, pady=1)
three = tk.Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(3)).grid(row=3, column=2, padx=1, pady=1)
plus = tk.Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click("+")).grid(row=3, column=3, padx=1, pady=1)

# Quinta linha
zero = tk.Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
point = tk.Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_click(".")).grid(row=4, column=2, padx=1, pady=1)
equals = tk.Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: button_equal()).grid(row=4, column=3, padx=1, pady=1)

# Inicia o loop da janela
window.mainloop()