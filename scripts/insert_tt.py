#!/usr/bin/python
# -*- coding: UTF-8 -*-

#------------------------------------------------------------------------------
# Inserir os dados do Times & Trades - Aba negocios
#
#------------------------------------------------------------------------------
# Importação das Bibliotecas
import psycopg2
#import sys
import csv

#------------------------------------------------------------------------------
# Abrindo conexão com o banco de dados
con = psycopg2.connect( host='localhost',
                        user='rodolpho',
                        password='macav810',
                        dbname='bolsa')
c = con.cursor()


# Acessando o schema
c.execute('SET SEARCH_PATH TO dolar')
con.commit()

# -----------------------------------------------------------------------------
# Funções


# Trocar caracter especial
def rmChar(txt):
    txt = txt.replace("\xc0", "A")
    txt = txt.replace("\xc1", "A")
    txt = txt.replace("\xc2", "A")
    txt = txt.replace("\xc3", "A")
    txt = txt.replace("\xc4", "a")
    txt = txt.replace("\xc7", "C")
    txt = txt.replace("\xe7", "c")
    txt = txt.replace("\xc8", "E")
    txt = txt.replace("\xc9", "E")
    txt = txt.replace("\xc1", "E")
    txt = txt.replace("\xc8", "E")
    txt = txt.replace("\xcc", "I")
    txt = txt.replace("\xcd", "I")
    txt = txt.replace("\xce", "I")
    txt = txt.replace("\xcf", "I")
    txt = txt.replace("\xd2", "O")
    txt = txt.replace("\xd3", "O")
    txt = txt.replace("\xd4", "O")
    txt = txt.replace("\xd5", "O")
    txt = txt.replace("\xd6", "O")
    txt = txt.replace("\xd9", "U")
    txt = txt.replace("\xda", "U")
    txt = txt.replace("\xdb", "U")
    txt = txt.replace("\xdc", "U")
    txt = txt.replace("\xe0", "a")
    txt = txt.replace("\xe1", "a")
    txt = txt.replace("\xe2", "a")
    txt = txt.replace("\xe3", "a")
    txt = txt.replace("\xe4", "a")
    txt = txt.replace("\xe5", "a")
    txt = txt.replace("\xe8", "e")
    txt = txt.replace("\xe9", "e")
    txt = txt.replace("\xea", "e")
    txt = txt.replace("\xeb", "e")
    txt = txt.replace("\xec", "i")
    txt = txt.replace("\xed", "i")
    txt = txt.replace("\xee", "i")
    txt = txt.replace("\xef", "i")
    txt = txt.replace("\xf2", "o")
    txt = txt.replace("\xf3", "o")
    txt = txt.replace("\xf4", "o")
    txt = txt.replace("\xf5", "o")
    txt = txt.replace("\xf9", "u")
    txt = txt.replace("\xfa", "u")
    txt = txt.replace("\xfb", "u")
    txt = txt.replace("\xfc", "u")
    txt = txt.replace("\'", "")
    return txt


def rmVirgula(num):
    num =str(num).replace(",", "")
    return num


# Arrumar data
def arrumaData(data):
    datasplit = data.split("/")
    dia, mes, ano = datasplit
    return str(ano)+'-'+str(mes)+'-'+str(dia)


#------------------------------------------------------------------------------
# Inserindo no banco de dados

ficheiro = open('/home/rodolpho/Desktop/TTneg.csv', 'rb')
dados = csv.reader(ficheiro, delimiter=';')

dados.next()

for dado in dados:
    data = arrumaData(dado[0])
    hora = dado[1]
    comprador = rmChar(dado[2])
    valor = rmVirgula(dado[3])
    quantidade = dado[4]
    vendedor = rmChar(dado[5])
    agressor = dado[6]

    #print data, hora, comprador,valor, quantidade, vendedor, agressor

    #--------------------------------------------------------------------------
    # Inserindo no banco de dados
    print('''  INSERT INTO negocios
                VALUES ('%s', '%s', %s, %s,
                            '%s', '%s', '%s') '''
            %(data, hora, valor, quantidade, comprador, vendedor, agressor))

    # Pesistindo dados no BD
    con.commit()

