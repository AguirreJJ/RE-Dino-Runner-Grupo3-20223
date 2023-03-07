from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.ran = False
        self.steep_index = 0
        if self.steep_index >= 10:
            self.steep_index = 0
        self.update_1()
        super().__init__(image, self.type, self.ran)
        self.rect.y = 270
        #self.type = 0
        

    
    def update_1(self):
        if self.steep_index >= 5:
            self.type = 0
        else:
            self.type = 1
        
        self.steep_index += 1