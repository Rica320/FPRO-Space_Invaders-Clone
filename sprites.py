#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:01:20 2020

@author: ricardo
"""
import pygame

# pygame.init()


class StarShip(pygame.sprite.Sprite):
    ''' States the methods and attributes that a StarShip object has '''

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/ship.png")
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.bullet_g = pygame.sprite.Group()
        self.score = 0
        self.life = 2  # giving 3 lifes

    def shoot(self):
        '''
        Instantiates a Shot object adding it to a group
        and giving it a sound.
        '''
        if len(self.bullet_g) == 0:
            shot = Shot(self.x, self.y, True)
            self.bullet_g.add(shot)
            self.shoot_sound.play()
            shot.update()

    def update(self):
        ''' Update of the position of the StarShip '''
        self.rect.center = self.x, self.y


class Aliens(pygame.sprite.Sprite):
    ''' States the methods and attributes that a Alien object has '''
    sound_counter = 0

    def __init__(self, image1, image2, x, y, points):
        super().__init__()
        self.counter = 0
        self.image = pygame.image.load(image1)
        self.vel = 3
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.image1 = image1
        self.image2 = image2
        self.points = points
        self.kill_frames = 1

    def update(self, flag):
        '''
        Update of the alien x & y, images and, if chosen, music.
        A flag is given which will determine the movement of the alien(s).
        '''
        self.flag = flag
        if self.counter // 4 <= 0:
            self.image = pygame.image.load(self.image1)
            self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        else:
            self.image = pygame.image.load(self.image2)
            self.image = pygame.transform.rotozoom(self.image, 0, 0.2)
        self.turn()
        self.x += self.vel
        self.counter += 1
        # if self.counter == 8 or self.counter == 4:
        #     # walk_sound_1 = pygame.mixer.Sound(
        #     #     f"sounds/fastinvader{self.sound_counter % 4 + 1}.wav")
        #     # walk_sound_1.play()
        #     pygame.mixer.music.load(
        #         f"sounds/fastinvader{self.sound_counter % 4 + 1}.wav")
        #     pygame.mixer.music.play()
        #     self.sound_counter += 1
        self.counter = self.counter % 8
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def turn(self):
        ''' If a flag is raised then the ship.vel changes signal '''
        if self.flag:
            self.vel = - self.vel
            self.y += 10

    def flag_bool(self):
        '''
        Returns a Boolean that tells if the alien as hit the edge of the screen
        '''
        if self.x - self.image.get_rect().size[0] / 2 <= 0:
            return True
        if self.x + self.image.get_rect().size[0] / 2 >= 1000:
            return True

    def killed(self):
        '''
        Defines the procedure in case of a kill.
        It will be given to the screen an image of an explosion.
        A atribute kill_frames will kill the alien on the main loop
        '''
        self.image = pygame.image.load("Images/explosionpurple.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)
        self.kill_frames = 0
        kill_sound = pygame.mixer.Sound('sounds/invaderkilled.wav')
        kill_sound.play()

    def shoot(self):
        ''' Instantiates a Shot object '''
        shot = Shot(self.x, self.y, False)
        shot.update()


class MysteriousShip(pygame.sprite.Sprite):
    ''' States the methods and attributes that a MysteriousShip object has '''
    points = 100

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Images/mystery.png")
        self.rect = self.image.get_rect()
        self.x, self.y = -self.image.get_rect().size[0] / 2, 50
        self.vel = 10
        self.image = pygame.transform.rotozoom(self.image, 0, 0.3)

    def update(self, abool):
        '''
        Update of the MysteriousShip x and music.
        A Boolean is given that will tell if there is less
        than 23 aliens on the screen.
        '''
        self.x += self.vel
        if abool:
            sound = pygame.mixer.Sound('sounds/ufo_highpitch.wav')
        else:
            sound = pygame.mixer.Sound('sounds/ufo_lowpitch.wav')
        sound.play()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y


class Shot(pygame.sprite.Sprite):
    ''' States the methods and attributes that a Shot object has '''

    def __init__(self, x, y, a_bool):
        super().__init__()
        self.image = pygame.image.load("Images/laser.png")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.a_bool = a_bool

    def update(self):
        '''
        Update of the bullet y.
        As this class is used for Aliens and StarShips a Boolean is given that
        will determine the direction of the bullet
        '''
        if 0 < self.y < 1000:
            self.rect.center = self.x, self.y
            self.y -= 10 if self.a_bool else -10
        else:
            self.kill()
