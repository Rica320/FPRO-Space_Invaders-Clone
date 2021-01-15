#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:25:49 2020

@author: ricardo
"""

import keyboard
import random


class Bot():
    def __init__(self, game):
        self.game = game
        self.this = 'right'

    def move(self):
        if self.game.ship1.x <= 400:
            self.this = 'right'
        elif self.game.ship1.x >= 700:
            self.this = 'left'
            
        if all(bullet.x < self.game.ship1.x for bullet in self.game.random_bullet):
            self.this = 'right'
            
        if all(bullet.x > self.game.ship1.x for bullet in self.game.random_bullet):
            self.this = 'left'
            
        for bullet in self.game.random_bullet:
            if self.game.ship1.x - 28 <= bullet.x <= self.game.ship1.x + 28:
                keyboard.press(self.this)
            if self.game.ship1.x - 28 <= bullet.x + 5 <= self.game.ship1.x + 28:
                keyboard.press(self.this)
        
                    
            # if self.game.ship1.x - 28 <= bullet.x <= self.game.ship1.x + 28:
            #     rn = random.randrange(0,2)
            #     if rn == 0:
            #         keyboard.press(this)
            #     else:
            #         keyboard.press(that)
            # if self.game.ship1.x - 28 <= bullet.x + 5 <= self.game.ship1.x + 28:
            #     rn = random.randrange(0,2)
            #     if rn == 0:
            #         keyboard.press(this)
            #     else:
            #         keyboard.press(that)
        for alien in self.game.alien_g:
            # boll_1 = abs(round((10/3)*self.game.ship1.x - self.game.ship1.y))
            # boll_2 = abs(round((10/3)*alien.x - alien.y))
            # if boll_1 == boll_2:
            #     keyboard.press('space')
            if abs((10/3)*self.game.ship1.x - self.game.ship1.y) <= abs((10/3)*alien.x - alien.y):
                keyboard.press('space')  # TODO change 10/3 to vel/vel
            # if alien.x == self.game.ship1.x + 3 or alien.x == self.game.ship1.x - 3:
            #     keyboard.press('space')
            # if round((10/3)*self.game.ship1.x - self.game.ship1.y) == round((10/3)*alien.x - alien.y):
            #     keyboard.press('space')