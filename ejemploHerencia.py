# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:22:12 2023

@author: lab
"""

class Vehiculo:
    def __init__(self, velocidad, posicion, direccion, nruedas, fcontrol):
        self.velocidad = velocidad
        self.posicion = posicion
        self.direccion = direccion
        self.nruedas = nruedas
        self.fcontrol = fcontrol
    
class Coche(Vehiculo):
    def __init__(self,nruedas):
        self.nruedas = nruedas
        
    def conducir():
        print("estoy conduciendo")
     
class Moto(Vehiculo):
    def __init__(self,fcontrol):
        self.fcontrol=fcontrol
        
    def acelerar():
        print("estoy acelerando")
        
        
coche1= Coche()
coche1.conducir()
