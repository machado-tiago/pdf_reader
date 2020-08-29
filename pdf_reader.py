import pandas as pd
import os
import pathlib
import tabula
#import camelot
import PyPDF2
import numpy as np

class mes(object):
    def __init__(self):
        super().__init__()
        self.dias=[]
    pass

    def lerNota(self):
        pasta = pathlib.Path('D:\Tiago\Documentos\IRPF\IRPF2021')
        arquivo=os.path.join(pasta, '2020.08-37984_NotaCorretagem.pdf')
        lista=tabula.read_pdf(arquivo,pages="all",multiple_tables=True)
        for i,tabela in enumerate(lista):
            tb = pd.DataFrame(tabela)
            #print(tb)
            if ('Data pregão' in tb.columns):
                if (len(self.dias)==0):#primeiro dia
                    dia_x= dia(tb.loc[0,'Data pregão'])
                    self.novoDia(dia_x)
                    pass
                elif (tb.loc[0,'Data pregão'] != dia_x.dataPregao):#novo dia
                    dia_x= dia(tb.loc[0,'Data pregão'])
                    self.novoDia(dia_x)
                print('Data do Pregão: ' + dia_x.dataPregao)

            
            if ('Resumo Financeiro' in tb.columns):
                del tb['Unnamed: 1']
                #FALTA PEGAR O IR DE DAYTRADE     
                #IRRFDayTrade = tb[tb['Resumo dos Negócios'].str.contains("IRRF Day Trade")]
                del tb['Resumo dos Negócios']
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Taxa de liquidação'])
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Taxa de Registro'])
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Taxa de termo/opções'])
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Taxa A.N.A.'])
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Emolumentos'])
                dia_x.custos=dia_x.custos.append(tb.loc[tb['Resumo Financeiro']=='Taxa Operacional'])
                dia_x.custos.rename(columns={'Unnamed: 0':'R$','Resumo Financeiro':'Custo'},inplace=True)
                print(dia_x.custos)
            
            if ('Cliente' in tb.columns):
                dia_x.operacoes=tb.drop(tb.index[:8])
                dia_x.operacoes.columns = dia_x.operacoes.iloc[0]
                dia_x.operacoes=dia_x.operacoes.drop(dia_x.operacoes.index[0])
                print(dia_x.operacoes)

    def novoDia(self,dia):
        self.dias.append(dia)
    pass
pass


class dia(object):
    def __init__(self,dia):
        super().__init__()
        self.dataPregao=dia
        self.custos=pd.DataFrame()
        self.operacoes=pd.DataFrame()
    pass
pass


mes().lerNota()
    

#texto=PyPDF2.PdfFileReader(arquivo)
#n_paginas = texto.getNumPages()

'''
tabelas= camelot.read_pdf(arquivo, pages="all")
for i,tabela in enumerate(tabelas):
    tb = tabela.df
#    print(tb)
'''
