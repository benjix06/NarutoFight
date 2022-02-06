import pygame

from player import Player
from setting import tile_size
from tiles import Tile


class Level:
    def __init__(self, level_data, surface):

        # levele setup
        self.display_surface = surface
        self.setup_level(level_data)

        self.world_shift = 0

    def setup_level(self, layout):
        """Set up the level, layout is the level_data"""
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        # Loop through the level_data
        for index_row, row in enumerate(layout):
            for index_column, column in enumerate(row):
                x = index_row * tile_size
                y = index_column * tile_size

                if column == "X":
                    tile = Tile((y, x), tile_size)
                    self.tiles.add(tile)
                elif column == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def run(self):

        # level title
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.player.draw(self.display_surface)
