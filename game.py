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
        self.running, self.playing = True, False  # DEBUGGING
        self.WIN_W, self.WIN_H = 1000, 1000
        self.display = pygame.Surface((self.WIN_W, self.WIN_H))
        self.window = pygame.display.set_mode((self.WIN_W, self.WIN_H))
        self.BACK_KEY = False
        self.COLOR = (0, 0, 0)
        self.music = True  # change this
        self.TEXT_COLOR = (0, 255, 255)
        self.menu_state = menu.Menu(self)
        self.clock = pygame.time.Clock()
        self.ship1_x, self.ship1_y = 500, 900
        self.ship1 = sprites.StarShip(self.ship1_x, self.ship1_y)
        # x defined for future changes
        self.ship_group = pygame.sprite.Group()
        self.ship_group.add(self.ship1)
        # Leaves the option for a second player
        self.vel = 5
        self.alien1 = [sprites.Aliens("Images/enemy1_1.png",
                                      "Images/enemy1_2.png",
                                      200 + x*50, 100) for x in range(11)]
        self.alien2 = [sprites.Aliens("Images/enemy2_1.png",
                                      "Images/enemy2_2.png",
                                      200 + x*50, 150) for x in range(11)]
        self.alien_g = pygame.sprite.Group()
        self.alien_g.add(self.alien1, self.alien2)

    def game_loop(self):
        self.background_sound()
        while self.playing:
            self.clock.tick(27)
            self.events()
            if self.BACK_KEY:
                self.ship1.x, self.ship1.y = self.ship1_x, self.ship1_y
                self.alien_g.remove(self.alien1, self.alien2)
                self.alien1 = [sprites.Aliens("Images/enemy1_1.png",
                                              "Images/enemy1_2.png",
                                              200 + x*50, 100)
                               for x in range(11)]
                self.alien2 = [sprites.Aliens("Images/enemy2_1.png",
                                              "Images/enemy2_2.png",
                                              200 + x*50, 150)
                               for x in range(11)]
                self.alien_g.add(self.alien1, self.alien2)
                self.playing = False
            self.update_method()

    def background_sound(self):
        # pygame.mixer.music.load('sounds/fastinvader1.wav')
        # pygame.mixer.music.play(loops = 1000000)
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
            self.ship1.x += -self.vel
        elif key[pygame.K_RIGHT]:
            self.ship1.x += self.vel
        if key[pygame.K_SPACE]:
            self.ship1.shoot()

    def blit_text(self, font_name, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        screen_text = font.render(text, True, self.TEXT_COLOR)
        text_rect = screen_text.get_rect()  # later use
        text_rect.center = (x, y)
        self.display.blit(screen_text, text_rect)

    def update_method(self):
        self.display.fill(self.COLOR)
        pygame.display.flip()
        self.window.blit(self.display, (0, 0))  # NOTA : Garantir posição (0,0)
        self.ship_group.draw(self.window)
        self.alien_g.draw(self.window)
        self.ship_group.update()
        pygame.display.update()
        for alien in self.alien_g:
            if alien.flag_bool():
                self.alien_g.update(True)
                break
        else:
            self.alien_g.update(False)
        self.BACK_KEY = False
        for alien in self.alien_g:
            pygame.sprite.spritecollide(alien, self.ship_group, True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    