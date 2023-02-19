# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:04:03 2023

@author: Hannah
"""

from abc import ABCMeta, abstractmethod
from random import random
import numpy as np
from Creatures import Bear, Fish

class River:
    
    def __init__(self, n_room):
        self.n_room = n_room
        self.list = [None] * n_room

    def initialize(self):
        for i in range(self.n_room):
            random_number = random.randit(0, 2)
            if (random_number == 0):
                self.list[i] = Fish(i)
            elif (random_number == 1):
                self.list[i] = Bear
            elif (random_number == 2):
                pass;

    def display(self):
        print("===================")
        for i in self.list:
            if i == None:
                print("None")
            else:
                print(i.type)
        print("===================")

    def next_move_t(self, no_iter):
        for t in range(no_iter):
            for i in range(len(self.list)):
                animal = self.list[i]

                if animal is not None:



    # define a new method:
    #
       
        
       
    def display(self):
        print("===================")
        print("Ecosystem status:\n")
        print(self.eco, "\n")
        print("===================")