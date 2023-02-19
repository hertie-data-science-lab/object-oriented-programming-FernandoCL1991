# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:02:49 2023

@author: Hannah
"""

# Importing libraries
from abc import ABCMeta, abstractmethod
from random import random

class Creature(metaclass = ABCMeta):
    def __init__(self, index):
        self.index = index
        self.type = "None"


  
        
class Bear(Creature):

    def __init__(self, index): # INSTANCE ATTRIBUTES
        self.type = "bear"

    def move(self, river, position): # INSTANCE METHODS
        new_position = random.choice([i-1, i, i+1])
        if new_position >= 0 and new_position < len(river):
            if river[new_position] is None:
                river[new_position] = self




class Fish(Creature):

    def __init__(self, index):
        self.type = "fish"

    def move(self, river, i):

