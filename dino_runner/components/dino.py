import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import DUCKING, JUMPING, RUNNING
class Dino(Sprite):
    X_POS = 0
    Y_POS = 380
    Y_POS_2 = 414
    JUMP_VEL = 8
    dino_pos_Y = 0

    def __init__(self):
        self.image = RUNNING[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.step_count = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL
        self.dino_Y = self.Y_POS

    def update(self, user_input):
        self.run()
        if self.dino_run:
            self.run()
        elif self.dino_duck:
            self.duck()
        elif self.dino_jump:
            self.jump()

        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = False
            self.dino_jump = True

        elif user_input[pygame.K_DOWN] and not self.dino_duck and not self.dino_jump:
            self.dino_run = False
            self.dino_duck = True
            self.dino_jump = False

        elif not self.dino_jump and not self.dino_duck:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image,(self.dino_rect.x, self.dino_pos_Y))

    def run(self):
        self.dino_Y = 380
        self.dino_pos_Y = self.dino_Y
        
        if self.step_index <= 5:
            self.image = RUNNING[0]
        else:
            self.image = RUNNING[1]
            
        self.step_index += 1

    def duck(self):
        self.dino_Y = 414
        self.dino_pos_Y = self.dino_Y
        
        if self.step_index <= 5:
            self.image = DUCKING[0]
        else:
            self.image = DUCKING[1]
        
        if self.step_count > 1:
            self.dino_duck = False
            self.step_count = 0
            
        self.step_count += 1    
        self.step_index += 1

    def jump(self):
        self.dino_pos_Y = self.dino_rect.y
        self.image = JUMPING
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4 # Salto
            self.jump_vel -= 0.8 # Subiendo y cuando es negativo baja
        if self.jump_vel < -self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL