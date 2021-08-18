# -*- coding: utf-8 -*- 
import pandas as pd
import os 


def initialize():
    global empresas_list
    f = open(str(os.path.dirname(os.path.realpath(__file__))) + '/database/Empresas.txt','r',encoding = 'utf-8')
    empresas_list = f.read().split(',')
    empresas_list.sort()
    f.close()
    return empresas_list    
        
def add_empresa(new_empresa):
    f = open(str(os.path.dirname(os.path.realpath(__file__))) + '/database/Empresas.txt','a')
    f.write(',' + new_empresa)
    f.close()

def pick_database(value):
    Empresa = empresas_list[value]
    df = pd.read_excel (os.path.dirname(os.path.realpath(__file__)) + '/database/Base empresas xls/' + Empresa + '.xlsx')
    Equipos = df['Equipo']
    for i in range(len(Equipos)):
        Equipos[i]=str(Equipos[i])
    Componente = df['Componente']
    PE = df['P.E']
    returnable = []
    for i in range(0,len(Equipos)):
        returnable.append(Equipos[i].encode('utf-8') + ' ' + Componente[i].encode('utf-8') + ' ' + PE[i].encode('utf-8'))

    return returnable

def numerar_list(raw_list, ordered_list):
    int_list = []
    for muestra  in raw_list:
        for i in range (len(raw_list)):
            if muestra == ordered_list[i][0]:
                int_list.append(i+1)
    return int_list

