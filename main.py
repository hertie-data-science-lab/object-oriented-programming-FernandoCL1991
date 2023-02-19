# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:05:41 2023

@author: Hannah
"""

## moves are randomized
## just three players: none, bear, fish
## if there is a fish vs fish: they stay where they are and +1 in random none
## if there is a fish vs bear: they stay where they are and +1 in random none


from River import River

river = River(5)
river.initialize()
river.display()

river.next_time_step(10)