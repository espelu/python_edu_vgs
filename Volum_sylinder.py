# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:23:35 2020

@author: Espen Lunden
"""

#Oppgave: Vi skal lage en tønne for oppbevaring av dette kraftfór. Denne skal stå i stallen hvor det er begrenset plass. Derfor må ikke diameteren på tønnen overgå 1 meter. 
# I tillegg ønsker vi at vekten på tønnen når den er full med kraftfór skal veie 1 tonn.
# Hvilken høyde og radius passer for vår tønne? oppgi svarene i meter.
# Vi anseer tønnen som en perfekt sylinder. 1 liter kraftfor veier 0,7 kg
# 
import numpy as np

pi = np.pi
#print(pi)

maks_vekt = 1000
maks_liter = maks_vekt/0.7
maks_volum_meter = maks_liter/1000

#Skrive ut formelen
def areal_sirkel(radius):
    return pi*radius*radius
# Kan skrives som en funksjon som vi kan 
def volum_sylinder(radius, høyde):
    Volum = areal_sirkel(radius)*høyde
    print('Volumet av sylinderen er:', Volum)
    
diameter = 1
maks_radius = diameter/2
høyde = int(input('høyde i meter:'))
radius = int(input('rad i meter:'))
#
if radius > maks_radius:
    print('Denne tønnen har for stor diameter')
#
#else:
#        volum = volum_sylinder(radius, høyde)
##Denne funksjonen beregner volumet av en kule
#
## vi må bestemme radiusen
## vi må ha pi
#
## Her har vi formelen 
#
#
#    
#print('Maks volum:', maks_volum_meter)
#print(')
#If Volum > maks_volum_meter
#    print('du må redusere størrelsen)
#    
#else if Volum < 