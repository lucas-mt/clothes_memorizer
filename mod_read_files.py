#módulo para ler os arquivos.
import tkinter as tk
import time

agora = time.localtime()

#aqui pede a data
def dia_arq():
    info = tk.Label(text='dia:')
    txt = tk.Entry()
    info.grid(column=0, row=35, sticky='e')
    txt.grid(column=1, row=35, columnspan=2)
    return txt

def mes_arq():
    info = tk.Label(text='mês:')
    txt = tk.Entry()
    info.grid(column=0, row=36, sticky='e')
    txt.grid(column=1, row=36, columnspan=2)
    return txt

def ano_arq():
    info = tk.Label(text='ano:')
    txt = tk.Entry()
    info.grid(column=0, row=37, sticky='e')
    txt.grid(column=1, row=37, columnspan=2)
    return txt

def virg(vlr, dsc=0):
    if ',' in vlr:
        return float(vlr.replace(',', '.'))*(1-(int(dsc)/100))
    return float(vlr)*(1-(int(dsc)/100))
