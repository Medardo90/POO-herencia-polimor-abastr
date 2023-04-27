# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 22:07:57 2023

@author: Patricio Haro
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 10:22:12 2023

@author: lab
"""

class Vehiculo:
    def __init__(self, velocidad, posicion, direccion):
        self.velocidad = velocidad
        self.posicion = posicion
        self.direccion = direccion
        
    def mover(self):
        #Implementacion generica para mover un vehiculo
        print("El vehiculo se mueve")
    
class Coche(Vehiculo):
    def __init__(self,velocidad, posicion, direccion, num_ruedas):
        super().__init__(velocidad, posicion, direccion)
        self.num_ruedas = num_ruedas
        
    def conducir(self):
        #implementacion especifica para conducir un coche
        print("El auto inicio la conduccion")
     
class Moto(Vehiculo):
    def __init__(self,velocidad, posicion, direccion,forma_control):
        super().__init__(velocidad, posicion, direccion)
        self.forma_control=forma_control
        
    def acelerar(self):
        #Implementacion especifica para acelerar una moto
        print("La moto esta acelerando")
        
coche1= Coche(velocidad= 100, posicion =(0, 0), direccion= "norte", num_ruedas=4 )
moto1 = Moto(velocidad= 90, posicion =(10, 20), direccion= "sur", forma_control= "manubrio")

print(coche1.velocidad)
print(moto1.posicion)

coche1.conducir()
moto1.acelerar()
