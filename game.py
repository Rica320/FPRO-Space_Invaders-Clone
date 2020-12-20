#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:21:03 2020

@author: ricardo
"""

import pygame
import menu
import sprites

class Game():
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.running, self.playing = True, False # DEBUGGING
        self.UP_KEY, self.DOWN_KEY = False, False # to use in menu
        self.RIGHT_KEY, self.LEFT_KEY = False, False # to use in menu
        self.WIN_W, self.WIN_H = 1000, 1000
        self.display = pygame.Surface((self.WIN_W, self.WIN_H))
        self.window = pygame.display.set_mode((self.WIN_W, self.WIN_H))
        self.font_name = "Invaders-From-Space.ttf"
        self.BACK_KEY = False
        self.COLOR = (0,0,0)
        self.music = True # change this 
        self.TEXT_COLOR = (0,255,255)
        self.menu_state = menu.Menu(self)
        self.clock = pygame.time.Clock()
        self.ship1_x, self.ship1_y = 500, 900
        self.ship1 = sprites.StarShip(self.ship1_x, self.ship1_y) # x defined for future changes
        self.ship_group = pygame.sprite.Group()
        self.ship_group.add(self.ship1) # Leaves the option for a second player
        self.vel = 5
        
    def game_loop(self):
        while self.playing:
            self.clock.tick(60)
            self.events()
            if self.BACK_KEY:
                self.ship1.x, self.ship1.y = self.ship1_x, self.ship1_y
                self.playing= False
            self.update_funct()            
    
    def background_sound(self):
        # pygame.mixer.music.load('')
        # pygame.mixer.music.play()
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.menu_state.running_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_SPACE:
                    self.playing = True
                    self.menu_state.running_display = False
                    pygame.mixer.music.fadeout(1000)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.ship1.x += - self.vel                
        elif key[pygame.K_RIGHT]:
            self.ship1.x += self.vel
        if key[pygame.K_SPACE]:
            self.ship1.shoot()
                
                    
    def blit_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        screen_text = font.render(text, True, self.TEXT_COLOR)
        text_rect = screen_text.get_rect()
        text_rect.center = (x,y)
        self.display.blit(screen_text, text_rect)
    
    def update_funct(self):
        self.display.fill(self.COLOR)
        pygame.display.flip()
        self.window.blit(self.display, (0,0)) # NOTA : Garantir posição (0,0)
        self.ship_group.draw(self.window)
        self.ship_group.update()
        pygame.display.update()
        self.BACK_KEY = False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    