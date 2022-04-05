import pygame

class item:
    def __init__(self, x,y):

        self.id = x,y
        self.item_count =0

        if self.id == 0:

            self.image = pygame.image.load('../graphics/objects/items/hp_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center = (0,0))

        elif self.id == 1:
            self.image = pygame.image.load('../graphics/objects/items/green_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.info = {"green potion": 1, "descrip": "restores some energy", "img": self.image}

        elif self.id == 2:
            self.image = pygame.image.load('../graphics/objects/items/axe1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        elif self.id == 3:
            self.image = pygame.image.load('../graphics/objects/items/blue_potion.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        elif self.id == 4:
            self.image = pygame.image.load('../graphics/objects/items/book1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        elif self.id == 5:
            self.image = pygame.image.load('../graphics/objects/items/book2.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        elif self.id == 6:
            self.image = pygame.image.load('../graphics/objects/items/book3.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        elif self.id == 7:
            self.image = pygame.image.load('../graphics/objects/items/sword1.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))

        else:
            self.id = 8
            self.image = pygame.image.load('../graphics/objects/items/heart.png').convert_alpha()
            self.rect = self.image.get_rect(center=(0, 0))
            self.info = {"axe": 20, "descrip": "its very sharp", "img": self.image}


    def show_item_info(self):
        return self.info




