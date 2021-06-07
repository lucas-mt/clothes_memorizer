#módulo do front-end.
import tkinter as tk, os
from tkinter.ttk import *
from pathlib import Path

os.chdir(f'{Path.home()}/OneDrive/Documentos')
home = os.getcwd()

janela = tk.Tk()

#aqui, o título da janela
def Janela():
    janela.title('VITRINE Online')
    janela.geometry('320x450')
    #janela.iconbitmap(f'{home}\\VIT app\\icons\\vitrine_ícone-v.ico')

#aqui é o título da página
def Rotulo(msg, col, lin):
    rotulo = tk.Label(text=msg, font=(10))
    rotulo.grid(column=col, row=lin, columnspan=2)

#aqui faz as caixas com as mensagens
def info_peca(msg, col):
    info = tk.Label(text=msg)
    txt = tk.Entry()
    info.grid(column=0, row=col, sticky='e')
    txt.grid(column=1, row=col, columnspan=2)
    return txt

#aqui é o loop para que a janela não feche
def loop():
    janela.mainloop()

class Est_arm:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
        self.info = []
    def mostra(self):
        try:
            dia_ = self.dia.get()
            mes_ = self.mes.get()
            ano_ = self.ano.get()
            arq = open(f'{home}\\VITRINE online\\armazenamento_{ano_}\\mes_{mes_}\\armazenagem_data_{dia_}-{mes_}-{ano_}.txt', 'r', encoding='utf-8')
            Label(janela, text='Armazenado').grid(column=4, row=1)
            ler_arq = arq.read()
            container = Frame(janela)
            canvas = tk.Canvas(container)
            scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)
            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            Label(scrollable_frame, text=ler_arq).grid(column=4, row=2)
            container.grid(column=4, row=2, rowspan=50)
            canvas.grid(column=1, row=0)
            scrollbar.grid(column=1, row=0)
        except:
            txtx = Label()
            txtx.configure(text=f'Desculpa, o arquivo não foi encontrado!')
            txtx.after(2500, txtx.destroy)
            txtx.grid(column=1, columnspan=3)
        
class Est_vnd(Est_arm):
    def __init__(self, dia, mes, ano):
        Est_arm.__init__(self, dia, mes, ano)
    def mostra(self):
        try:
            dia_ = self.dia.get()
            mes_ = self.mes.get()
            ano_ = self.ano.get()
            arq = open(f'{home}\\VITRINE online\\venda_{ano_}\\mes_{mes_}\\venda_data_{dia_}-{mes_}-{ano_}.txt', 'r', encoding='utf-8')
            Label(janela, text='Vendido').grid(column=5, row=1)
            ler_arq = arq.read()
            container = Frame(janela)
            canvas = tk.Canvas(container)
            scrollbar = Scrollbar(container, orient="vertical", command=canvas.yview)
            scrollable_frame = Frame(canvas)
            scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(yscrollcommand=scrollbar.set)
            Label(scrollable_frame, text=ler_arq).grid(column=5, row=2)
            container.grid(column=5, row=2, rowspan=50)
            canvas.grid(column=1, row=0)
            scrollbar.grid(column=1, row=0)
        except:
            txtx = Label()
            txtx.configure(text=f'Desculpa, o arquivo não foi encontrado!')
            txtx.after(2500, txtx.destroy)
            txtx.grid(column=1, columnspan=3)
        