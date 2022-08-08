
#Importando o tkinter
from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

# Importando views
from view import *

# cores
co0 = "#f0f3f5" 
co1 = "#feffff"  
co2 = "#4fa882"  
co3 = "#38576b"  
co4 = "#403d3d"   
co5 = "#e06636"   
co6 = "#038cfc"   
co7 = "#ef5350"   
co8 = "#263238"   
co9 = "#e9edf5"   

# Criando janela 
janela = Tk()
janela.title("")
janela.geometry("600x453")
janela.configure(background=co9)
janela.resizable(width=False, height=False)

# Dividindo a janela
frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=800, height=403, bg=co1, relief='flat')
frame_direita.grid(row=0, column=1, rowspan=2, sticky=NSEW, padx=1, pady=0)

# Label de cima
app_nome = Label(frame_cima, text='Sistema de Registro de Notas', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

# Variável tree global
global tree

# Função inserir
def inserir():
    nome = e_nome.get()
    nota = e_nota.get()

    lista = [nome, nota]

    if nome == '':
        messagebox.showerror('Erro!', 'Por favor insira o nome do aluno.')
    else: 
        inserir_info(lista)
        messagebox.showinfo('Tudo pronto!', ' A nota do  aluno foi registrada com sucesso.')


        e_nome.delete(0,'end')
        e_nota.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

# Função atualizar
def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario =  tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = tree_lista[0]

        e_nome.delete(0,'end')
        e_nota.delete(0,'end')

        e_nome.insert(0,tree_lista[1])
        e_nota.insert(0, tree_lista[2])

        def update():
            nome = e_nome.get()
            nota = e_nota.get()

            lista = [nome, nota, valor_id]

            if nome == '':
                messagebox.showerror('Erro!', 'Por favor insira o nome do aluno.')
            else: 
                atualizar_info(lista)
                messagebox.showinfo('Tudo pronto!', ' A nota do aluno foi atualizada com sucesso.')


                e_nome.delete(0,'end')
                e_nota.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()
                mostrar()

        b_comfirmar = Button(frame_baixo, command=update, text='Confirmar', anchor=NW, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_comfirmar.place(x=123, y=240)

        

    except IndexError:
        messagebox.showerror('Erro!', 'Por favor selecione uma das notas que deseja alterar.')

# Funçao atualizar
def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario =  tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_id = [tree_lista[0]]

        deletar_info(valor_id)
        messagebox.showinfo('Tudo pronto!', ' A nota do aluno foi deletada com sucesso.')

        for widget in frame_direita.winfo_children():
            widget.destroy()

        mostrar()

    except IndexError:
        messagebox.showerror('Erro!', 'Por favor selecione uma das notas que deseja alterar.')

# Frame de baixo

#Nome
#l_nome significa label_nome e e_nome significa entry_nome.
l_nome = Label(frame_baixo, text='Nome do Aluno: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=50)

e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=80)

#Nota
#l_nome significa label_nome e e_nome significa entry_nome.

l_nota = Label(frame_baixo, text='Nota: ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nota.place(x=10, y=130)

e_nota = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nota.place(x=15, y=160)

# Botão inserir
b_inserir = Button(frame_baixo, command=inserir, text='Inserir', font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=200)

# Botão atualizar
b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', anchor=NW, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=120, y=200)

# Botão deletar
b_deletar = Button(frame_baixo, command=deletar, text='Deletar', anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=240, y=200)


# Frame direita
def mostrar():

    global tree

    lista = mostrar_info()

    # lista para cabecario
    tabela_head = ['ID', 'Nome', 'Nota']


    # criando a tabela
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")

    tree.grid(column=0, row=0, sticky='nsew')
    
    frame_direita.grid_rowconfigure(0, weight=12)


    hd=["nw","nw","nw"]
    h=[50,100,150]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista:
        tree.insert('', 'end', values=item)

# Chanando a função mostrar
mostrar()

janela.mainloop()