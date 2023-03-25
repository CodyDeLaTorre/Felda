import pygame
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        #get display surface
        self.display_surface = pygame.display.get_surface()
        
        #sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()

    def create_map(self):
        for row, row_index in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == 'X':
                    Tile((x,y)[self.visible_sprites])

    def run(self):
        self.visible_sprites.draw(self.display_surface)
