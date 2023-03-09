# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 08:32:22 2023

@author: Samuel Mota
"""
from math import pi, log10
"""
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
#Quando em Log(dB)
lb= log10(l)
print(lb)
"""

# Calculo da pontência recebida em um ponto de referencia:
pr = float
ppr = float(input("Digite a potência no ponto de referência:  "))
d = float(input("Digite o distância: "))
do = float(input("Digite o distância do ponto de referência: "))
beta = 2

pr = (ppr*pow(do,beta))/(pow(d,beta))
print(pr)
#Quando em Log(dB)
d1 = d/do
lb = -10*beta*log10(d/do)
print(lb, "dB")

"""

Ambiente:                                Beta:
                
Outdoor           Espaço Livre
               
2
Área urbana
2,7 a 5
Indoor
LOS
1,6 a 1,8
Obstruído
4 a 6
"""
