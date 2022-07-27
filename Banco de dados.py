# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 10:00:40 2018

@author: alunosbs
"""

import pandas as pd 
csv= pd.read_csv("C:\\Users\\alunosbs.PATUSKA\\Desktop\\exec2.csv" , sep=',')
print(csv)

def add_linha( Temperatura, Umidade, Vel_Vento) :
    csv.loc[len(csv)]=[ Temperatura, Umidade, Vel_Vento]
    
s_n='sim'
while s_n=='sim':
    Temperatura=int(input("Insira a temperatura:"))
    Umidade=int(input("Insira a umidade:"))
    Vel_Vento=int(input("Insira a Velocidade do Vento:"))
    add_linha( Temperatura, Umidade, Vel_Vento)
    s_n=input("Adicionar nova linha:")
print(csv)

csv.to_csv("C:\\Users\\alunosbs.PATUSKA\\Desktop\\exec2.csv")