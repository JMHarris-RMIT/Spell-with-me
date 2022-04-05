import pygame
import random


class Chest:

    def __init__(self, x,y):

        self.posX = x
        self.posY = y


    def get_chest_posX(self):
        return self.posX

    def get_chest_posY(self):
        return self.posY

    def get_chest_pos(self):
        self.pos = self.posX, self.posY
        return self.pos