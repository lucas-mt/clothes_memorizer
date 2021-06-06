#módulo para verificação e atualização de data de estocagem.
import time, os.path, os

agora = time.localtime()

#verifica se já existe a pasta de destino, caso não, é criada.
try:
    os.mkdir(f'/Users/lucas/OneDrive/Documentos/VITRINE online/')
except FileExistsError:
    pass
finally:
    def cria_arm_ano():
        if not os.path.exists(f'/Users/lucas/OneDrive/Documentos/VITRINE online/armazenamento_{agora.tm_year}/'):
            os.mkdir(f'/Users/lucas/OneDrive/Documentos/VITRINE online/armazenamento_{agora.tm_year}/')

    def cria_arm_mes():
        if not os.path.exists(f'/Users/lucas/OneDrive/Documentos/VITRINE online/armazenamento_{agora.tm_year}/mes_{agora.tm_mon}'):
            os.mkdir(f'/Users/lucas/OneDrive/Documentos/VITRINE online/armazenamento_{agora.tm_year}/mes_{agora.tm_mon}')

    def cria_vnd_ano():
        if not os.path.exists(f'/Users/lucas/OneDrive/Documentos/VITRINE online/venda_{agora.tm_year}/'):
            os.mkdir(f'/Users/lucas/OneDrive/Documentos/VITRINE online/venda_{agora.tm_year}/')

    def cria_vnd_mes():
        if not os.path.exists(f'/Users/lucas/OneDrive/Documentos/VITRINE online/venda_{agora.tm_year}/mes_{agora.tm_mon}'):
            os.mkdir(f'/Users/lucas/OneDrive/Documentos/VITRINE online/venda_{agora.tm_year}/mes_{agora.tm_mon}')
