import pygame
from setting import *
import sys


class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups, collision_sprite):
        super().__init__(groups)

        # Position for the player
        self.image = pygame.Surface((tile_size // 2, tile_size))

        # Player color
        self.image.fill(player_color)

        # rect = player
        self.rect = self.image.get_rect(topleft=position)

        # Player movement
        self.direction = pygame.math.Vector2()
        self.speed = 5
        self.gravity = 0.981
        self.collision_sprite = collision_sprite
        self.on_floor = False

        # How high the player can jump
        self.jump_speed = 15

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

        # Set negative value to make the play jump upward
        # ! Pygame topleft is 0,0
        if keys[pygame.K_SPACE]:
            self.direction.y = -self.jump_speed
            print("jump")

        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()

    # Apply the gravity
    def gravity_method(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def horizontal_collision(self):
        # check if the player collide with the tile
        for sprite in self.collision_sprite.sprites():
            if sprite.rect.colliderect(self.rect):
                # player hit the left
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right

                # player hit the right
                elif self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collision(self):

        # check if the player collide with the tile
        for sprite in self.collision_sprite.sprites():
            if sprite.rect.colliderect(self.rect):

                # Player hit the bottom
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True

                # Player hit the top
                elif self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        # Case: the user is not on the ground
        # if self.on_floor and self.direction.y != 0:
        #     self.on_floor = False

    def update(self):
        self.get_input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collision()
        self.gravity_method()
        self.vertical_collision()
