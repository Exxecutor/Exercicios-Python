# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:38:59 2020

@author: Vitor
"""

x=int(input("Digite um número:"))
n=int(input("Digite um número (não negativo):"))
expoente=0
elevado=1

while expoente<n:
      expoente=expoente+1
      elevado=elevado*x
print("O resultado é %s "%(elevado))      

