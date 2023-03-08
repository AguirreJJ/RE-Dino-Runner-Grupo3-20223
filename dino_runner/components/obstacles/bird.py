import random
from dino_runner.components.obstacles.obstacle import Obstacle
from dino_runner.utils.constants import BIRD


class Bird(Obstacle):
    def __init__(self, image):
        self.image = BIRD[0]
        self.dino_rect = self.image.get_rect()
        self.steep_index = 0
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(210, 330)
    
    def draw(self, screen): 
        if self.steep_index >= 6:
            self.steep_index = 0
        if self.steep_index <= 3:
            self.image = BIRD[0]
        else:
            self.image = BIRD[1]
    
        screen.blit(self.image,(self.rect.x, self.rect.y))
        self.steep_index += 1