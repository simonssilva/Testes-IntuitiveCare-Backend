from encodings import utf_8
import tabula
import os
import pandas as pd
import shutil

anexo = 'Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'
DIR = os.path.join ('Anexos', anexo)

paginas = '3-200'
tables = tabula.read_pdf(DIR, pages=paginas, encoding='ISO-8859-1', lattice=True, stream=False)

df = pd.concat(tables)
df.to_csv('Teste_Simon.csv', sep=';', encoding='utf_8')

shutil.make_archive('Teste_Simon', 'zip', './', 'Teste_Simon.csv')
