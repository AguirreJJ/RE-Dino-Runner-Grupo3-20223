import random
import pygame
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD


class ObstacleManager:
    DEATH_COUNT = 0
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:

            if random.randint(0,2)==1:
                self.obstacles.append(Cactus("SMALL"))
            elif random.randint(0,2)==0:
                self.obstacles.append(Cactus("LARGE"))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                self.DEATH_COUNT += 1
                pygame.time.delay(1000)
                game.playing = False
                break

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []