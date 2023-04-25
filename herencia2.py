# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 09:51:19 2023

@author: lab
"""

"""HERENCIA2"""
###################################################

class Robot:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        
    def saludar(self):
        print(f"hola, mi nonbre es {self.nombre} y soy un robot {self.color}.")

class RobotAsistente(Robot):
    def __init__(self, nombre, color, tareas):
        super().__init__(nombre, color)
        self.tareas = tareas 
        
    def saludar(self):
        super().saludar()
        print("soy un robot asistente y estoy aqui para ayudarte.")
        
    def realizar_tareas(self):
        print(f"Realizando tareas: {self.tareas}")
        
robot1 = Robot("Robot1","Rojo")
robot1.saludar()

robot2 = RobotAsistente("Robot2","azul",["limpiar","cocinar","organizar"])  
robot2.saludar()
robot2.realizar_tareas()    