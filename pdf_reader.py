import pandas as pd
import os
import pathlib
import tabula
#import camelot
import PyPDF2

pasta = pathlib.Path('D:\Tiago\Documentos\IRPF\IRPF2021')
arquivo=os.path.join(pasta, '2020.08-37984_NotaCorretagem.pdf')
lista=tabula.read_pdf(arquivo,pages="all",multiple_tables=True)

#print(df)
for i,tabela in enumerate(lista):
    tb = pd.DataFrame(tabela)
    print(tb)
    dataPregao = tb.loc[0,'Data Pregão']
    print(dataPregao)
    

#texto=PyPDF2.PdfFileReader(arquivo)
#n_paginas = texto.getNumPages()

'''
tabelas= camelot.read_pdf(arquivo, pages="all")
for i,tabela in enumerate(tabelas):
    tb = tabela.df
#    print(tb)
'''
