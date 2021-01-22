#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:25:49 2020

@author: ricardo
"""

import keyboard


class Bot():
    '''
    Creates the process of thinking of the Bot.
    The keyboard module is used to simulate the inputs of a user.
    '''

    def __init__(self, game):
        self.game = game
        self.this = 'right'

    def move(self, aliens_left):
        '''
        Defines the responses of the bot to different events.
        The bot will always shot until only 4 aliens are left out.
        '''
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
        for alien in self.game.alien_g:
            up = round(self.game.ship1.x + (self.game.ship1.y - alien.y)/10 * alien.vel)
            less = round(self.game.ship1.x - (self.game.ship1.y - alien.y)/10 * alien.vel)
            if less <= alien.x <= up:
                keyboard.press('space')
        if aliens_left >= 4:
            keyboard.press('space')
