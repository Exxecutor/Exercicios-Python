# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 09:15:41 2018

@author: alunosbs
"""
agenda={'Maria' : 99887766 , 'Pedro' : 9234678 , 'Joaquim' : 99887711 , 'Teresa' : 991388534}
nome=(input("Insira o nome para a busca pelo número:"))
print(nome , agenda[nome])
if nome=="Pedro" :
    print("O numero de %s estava errado , insira um novo número" %(nome))
    novonumero=int(input("Insira um novo número para %s :" %(nome)))
    agenda['Pedro']=novonumero
    print("O numero novo de %s é %s " %(nome , agenda['Pedro']))
    
