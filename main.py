#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:23:09 2020

@author: ricardo
"""

import pygame
import menu
import game 

game = game.Game()

while game.running: # .running (original) DEBUG with .playing
    game.menu_state.menu_options_display()
    game.game_loop()

pygame.quit()                                
# win = pygame.display.set_mode((1000,1000))

# # images 

# ship = [pygame.image.load('Images/ship.png')]

# #sounds

# pygame.mixer.init()
# pygame.mixer.music.load('sounds/spaceinvaders1.ogg')
# pygame.mixer.music.play()

# pygame.init()

# class Ship(pygame.sprite.Sprite):
#     def __init__(self, pos):
#         self.pos = pos     
#         # self.music = 

# def main():
#     run = True 
    # while run:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             run = False
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_LEFT]:
    #           pygame.mixer.music.fadeout(1000)
    # pygame.quit()

# main()
