# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:24:59 2023

@author: lab
"""
"""HERENCIA"""
###################################################
class Animal:
    def hablar (self):
        print("Haciendo ruido generico")
    def comer(self):
        print("Inspeccionando comida ")
    def dormir(self):
        print("Buscando donde dormir")
    def correr(self):
        print("Saliendo a correr al parque")
        
class Perro(Animal):
    def hablar(self):
        super().hablar()
        super().comer()
        print("ladrando")
        
class Gato(Animal):
    def hablar(self):
        super().hablar()
        print("Maullando..... ")
        
class Vaca(Animal):
    def hablar(self):
        super().hablar()
        print("Mujiendo")
        
class Leon(Animal):
    def hablar(self):
        super().hablar()
        print("Ruginedo..........")
    
miperro = Perro()
miperro.hablar()
mascota1 = Perro()
mascota1.hablar()
print("")

migato = Gato()
migato.hablar()
mimascota2 = Gato()
mimascota2.hablar()
print("")

mivaca = Vaca()
mivaca.hablar()
mimascota3 = Vaca()
mimascota3.hablar()
print("")

mileon = Leon()
mileon.hablar()
mimascota4 = Leon()
mimascota4.hablar()






























