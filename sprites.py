#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 21:01:20 2020

@author: ricardo
"""
import pygame

pygame.init()


class StarShip(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("Images/ship.png")
        self.shoot_sound = pygame.mixer.Sound("sounds/shoot.wav")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        # self.shot = Shot(self.x, self.y)
        self.bullet_g = pygame.sprite.Group()
        self.score = 0
        self.life = 2  # giving 3 lifes

    def shoot(self):
        if len(self.bullet_g) == 0:
            self.shot = Shot(self.x, self.y, True)
            self.bullet_g.add(self.shot)
            self.shoot_sound.play()
            self.shot.update()  # estará a mais ??

    def update(self):
        self.rect.center = self.x, self.y


class Aliens(pygame.sprite.Sprite):
    def __init__(self, image1, image2, x, y):
        super().__init__()
        self.counter = 0
        self.image = pygame.image.load(image1)
        self.vel = 3
        self.x, self.y = x, y
        self.rect = self.image.get_rect()
        self.image1 = image1
        self.image2 = image2
        self.walk_sound_1 = pygame.mixer.Sound('sounds/fastinvader1.wav')

    def update(self, flag):
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
        if self.counter == 8 or self.counter == 4:
            self.walk_sound_1.play()
        self.counter = self.counter % 8
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def turn(self):
        if self.flag:
            self.vel = - self.vel
            self.y += 10

    def flag_bool(self):
        if self.x - self.image.get_rect().size[0] / 2 <= 0:
            return True
        if self.x + self.image.get_rect().size[0] / 2 >= 1000:
            return True

    def killed(self):
        self.image = pygame.image.load("Images/explosionpurple.png")
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4)

    def shoot(self):
        self.shot = Shot(self.x, self.y, False)
        self.shot.update()  # estará a mais ??
        
class Shot(pygame.sprite.Sprite):
    def __init__(self, x, y, a_bool):
        super().__init__()
        self.image = pygame.image.load("Images/laser.png")
        self.rect = self.image.get_rect()
        self.x, self.y = x, y
        self.a_bool = a_bool
        
    def update(self):
        if 0 < self.y < 1000:
            self.rect.center = self.x, self.y
            self.y -= 10 if self.a_bool else -10
        else:
            self.kill()


        
# alien_g = pygame.sprite.Group()

# alien1 = [Aliens("Images/enemy1_1.png", "Images/enemy1_2.png", 200 + x*50, 100) for x in range(11)]
# alien2 = [Aliens("Images/enemy1_1.png", "Images/enemy1_2.png", 200 + x*50, 150) for x in range(11)]

# alien_g.add(alien1,alien2)

# random_bullet = pygame.sprite.Group()
        

# ship = StarShip(400, 900)
# ship_g = pygame.sprite.Group()
# ship_g.add(ship)
# screen = pygame.display.set_mode((1000,1000))
# run = True
# clock = pygame.time.Clock()
# su = pygame.Surface((1000,1000))
# su.fill((40,0,0))
# ship2 = StarShip(300, 900)
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
#     ship.bullet_g.draw(screen)
#     alien_g.draw(screen)
    
#     if len(random_bullet) < 2:
#         aln = alien_g.sprites()
#         if len(aln) > 0:
#             chosen_one = aln[random.randrange(0, len(aln))]
#             random_bullet.add(Shot(chosen_one.x, chosen_one.y, False))
#     random_bullet.draw(screen)
#     random_bullet.update()
#     ship.bullet_g.update()
#     ship_g.update()
        

#     for alien in alien_g:
#         if alien.flag_bool():
#             alien_g.update(True)
#             break
#     else:
#         alien_g.update(False)

#     for alien in alien_g:
#         pygame.sprite.spritecollide(alien , ship_g, True)
#         if pygame.sprite.spritecollide(alien, ship.bullet_g, True):
#             alien_g.remove(alien)
    
    
       
    
# pygame.quit()



# random_bullet = pygame.sprite.Group()
# if len(random_bullet) < 2:
#             aln = self.alien_g.sprites()
#             if len(aln) > 0:
#                 chosen_one = aln[random.randrange(0, len(aln))]
#                 random_bullet.add(sprites.Shot(chosen_one.x, chosen_one.y,
#                                                 False))
#         random_bullet.draw(self.window)
# random_bullet.update()
        