import random
from dino_runner.components.obstacles.obstacle import Obstacle


class Cactus(Obstacle):
    def __init__(self, image):
        self.ran = True
        self.type = random.randint(0, 5)
        super().__init__(image, self.type, self.ran)
        #self.rect.y = 325
        #print(self.image[self.type].get_height())
        if self.image[self.type].get_height() == 71:
            self.rect.y = 330
        elif self.image[self.type].get_height() == 95:
            self.rect.y = 306