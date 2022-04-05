import threading

import pygame
import math
from pygame.camera import *

from config import *
from tile import Tile
from player import Player
from Chest import Chest
from Inventory import Inventory
from math import *
from threading import Thread
from item import item
import time

inven_open = False



class Level:
    def __init__(self):

        self.chests = []

        # get the display surface this is where objects are drawn
        self.display_surface = pygame.display.get_surface()

        # sprite group setup, camera this method re-draws the map when moving around
        self.visible_sprites = Camera()
        # obstale and chest sprites, chests are both an obstacle and a chest. this is done to make chests interactive, same thing can be done with doors, ladders, ect
        self.obstacle_sprites = pygame.sprite.Group()
        self.chest_sprites = pygame.sprite.Group()
        self.item_sprites = pygame.sprite.Group()

        self.Inventory = Inventory()

        self.inven_open = False

        # creating the map
        self.create_map(MAP1)

    def create_map(self, map):
        # background here

        for row_index, row in enumerate(map):
            for col_index, col in enumerate(row):

                x = col_index * TILESIZE
                y = row_index * TILESIZE

                # dont worry about any of the highlited things below: they wont throw errors
                if col == 'x':
                    Tile((x, y), [self.visible_sprites, self.obstacle_sprites], 'boundry')

                if col == 'p':
                    self.player = Player(x, y, [self.visible_sprites], self.obstacle_sprites)

                if col == 'c':
                    Tile((x, y), [self.visible_sprites, self.chest_sprites, self.obstacle_sprites], 'chest')
                    self.chests.append(Chest(x, y))
                    print(x, y)

    def run(self):
        global inven_open
        # update and draw the game

        t1 = Thread(target=self.visible_sprites.draw_all(self.player))
        t2 = Thread(target=self.visible_sprites.update())
        t1.start()
        t2.start()

        self.keys = pygame.key.get_pressed()



        if self.keys[pygame.K_p]:
            print("aa")
            self.Inventory.print_inven()

        if self.keys[pygame.K_i]:
            inven_open = True

        if self.keys[pygame.K_c]:
            inven_open = False

        # aadd checks for any other things here, hidden items. Loot on ground? doors?
        if pygame.mouse.get_pressed()[0]:
            #this wait will make only 1 mouse click register, not several
            pygame.time.wait(100)
            mouse_pos = pygame.mouse.get_pos()[0] + self.visible_sprites.get_offset()[0], pygame.mouse.get_pos()[1] + \
                        self.visible_sprites.get_offset()[1]

            self.check_all(mouse_pos)

    # this can be used to call additional methods, such as if there's doors, or other things to click on apart from chests
    def check_all(self, mouse_pos):

        self.check_chests(mouse_pos)

    # this will check if the user has clicked on a chest and is close enough to open, change <= 64 to another number to increase range
    def check_chests(self, mouse_pos):

        i = 0
        for chest in self.chests:

            if dist(mouse_pos, self.chests[i].get_chest_pos()) <= 64:

                # checking if player is close enough to the item
                if math.floor(dist((sqrt((pow(self.player.get_player_pos()[0] - 0, 2))),
                                    sqrt((pow(self.player.get_player_pos()[1] - 0, 2)))),
                                   self.chests[i].get_chest_pos())) <= 64:
                    self.Inventory.add_item(1)

            i += 1


# this is for the adjusting of the screen how the camera follows it around
class Camera(pygame.sprite.Group):
    def __init__(self):
        # general setup
        super().__init__()
        self.Inventory = Inventory()
        global inven_open
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] / 2
        self.half_height = self.display_surface.get_size()[1] / 2
        self.offset = pygame.math.Vector2()

    def get_offset(self):
        return self.offset

    def draw_all(self, player):
        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        if inven_open:

            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)
            self.Inventory.draw_inven()

        else:

            for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
                offset_pos = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset_pos)

            # for sprite in self.sprites():
