import pandas as pd
import os
import pathlib
import tabula
import camelot

pasta = pathlib.Path('D:\Tiago\Documentos\IRPF\IRPF2021')
arquivo=os.path.join(pasta, '2020.08-37984_NotaCorretagem.pdf')
df=tabula.read_pdf(arquivo,pages="all",multiple_tables=True)
print(df)

tabelas= camelot.read_pdf(arquivo, pages="all")
for i,tabela in enumerate(tabelas):
    tb = tabela.df
    print(tb)
