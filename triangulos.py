# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 11:28:13 2018

@author: alunosbs
"""
a=float(input("Digite o lado A"))
b=float(input("Digite o lado B"))
c=float(input("Digite o lado C"))
if a==0 or b==0 or c==0 :
    print("Não é um triangulo")
elif a==b==c:
    print("É um triangulo equilatero")
elif a!=b==c or a==b!=c or a==c!=b :
    print("É um triangulo isóceles:")
elif a!=b!=c:
    print("É um triangulo escaleno")
                                      
    

