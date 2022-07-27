# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:02:58 2018

@author: alunosbs
"""
prova1=float(input("Insira o valor da primeira prova:"))
prova2=float(input("Insira o valor da segunda prova:"))
prova3=float(input("Insira o valor da segunda prova:"))
media=(prova1+prova2+prova3)/3
exame1=6-media
exame2=6+exame1
if media>=6:
    print("O aluno foi aprovado com nota %s"%(media))   
elif media<3:
     print("O aluno esta reprovado")
else:
    print("O aluno esta de exame e precisa tirar nota maior ou igual a %s"%(exame2))
    
     
