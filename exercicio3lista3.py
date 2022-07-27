# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:50:15 2020

@author: Vitor
"""
n=int(input("Insira um número:"))
i=1
while i*(i+1)*(i+2)<n:
    i=i+1
if i*(i+1)*(i+2)==n:
    print("%s é produto de %s,%s e %s"%(n,i,i+1,i+2))
else:
    print("O número não é triangular")