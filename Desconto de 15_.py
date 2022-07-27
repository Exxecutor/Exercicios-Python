# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 20:48:44 2018

@author: alunosbs
"""
valor=float(input("Insira o valor do produto:"))
desconto1=valor*15
desconto2=desconto1/100
desconto3=valor-desconto2
print("O valor do seu produto com o desconto é de R$ %s"%(desconto3))

