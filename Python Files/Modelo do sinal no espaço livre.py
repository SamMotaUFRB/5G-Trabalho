# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:32:22 2023

@author: Samuel Mota
"""
from math import pi, log10

pr = float
pt = float(input("Digite a potência de transmissão: "))
gt = float(input("Digite o ganho da transmissão: "))
gr = float(input("Digite o ganho de recepção: "))
lam = float(input("Digite o comprimento: "))
d = float(input("Digite o distância: "))

pr = (pt*gt*gr*lam**2)/(((4*pi**2))*(d**2))
print("Potência recebida: ",pr,"W")

#Atenuação no espaço livre (admensional)
l = ((4*pi)**2*d**2)/(lam**2)

lb= log10(l)
print(lb)
