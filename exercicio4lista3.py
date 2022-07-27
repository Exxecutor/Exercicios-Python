# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 16:07:43 2020

@author: Vitor
"""
nmul=0
nhom=0
num=1
quanthome=0
somahom=0
quantmul=0
somamul=0
itn="s"
mulvel=150
while itn=="s":
    print("--------Canditato número %s--------"%(num))
    idade=int(input("Insira a idade do candidato:"))
    sexo=str(input("Insira masculino ou feminino(m/f):"))
    exp=str(input("Tem experiencia (s/n):"))
    itn=str(input("Deseja continuar (s/n):"))
    num+=1
    if itn=="n":
        itn="n"
    else:
        if sexo=="f":
             nmul+=1
        if sexo=="m":
             nhom+=1
        if sexo=="m" and exp=="s":
             somahom+=idade 
             quanthome+=1
        if sexo=="f" and exp=="s":
             somamul+=idade 
             quantmul+=1
        if sexo=="f" and exp=="s" and idade<mulvel:
             mulvel=idade
mediahom=(somahom/quanthome)
mediamul=(somamul/quantmul)
print("O número de mulheres é de %s"%(nmul))
print("O número de homens é de %s"%(nhom))
print("A idade média de homens com experiencia é de %s anos "%(mediahom))
print("A idade média de mulheres com experiencia é de %s anos "%(mediamul))
print("A mulher mais jovem com experiencia tem %s anos . "%(mulvel))