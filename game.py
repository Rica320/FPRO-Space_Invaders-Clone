#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 13:21:03 2020

@author: ricardo
"""

import ctypes
import pygame
import menu
import sprites
import random
import bot
import keyboard


class Game():
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.running, self.playing = True, False  # DEBUGGING
        self.WIN_W, self.WIN_H = 1000, 1000
        self.display = pygame.Surface((self.WIN_W, self.WIN_H))
        ctypes.windll.user32.SetProcessDPIAware() # for windows users 
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
                                      200 + x*50, 100, 30)
                       for x in range(11)]
        self.alien2 = [sprites.Aliens("Images/enemy2_1.png",
                                      "Images/enemy2_2.png",
                                      200 + x*50, 150, 20)
                       for x in range(11)]
        self.alien3 = [sprites.Aliens("Images/enemy2_1.png",
                                      "Images/enemy2_2.png",
                                      200 + x*50, 200, 20)
                       for x in range(11)]
        self.alien4 = [sprites.Aliens("Images/enemy3_1.png",
                                      "Images/enemy3_2.png",
                                      200 + x*50, 250, 10)
                       for x in range(11)]
        self.alien5 = [sprites.Aliens("Images/enemy3_1.png",
                                      "Images/enemy3_2.png",
                                      200 + x*50, 300, 10)
                       for x in range(11)]
        self.alien_g = pygame.sprite.Group()
        self.alien_g.add(self.alien1, self.alien2, self.alien3, self.alien4,
                         self.alien5)
        self.random_bullet = pygame.sprite.Group()
        self.bot = bot.Bot(self)
        self.bot_state = False

    def game_loop(self):
        self.background_sound()
        while self.playing:
            self.clock.tick(27)  # 
            if self.bot_state:
                self.bot.move()
            self.events()
            if self.bot_state:
                keyboard.release('left')
                keyboard.release('right')
                keyboard.release('space')
            if self.BACK_KEY:
                with open('points.txt', 'a') as f:
                    f.writelines(f"{self.ship1.score}\n")
                self.bot_state = False
                self.BACK_KEY = False
                self.recreater()
                self.playing = False
            if len(self.alien_g) == 0:
                acum_score = self.ship1.score
                priv_life = self.ship1.life
                self.recreater()
                self.ship1.score = acum_score
                self.ship1.life = priv_life
            self.update_method()

    def background_sound(self):
        # pygame.mixer.music.load('teste2.wav')
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
                if event.key == pygame.K_i and not self.playing:
                    self.playing = True
                    self.menu_state.running_display = False
                    pygame.mixer.music.fadeout(1000)
                if event.key == pygame.K_b and not self.playing:
                    self.playing = True
                    self.menu_state.running_display = False
                    self.bot_state = True
                    pygame.mixer.music.fadeout(1000)
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT] and self.playing:
            if self.ship1.x > self.ship1.image.get_rect().size[0]/2:
                self.ship1.x += -self.vel
        elif key[pygame.K_RIGHT] and self.playing:
            if self.ship1.x + self.ship1.image.get_rect().size[0]/2 < self.WIN_W:
                self.ship1.x += self.vel
        if key[pygame.K_SPACE] and self.playing:
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
        self.blit_text('space_invaders.ttf', f"{self.ship1.score}",
                       30, self.WIN_W - 30*len(f"{self.ship1.score}"), 30)
        self.blit_text("Invaders-From-Space.ttf",
                       'W' * (self.ship1.life + 1), 45, 55, 950)
        self.window.blit(self.display, (0, 0))  # NOTE : Garantir posição (0,0)
        if len(self.random_bullet) < 4:
            aln = self.alien_g.sprites()
            if len(aln) > 0:
                chosen_one = aln[random.randrange(0, len(aln))]
                self.random_bullet.add(sprites.Shot(chosen_one.x,
                                                    chosen_one.y, False))

        self.random_bullet.update()
        self.random_bullet.draw(self.window)
        self.ship1.bullet_g.update()
        self.ship1.bullet_g.draw(self.window)
        self.ship_group.update()
        self.ship_group.draw(self.window)
        self.alien_g.draw(self.window)  # TODO Find a way to stop the Bug
        pygame.display.update()  # BUG Solved... first update then draw
        for alien in self.alien_g:
            if alien.flag_bool():
                self.alien_g.update(True)
                break
        else:
            self.alien_g.update(False)
        for alien in self.alien_g:
            if pygame.sprite.spritecollide(alien, self.ship_group, True):
                self.lose_window()
            if pygame.sprite.spritecollide(alien, self.ship1.bullet_g, True):
                alien.killed()
                self.update_method()
                self.ship1.score += alien.points  # TODO change points
                self.alien_g.remove(alien)
        if pygame.sprite.spritecollide(self.ship1, self.random_bullet, True):
            if self.ship1.life == 0:
                self.ship1.kill()
                self.lose_window()
            else:
                self.ship1.life -= 1

    def recreater(self):
        self.ship_group.add(self.ship1)
        self.ship1.life = 2
        self.ship1.x, self.ship1.y = self.ship1_x, self.ship1_y
        self.alien_g.empty()
        self.alien1 = [sprites.Aliens("Images/enemy1_1.png",
                                      "Images/enemy1_2.png",
                                      200 + x*50, 100, 30)
                       for x in range(11)]
        self.alien2 = [sprites.Aliens("Images/enemy2_1.png",
                                      "Images/enemy2_2.png",
                                      200 + x*50, 150, 20)
                       for x in range(11)]
        self.alien3 = [sprites.Aliens("Images/enemy2_1.png",
                                      "Images/enemy2_2.png",
                                      200 + x*50, 200, 20)
                       for x in range(11)]
        self.alien4 = [sprites.Aliens("Images/enemy3_1.png",
                                      "Images/enemy3_2.png",
                                      200 + x*50, 250, 10)
                       for x in range(11)]
        self.alien5 = [sprites.Aliens("Images/enemy3_1.png",
                                      "Images/enemy3_2.png",
                                      200 + x*50, 300, 10)
                       for x in range(11)]
        self.alien_g.add(self.alien1, self.alien2, self.alien3, self.alien4,
                         self.alien5)
        self.ship1.score = 0
        self.ship1.bullet_g = pygame.sprite.Group()  # Not needed
        self.random_bullet.empty()

    def lose_window(self):
        with open('points.txt', 'a') as f:
            f.writelines(f"{self.ship1.score}\n")
        while self.playing:
            self.display.fill(self.COLOR)
            pygame.display.flip()
            self.blit_text('space_invaders.ttf', "You lose!!!",
                           50, 500, 400)
            self.blit_text('space_invaders.ttf',
                           f"Your score: {self.ship1.score}", 30, 500, 500)
            self.blit_text('space_invaders.ttf', "Press backspace to return",
                           30, 500, 600)
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.events()
            if self.BACK_KEY:
                self.bot_state = False
                self.BACK_KEY = False
                self.recreater()
                self.playing = False
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
                    