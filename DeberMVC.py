# -*- coding: utf-8 -*-
"""
Created on Sun Apr 30 13:23:47 2023

@author: Pablo Estrada
"""
"""model"""
#############################################################
class TemperatureModel:
    def _init__(self):
        self.filepath = "temperature_data.txt"
        
    def read_data(self):
        with open(self.filepath, "r")as file:
            data = file.read()
            return data
        
    def write_data(self,data):
        with open(self.filepath, "w")as file:
            file.write(data)

"""View"""
#######################################################
class TemperatureView:
    
    def print_data(self,data):
        print(f"TEmperature data:"{data}) 
        
"""Controlodaor"""
######################################################
class TemeperatureController:
    def __int__(self,model,view):
        self.model= model
        self.view = view
        
    def get_data(self):
        data = self.model.read_data()
        self.view.print_data(data)
        
    def set_data(self, data):
        self.model.write_data(data)
        self.view.print_data(data)