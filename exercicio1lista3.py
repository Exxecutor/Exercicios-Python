# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 16:18:08 2020

@author: Vitor
"""
pot=1
final=0
n=int(input("Insira um número (binário):"))
while n!=0:
    final=final+n%10*pot
    n=n//10
    pot=pot*2
print("Seu número na base decimal é %s " %(final))
