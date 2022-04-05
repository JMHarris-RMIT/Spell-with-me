import threading
import time

import pygame

from config import *
from threading import Thread
from Inventory import *
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, groups, obstacle_sprites):
        super().__init__(groups)


        self.image = pygame.image.load('../graphics/player/player_down.png').convert_alpha()

        # do not change
        self.rect = self.image.get_rect(center=(x, y))

        # hitbox can put player infromt/behind sprites, deals with collisions
        self.hitbox = self.rect.inflate(0, -25)

        self.direction = pygame.math.Vector2()
        self.speed = 4
        self.obstacle_sprites = obstacle_sprites

        # will be used to stop player moving if a battle starts
        self.frozen = False

        # marks what sprite in animation is being used and how quick they will change
        self.frame_index = 0
        self.animation_speed = 0.10

        # used to change what animation / sprite is used for what direction the player is facing
        self.facing = 'down'

        # will be used when starting battle
        self.inBattle = False

        # open / close Inven tracking
        self.Inven_open = False



    # this dosent need to be in here, but saves room in input, might move later if this class gets to0 big
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:

            self.direction.y = -1
            self.facing = 'up'
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
                self.hitbox.y += self.direction.y * self.speed
                self.collision('vertical')
                self.rect.center = self.hitbox.center

        elif keys[pygame.K_DOWN]:

            self.direction.y = 1
            self.facing = 'down'
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
                self.hitbox.y += self.direction.y * self.speed
                self.collision('vertical')
                self.rect.center = self.hitbox.center
        else:
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing = 'right'
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
                self.hitbox.x += self.direction.x * self.speed
                self.collision('horizontal')
                self.rect.center = self.hitbox.center

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing = 'left'
            if self.direction.magnitude() != 0:
                self.direction = self.direction.normalize()
                self.hitbox.x += self.direction.x * self.speed
                self.collision('horizontal')
                self.rect.center = self.hitbox.center
        else:
            self.direction.x = 0

        # used to open inventory



    def get_player_pos(self):
        self.pos = self.rect.centerx, self.rect.centery
        return self.pos

    # used for colliding with sprites / walls, trees, ect
    def collision(self, direction):

        # outer if statement for moving horizontally
        if direction == 'horizontal':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # used if moving right to mark collision
                    if self.direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left

                    # used if moving left to mark collision
                    if self.direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right

        # outer if statement for vertical movements
        if direction == 'vertical':
            for sprite in self.obstacle_sprites:
                if sprite.hitbox.colliderect(self.hitbox):
                    # used if moving down to mark collision
                    if self.direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top

                    # used if moving up to mark collision
                    if self.direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom

    # updating user input
    def update(self):
        self.input()
