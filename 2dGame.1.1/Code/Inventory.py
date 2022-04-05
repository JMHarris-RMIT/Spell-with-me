
import pygame
from level import *
from item import item





pygame.init()




font = pygame.font.Font(pygame.font.match_font("calibri"),26)
item_background = pygame.image.load('../graphics/objects/items/inven_background.png')
item_slot = pygame.image.load('../graphics/objects/items/item_slot.png')

class Inventory:
    def __init__(self):

        self.items_list = []

        self.rows = 5
        self.col = 5
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        self.box_size = 300
        self.x = 200
        self.y = 50
        self.slot_x = 64
        self.slot_y = 64
        self.border = 3


    def draw_inven(self):

        screen = pygame.display.get_surface()
        screen.blit(item_background,(200,100))

        self.slot_x = 750
        self.slot_y = 100

        for rows in range(self.rows):
            self.slot_x =750
            self.slot_y +=68
            for col in range(self.col):

                screen.blit(item_slot,(self.slot_x,self.slot_y))
                self.slot_x +=68



    def add_item(self, item_code):

        print("hello")






    def print_inven(self):

        i=0
        for item in self.items_list:
            print(self.items_list[i].show_item_info())
        i+=1







