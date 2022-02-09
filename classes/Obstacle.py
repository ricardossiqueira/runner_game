import pygame
from random import randint


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, type='fly'):
        super().__init__()

        if type == 'snail':
            # Snail
            snail_frame_1 = pygame.image.load(
                "graphics/snail/snail1.png").convert_alpha()
            snail_frame_2 = pygame.image.load(
                "graphics/snail/snail2.png").convert_alpha()
            self.frames = [snail_frame_1, snail_frame_2]
            y_pos = 300
        else:
            # Fly
            fly_frame_1 = pygame.image.load(
                "graphics/Fly/Fly1.png").convert_alpha()
            fly_frame_2 = pygame.image.load(
                "graphics/Fly/Fly2.png").convert_alpha()
            self.frames = [fly_frame_1, fly_frame_2]
            y_pos = 210

        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(midbottom=(randint(900, 1100), y_pos))

    def animation_state(self, type):
        if type == 'snail': self.animation_index += 0.1
        else: self.animation_index += 0.2

        if self.animation_index >= len(self.frames):
            self.animation_index = 0

        self.image = self.frames[int(self.animation_index)]

    def destroy(self):
        if self.rect.x <= -100:
            self.kill()

    def update(self):
        self.animation_state(type)
        self.rect.x -= 6
        self.destroy()