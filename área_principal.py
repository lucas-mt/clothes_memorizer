import tkinter as tk
from tkinter.ttk import *
from mod_files import *
from mod_time_file import *
from mod_GUI import *
from mod_read_files import *

Janela()
Rotulo('Sistema de ESTOQUE', 0, 0)

def armazena():
    Rotulo('Sistema de ARMAZENAMENTO', 0, 11)
    qqr = tipo_peca = info_peca('tipo da peça:', 12)
    cod_peca = info_peca('código da peça:', 14)
    qnt_peca = info_peca('quantidade da peça:', 15)
    prc_peca = info_peca('preço de revenda:', 16)
    vlr_peca = info_peca('valor de compra da peça:', 18)
    cria_arm_ano()
    cria_arm_mes()
    peca = Armazena(tipo_peca, cod_peca, qnt_peca, prc_peca, vlr_peca)
    botao = tk.Button(text='SALVAR', command=peca.guarda)
    botao.grid(column=1, row=19)
    deletar = Deleta(tipo_peca, cod_peca, qnt_peca, prc_peca, vlr_peca, qqr)
    ap_bt = tk.Button(text='APAGAR', command=deletar.apaga)
    ap_bt.grid(column=2, row=19)

def vende():
    Rotulo('Sistema de VENDA', 0, 22)
    tipo_peca = info_peca('tipo da peça:', 23)
    cod_peca = info_peca('código da peça:', 25)
    qnt_peca = info_peca('quantidade da peça:', 26)
    vlr_peca = prc_peca = info_peca('preço de revenda:', 27)
    dsc_peca = info_peca('desconto:', 28)
    tipo_cmp = info_peca('tipo de compra da peça:', 29)
    cria_vnd_ano()
    cria_vnd_mes()
    peca = Venda(tipo_peca, cod_peca, qnt_peca, prc_peca, vlr_peca, tipo_cmp, dsc_peca)
    botao = tk.Button(text='SALVAR', command=peca.guarda)
    botao.grid(column=1, row=30)
    deletar = Deleta(tipo_peca, cod_peca, qnt_peca, prc_peca, tipo_cmp, dsc_peca)
    ap_bt = tk.Button(text='APAGAR', command=deletar.apaga)
    ap_bt.grid(column=2, row=30)

def estoque():
    Rotulo('ESTOQUE', 0, 34)
    dia = dia_arq()
    mes = mes_arq()
    ano = ano_arq()
    arq_arm = Est_arm(dia, mes, ano)
    arq_vnd = Est_vnd(dia, mes, ano)
    b_arm = Button(janela, text='armazenado', command=arq_arm.mostra)
    b_arm.grid(column=1, row=38)
    b_vnd = Button(janela, text='vendido', command=arq_vnd.mostra)
    b_vnd.grid(column=2, row=38)
    deletar = Del_data(dia, mes, ano)
    ap_bt = tk.Button(text='APAGAR', command=deletar.apaga)
    ap_bt.grid(column=1, row=39, columnspan=2)

bt1 = Button(janela, text='armazenar', command=armazena)
bt1.grid(columnspan=2)
bt2 = Button(janela, text='vender', command=vende)
bt2.grid(columnspan=2)
bt3 = Button(janela, text='estoque', command=estoque)
bt3.grid(columnspan=2)

loop()
