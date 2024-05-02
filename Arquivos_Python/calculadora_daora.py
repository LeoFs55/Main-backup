from tkinter import *

def oi():
    print('olá')

janela = Tk()
janela.geometry("320x500")
janela.title('Calculadora')
receive = ''
border_tela = Frame(janela, background="black")
label = Label(border_tela, text=receive, bd=0, width=35, height=7)
label.pack(padx=3, pady=3)
border_tela.pack(padx=40, pady=19)

# border_teclado = Frame(janela, background="black")
# label2 = Label(border_teclado, text=receive, bd=0, width=37, height=26)
# label2.pack(padx=3, pady=3)
# border_teclado.pack(padx=40, pady=19)

btn_1 = Button(janela, text= '1', command=oi,width=20)
btn_1.pack(padx=20,pady=19)
janela.grid_rowconfigure(10,weight=1)




janela.mainloop()