import sys
import os
from cx_Freeze import setup, Executable

# Definir o que deve ser incluído na pasta final
# Saida de arquivos
configuracao = Executable(
    script='pythonista.py',
    icon='python.ico'
)
# Configurar o executável
setup(
    name='Automatizador de login',
    version='1.0',
    description='Este programa automatiza o login deste site',
    author='Marcos Martins',
    options={'build_exe':{
        'include_msvcr': True
    }},
    executables=[configuracao]
)