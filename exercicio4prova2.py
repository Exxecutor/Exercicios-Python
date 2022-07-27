# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 15:28:14 2020

João Victor Fagundes Nascimento 135926
Felipe Gragnani
Fernando Santoro

"""

print("O número inserido é primo ou não-primo")
num=int(input("Insira um número (maior que 0):"))
primo=True
divisor=2
while divisor<num and primo== True:
    if num%divisor==0:
        primo= False
    divisor+=1
if primo==True and num!=1:
    print("O número é primo")
else:
    print("O número não é primo")


