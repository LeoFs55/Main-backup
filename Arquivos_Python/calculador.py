from tkinter import Frame, Button, Tk, StringVar, Entry, RIGHT, TOP, messagebox

class Calculadora:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")
        self.resultado = ''
        self.valor_tela = StringVar()
        self.btns = [
            
        ]
        
        self.container0 = Frame(master, width=250, height=83, bd=0, highlightbackground='black', highlightcolor='black', highlightthickness=1)
        self.container0.pack(side=TOP)

        self.container1 = Frame(master, width=250, height=400, bg='grey')
        self.container1.pack()

        # Tela
        self.tela = Entry(self.container0, font=('arial', 18, 'bold'), textvariable=self.valor_tela, width=250, bg='#eee', bd=0, justify= RIGHT)
        self.tela.pack(ipady=10)
    
        #Coluna 1
        self.btn_limpar = Button(self.container1, text='C', fg="black", width=44, height=3, bd=0, cursor="hand2", command=lambda: self.btn_clear()).grid(row=0, column=0,columnspan=4, padx=1, pady=1)
        self.btn_quatro = Button(self.container1, text='4', fg="black", width=10, height=3, bd=0,cursor='hand2', command= lambda: self.btn_value_exec('4')).grid(row=2, column=0, padx=1, pady=1)
        self.btn_sete = Button(self.container1, text='7', fg="black", width=10, height=3, bd=0, cursor='hand2', command= lambda: self.btn_value_exec('7')).grid(row=1, column=0, padx=1, pady=1)
        self.btn_um = Button(self.container1, text='1', fg="black", width=10, height=3, bd=0,cursor='hand2', command= lambda: self.btn_value_exec('1')).grid(row=3, column=0, padx=1, pady=1)
        self.btn_ponto = Button(self.container1, text='.', fg="black", width=10, height=3, bd=0,cursor='hand2', command= lambda: self.btn_value_exec('.')).grid(row=4, column=0, padx=1, pady=1)
        #Coluna 2
        self.btn_oito = Button(self.container1, text='8', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('8')).grid(row=1, column=1, padx=1, pady=1)
        self.btn_cinco = Button(self.container1, text='5', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('5')).grid(row=2, column=1, padx=1, pady=1)
        self.btn_dois = Button(self.container1, text='2', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('2')).grid(row=3, column=1, padx=1, pady=1)
        self.btn_zero = Button(self.container1, text='0', fg="black", width=10, height=3, bd=0, cursor="hand2", command=lambda: self.btn_value_exec('0')).grid(row=4, column=1, padx=1, pady=1)
        #Coluna 3
        self.btn_nove = Button(self.container1, text='9', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('9')).grid(row=1, column=2, padx=1, pady=1)
        self.btn_seis = Button(self.container1, text='6', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('6')).grid(row=2, column=2, padx=1, pady=1)
        self.btn_tres = Button(self.container1, text='3', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('3')).grid(row=3, column=2, padx=1, pady=1)
        self.btn_igual = Button(self.container1, text='=', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.resultar()).grid(row=4, column=2, padx=1, pady=1)
        #Coluna 4
        self.btn_dividir = Button(self.container1, text='/', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('/')).grid(row=1, column=3, padx=1, pady=1)
        self.btn_vezes = Button(self.container1, text='*', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('*')).grid(row=2, column=3, padx=1, pady=1)
        self.btn_menos = Button(self.container1, text='-', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('-')).grid(row=3, column=3, padx=1, pady=1)
        self.btn_mais = Button(self.container1, text='+', fg="black", width=10, height=3, bd=0,cursor="hand2", command=lambda: self.btn_value_exec('+')).grid(row=4, column=3, padx=1, pady=1)

    def btn_value_exec(self, val):
        self.resultado += val
        self.valor_tela.set(self.resultado)

    def btn_clear(self):
        self.resultado = ''
        self.valor_tela.set(self.resultado)

    def resultar(self):
        try:
            self.conta = str(eval(self.resultado))
            self.valor_tela.set(self.conta)
            self.resultado = self.conta
        except:
            messagebox.showerror("Erro", "Expressão inválida")
            self.resultado = ''
            self.valor_tela.set(self.resultado)

root = Tk()
Calculadora(root)
root.geometry('310x323')
root.resizable(0,0)
root.title('Calculadora do Leo')
root.mainloop()