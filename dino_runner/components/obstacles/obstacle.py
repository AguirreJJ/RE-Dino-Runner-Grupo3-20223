import random
from pygame.sprite import Sprite

from dino_runner.utils.constants import SCREEN_WIDTH
class Obstacle(Sprite):
    def __init__(self, image, type, ran):
        self.image = image
        self.type = type
        self.ran = ran
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.steep_index = 0

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()
        if self.steep_index >= 6:
            self.steep_index = 0
        if not self.ran:
            if self.steep_index >= 3:
                self.type = 0
            else:
                self.type = 1
            
            self.steep_index += 1

    def draw(self, screen):
        screen.blit(self.image[self.type], self.rect)