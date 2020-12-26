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

    def move(self):
        for bullet in self.game.random_bullet:
            if self.game.ship1.x - 28 <= bullet.x <= self.game.ship1.x + 28:
                rn = random.randrange(0,2)
                if rn == 0:
                    keyboard.press('left')
                else:
                    keyboard.press('right')
            if self.game.ship1.x - 28 <= bullet.x + 5 <= self.game.ship1.x + 28:
                rn = random.randrange(0,2)
                if rn == 0:
                    keyboard.press('left')
                else:
                    keyboard.press('right')
        for alien in self.game.alien_g:
            # boll_1 = abs(round((10/3)*self.game.ship1.x - self.game.ship1.y))
            # boll_2 = abs(round((10/3)*alien.x - alien.y))
            # if boll_1 == boll_2:
            #     keyboard.press('space')
            if abs((10/3)*self.game.ship1.x - self.game.ship1.y) <= abs((10/3)*alien.x - alien.y):
                keyboard.press('space')
            # if alien.x == self.game.ship1.x + 3 or alien.x == self.game.ship1.x - 3:
            #     keyboard.press('space')
        