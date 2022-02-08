import pygame

from player import Player
from setting import *
from tiles import Tile


class Level:
    def __init__(self):

        # levele setup
        self.display_surface = pygame.display.get_surface()

        # Sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        # Set the level map
        self.setup_level()

    def setup_level(self):
        # Loop through the level_data
        for index_row, row in enumerate(level_map):
            for index_column, column in enumerate(row):
                x = index_column * tile_size
                y = index_row * tile_size

                if column == "X":
                    Tile((x, y), [self.visible_sprites,
                         self.collision_sprites])
                elif column == "P":
                    self.player = Player(
                        (x, y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

    def run(self):

        # Run the game in this level
        self.active_sprites.update()
        self.visible_sprites.custom_draw(self.player)


class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100, 300)

        # center camera setup
        # self.half_w = self.display_surface.get_size()[0] // 2
        # self.half_h = self.display_surface.get_size()[1] // 2

        # camera
        cam_left = camera_padding['left']
        cam_top = camera_padding['top']
        cam_width = self.display_surface.get_size(
        )[0] - (cam_left + camera_padding['right'])
        cam_height = self.display_surface.get_size(
        )[1] - (cam_top + camera_padding['bottom'])

        self.camera_rect = pygame.Rect(
            cam_left, cam_top, cam_width, cam_height)

    def custom_draw(self, player):

        # get the player offset
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h

        # getting the camera position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left
        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right
        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top
        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom

        # camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - camera_padding['left'],
            self.camera_rect.top - camera_padding['top'])

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
