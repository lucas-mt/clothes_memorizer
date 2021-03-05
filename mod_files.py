#módulos de cadastramento e informações das peças aramzenadas e vendidas.
import tkinter as tk
import time
from mod_read_files import virg

agora = time.localtime()

class Armazena:
    def __init__(self, tipo, codigo, quantidade, preco, valor):
        self.tipo = tipo
        self.cod = codigo
        self.qnt = quantidade
        self.prc = preco
        self.vlr = valor
    def guarda(self):
        tipo_ = self.tipo.get()
        codigo_ = self.cod.get()
        quantidade_ = self.qnt.get()
        preco_ = self.prc.get()
        valor_ = self.vlr.get()
        if tipo_ == '' or codigo_ == '' or quantidade_ == '' or preco_ == '' or valor_ == '':
            aviso = tk.Label()
            aviso.configure(text='há informações faltando!')
            aviso.after(3000, aviso.destroy)
            aviso.grid(column=1, columnspan=2)
        else:
            try:
                with open(f'C:\\Users\\Cliente\\OneDrive\\Documentos\\VITRINE online\\armazenamento_{agora.tm_year}\\mes_{agora.tm_mon}\\armazenagem_data_{agora.tm_mday}-{agora.tm_mon}-{agora.tm_year}.txt', 'a+', encoding='utf-8') as arm_peca:
                    arm_peca.write(f'''
                    tipo...............{tipo_}
                    código.............{codigo_}
                    quantidade.........{quantidade_}
                    preço..............R${preco_}
                    valor de compra....R${valor_}
                    total..............R${int(quantidade_)*virg(preco_)}\n''')
                    arm_peca.write('-'*40)
                aviso = tk.Label()
                aviso.configure(text='Salvo com sucesso!')
                aviso.after(3000, aviso.destroy)
                aviso.grid(column=1, columnspan=2)
            except Exception as erro:
                aviso = tk.Label()
                aviso.configure(text=f'o erro {erro} ocorreu!')
                aviso.after(3000, aviso.destroy)
                aviso.grid(column=1, columnspan=2)

class Venda(Armazena):
    def __init__(self, tipo, codigo, quantidade, preco, valor, compra, desconto):
        Armazena.__init__(self, tipo, codigo, quantidade, preco, valor)
        self.cmp = compra
        self.dsc = desconto
    def guarda(self):
        tipo_ = self.tipo.get()
        codigo_ = self.cod.get()
        quantidade_ = self.qnt.get()
        preco_ = self.prc.get()
        compra_ = self.cmp.get()
        desconto_=self.dsc.get()
        if tipo_ == '' or codigo_ == '' or quantidade_ == '' or preco_ == ''  or compra_ == '' or desconto_ == '':
            aviso = tk.Label()
            aviso.configure(text='Há informações faltando!')
            aviso.after(3000, aviso.destroy)
            aviso.grid(column=1, columnspan=2)
        else:
            try:
                with open(f'C:\\Users\\Cliente\\OneDrive\\Documentos\\VITRINE online\\venda_{agora.tm_year}\\mes_{agora.tm_mon}\\venda_data_{agora.tm_mday}-{agora.tm_mon}-{agora.tm_year}.txt', 'a+', encoding='utf-8') as arm_peca:
                    arm_peca.write(f'''
                    tipo...............{tipo_}
                    código.............{codigo_}
                    quantidade.........{quantidade_}
                    preço..............R${preco_}
                    desconto...........{desconto_}%
                    tipo de compra.....{compra_}
                    total..............R${int(quantidade_)*virg(preco_, desconto_)}\n''')
                    arm_peca.write('-'*40)
                aviso = tk.Label()
                aviso.configure(text=f'total: R${int(quantidade_)*virg(preco_, desconto_)}\nSalvo com sucesso!')
                aviso.after(3000, aviso.destroy)
                aviso.grid(column=1, columnspan=2)
            except Exception as erro:
                aviso = tk.Label()
                aviso.configure(text=f'o erro {erro} ocorreu!')
                aviso.after(3000, aviso.destroy)
                aviso.grid(column=1, columnspan=2)

class Del_data:
    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3        
    def apaga(self):
        self.n1.delete(0, 'end')
        self.n2.delete(0, 'end')
        self.n3.delete(0, 'end')

class Deleta(Del_data):
    def __init__(self, n1, n2, n3, n4, n5, n6):
        Del_data.__init__(self, n1, n2, n3)
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
    def apaga(self):
        self.n1.delete(0, 'end')
        self.n2.delete(0, 'end')
        self.n3.delete(0, 'end')
        self.n4.delete(0, 'end')
        self.n5.delete(0, 'end')
        self.n6.delete(0, 'end')
