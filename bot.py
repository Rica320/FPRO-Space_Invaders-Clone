#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:25:49 2020

@author: ricardo
"""

import keyboard


class Bot():
    def __init__(self, game):
        self.game = game

    def move(self):
        for bullet in self.game.random_bullet:
            if self.game.ship1.image.get_rect().size[0] + self.game.ship1.x <= bullet.x >= self.game.ship1.x:
                # keyboard.press_and_release('space')
                # print('okkkkkkkkkk')
                pass
