#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:23:09 2020

@author: ricardo
"""

import pygame
import game

game = game.Game()

while game.running:
    game.menu_state.menu_options_display()
    game.game_loop()

pygame.quit()
