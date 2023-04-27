# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class Arbol:
    def __init__(self,especies, edad, altura, tipo_arbol):
        self.especies = especies
        self.edad = edad
        self.altura = altura
        self.tipo_arbol = tipo_arbol
        
    def crecer(self,especies, edad, altura, tipo_arbol):
        print("El arbol de esta creciendo")
        
    def mover(self,especies, edad, altura, tipo_arbol):
        print("El arbol se esta moviendose a la derecha")
        
    def fabricacion(self,especies, edad, altura, tipo_arbol):
        print("El arbol esta listo para la fabricacion")
        
    def edad_tala(self,especies, edad, altura, tipo_arbol):
        print("El arbol sera talado a la edad de 30 años para la fabricacion de madera preparada")
    
    def coecha_frutos(self,especies, edad, altura, tipo_arbol):
         print("El arbol esta listo para la cosecha de frutos")
         
arbol1 = Arbol(especies = "Pino",edad = 12, altura = 20, tipo_arbol = "Madera")
print(arbol1.edad)
arbol1.altura()









# coche1= Coche(velocidad= 100, posicion =(0, 0), direccion= "norte", num_ruedas=4 )
# moto1 = Moto(velocidad= 90, posicion =(10, 20), direccion= "sur", forma_control= "manubrio")

# print(coche1.velocidad)
# print(moto1.posicion)

# coche1.conducir()
# moto1.acelerar()