#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:19:05 2020

@author: ricardo
"""
import pygame


class Menu():
    ''' A class that defines a menu and it's atributes'''

    def __init__(self, game):
        pygame.mouse.set_visible(False)
        self.game = game
        self.running_display = True
        #  self.music = True  # if the user wants...and fadout when moving to play
        self.back_music = 'sounds/spaceinvaders1.ogg'

    def menu_options_display(self):
        ''' Creates a menu window '''
        self.running_display = True  # ADD STOP
        if self.game.music:
            self.background_sound()
        while self.running_display:
            self.game.events()
            self.game.display.fill(self.game.COLOR)
            self.game.blit_text("space_invaders.ttf",
                                f"Hi-score:{self.game.hi_score}",
                                30, 500, 100)
            self.game.blit_text("space_invaders.ttf", "'f' to fit the screen",
                                25, 500, 200)
            self.game.blit_text("Invaders-From-Space.ttf", "A", 350, 500, 400)
            self.game.blit_text("space_invaders.ttf", "Press 'i' to play",
                                40, 500, 560)
            self.game.blit_text("space_invaders.ttf", "Press 'b' to play the Bot",
                                40, 500, 660)
            self.game.blit_text("space_invaders.ttf",
                                f"Music ('m')-->{'On' if self.game.music else 'Off'}",
                                25, 800, 900)
            self.game.blit_text("space_invaders.ttf",
                                "'q' to leave",
                                25, 150, 900)
            self.update_everything()

    def background_sound(self):
        ''' Loads and plays the Background music '''
        pygame.mixer.music.load(self.back_music)
        pygame.mixer.music.play(-1)

    def update_everything(self):
        ''' Update Method '''
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
