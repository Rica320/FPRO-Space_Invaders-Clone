#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:01:20 2020

@author: ricardo
"""
import pygame

pygame.init()

class StarShip(pygame.sprite.Sprite):
    def __init__(self,x, y):
        super().__init__()
        self.image = pygame.image.load("Images/ship.png")
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.rect = self.image.get_rect()
        self.y = y
        self.x = x
    
    def shoot(self):
        self.shoot_sound.play()
        
    def update(self):
        self.rect.center = self.x, self.y
        
# ship = StarShip(400)
# ship_g = pygame.sprite.Group()
# ship_g.add(ship)
# screen = pygame.display.set_mode((1000,1000))
# run = True
# clock = pygame.time.Clock()
# su = pygame.Surface((1000,1000))
# su.fill((40,0,0))
# ship2 = StarShip(300)
# ship_g.add(ship2)
# while run:
#     clock.tick(27)
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT]:
#         for el in ship_g:
#             el.x += -5
        
#     elif key[pygame.K_RIGHT]:
#         for el in ship_g:
#             el.x += +5
   
#     if key[pygame.K_SPACE]:
#         ship.shoot()

        
#     pygame.display.flip()
#     screen.blit(su, (0,0))
#     ship_g.draw(screen)
#     ship_g.update()
    
# pygame.quit()
        
        