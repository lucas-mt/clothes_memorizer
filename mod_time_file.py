#módulo para verificação e atualização de data de estocagem.
import time, os.path, os
from pathlib import Path

os.chdir(f'{Path.home()}/OneDrive/Documentos')
home = os.getcwd()
agora = time.localtime()

#verifica se já existe a pasta de destino, caso não, é criada.
try:
    os.mkdir(f'{home}/VITRINE online/')
except FileExistsError:
    pass
finally:
    def cria_arm_ano():
        if not os.path.exists(f'{home}/VITRINE online/armazenamento_{agora.tm_year}/'):
            os.mkdir(f'{home}/VITRINE online/armazenamento_{agora.tm_year}/')

    def cria_arm_mes():
        if not os.path.exists(f'{home}/VITRINE online/armazenamento_{agora.tm_year}/mes_{agora.tm_mon}'):
            os.mkdir(f'{home}/VITRINE online/armazenamento_{agora.tm_year}/mes_{agora.tm_mon}')

    def cria_vnd_ano():
        if not os.path.exists(f'{home}/VITRINE online/venda_{agora.tm_year}/'):
            os.mkdir(f'{home}/VITRINE online/venda_{agora.tm_year}/')

    def cria_vnd_mes():
        if not os.path.exists(f'{home}/VITRINE online/venda_{agora.tm_year}/mes_{agora.tm_mon}'):
            os.mkdir(f'{home}/VITRINE online/venda_{agora.tm_year}/mes_{agora.tm_mon}')
