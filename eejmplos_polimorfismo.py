# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 21:55:02 2023

@author: Patricio Haro
"""

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def __repr__(self):
        return f"el nombre es {self.nombre}"

    def Moverse(self):
        print("El animal se esta moviendo")

class Perro(Animal):

    def Moverse(self):
        print(f"El perro {self.nombre} camina")

class Pez(Animal):

    def Moverse(self):
        print(f"El pez {self.nombre} nada")
        
class Reptil(Animal):
    
    def Moverse(self):
        print(f"El reptil {self.nombre} se arrastra")
        
def trabajaAnimal(animal):
    print(animal)
    animal.moverse()
    
print("Que mascota quieres ")
print("1-Perro, 2-Pez, 3-Reptil")
op = int(input())
nombre = input("Que nombre tiene?")

if op == 1 :
    miMascota=Perro(nombre)
elif op == 2:
    miMascota=Pez(nombre)
else:
    miMascota=Reptil(nombre)
    
""" Invocamos a trabajaanimal que funciona 
forma polimorfica"""

trabajaAnimal = (miMascota)
print("-------------")

m1 = Perro ("Max")
m2 = Pez ("Moby")
m3 = Reptil("Draco")
mascotas = [m1,m2,m3]

for mascota in mascotas:
    print(mascota)
    mascota.Moverse()