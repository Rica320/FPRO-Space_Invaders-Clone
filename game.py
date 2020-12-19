#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:21:03 2020

@author: ricardo
"""
import pygame
import menu

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False # DEBUGGING
        self.UP_KEY, self.DOWN_KEY = False, False
        self.RIGHT_KEY, self.LEFT_KEY = False, False
        self.WIN_W, self.WIN_H = 1000, 1000
        self.display = pygame.Surface((self.WIN_W, self.WIN_H))
        self.window = pygame.display.set_mode((self.WIN_W, self.WIN_H))
        self.font_name = "Invaders-From-Space.ttf"
        self.BACK_KEY = False
        self.COLOR = (0,0,0)
        self.music = True # change this 
        self.TEXT_COLOR = (0,255,255)
        self.menu_state = menu.Menu(self)
        
    def game_loop(self):
        while self.playing: # TODO STOP MUSIC
            self.events()
            if self.BACK_KEY:
                self.playing= False
            self.display.fill(self.COLOR)
            self.window.blit(self.display, (0,0)) # NOTA : Garantir posição (0,0)
            pygame.display.update()
    
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
                    
                    
    def blit_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        screen_text = font.render(text, True, self.TEXT_COLOR)
        text_rect = screen_text.get_rect()
        text_rect.center = (x,y)
        self.display.blit(screen_text, text_rect)
        
                    