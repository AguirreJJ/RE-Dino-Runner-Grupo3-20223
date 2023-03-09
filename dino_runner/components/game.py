import random
import pygame
from dino_runner.components.dino import Dino
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components import tex_utils
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import BG, CLOUD, DINO_S, GAME_OVER, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS



class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.x_pos_cloud = SCREEN_WIDTH
        self.y_pos_cloud = random.randint(50, 250)
        self.x_pos_cloud_2 = SCREEN_WIDTH
        self.y_pos_cloud_2 = random.randint(50, 250)
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.max_points = 0
        self.running = True
        self.death_count = 0
        self.power_up_manager = PowerUpManager()

    def run(self):
        self.create_components()
        self.playing = True
        self.game_speed = 20
        self.points = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player, self) 

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

        image_width = CLOUD.get_width()
        self.screen.blit(CLOUD, (self.x_pos_cloud, self.y_pos_cloud))
        self.screen.blit(CLOUD, (self.x_pos_cloud_2, self.y_pos_cloud_2))
        if self.x_pos_cloud <= -SCREEN_WIDTH:
            self.y_pos_cloud = random.randint(50, 250)
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud, self.y_pos_cloud))
            self.x_pos_cloud = SCREEN_WIDTH
        if self.x_pos_cloud_2 <= -SCREEN_WIDTH + 500:
            self.y_pos_cloud_2 = random.randint(50, 250)
            self.screen.blit(CLOUD, (image_width + self.x_pos_cloud_2, self.y_pos_cloud_2))
            self.x_pos_cloud_2 = SCREEN_WIDTH
        self.x_pos_cloud -= self.game_speed
        self.x_pos_cloud_2 -= self.game_speed - 5

    def execute (self):
        while self.running:
            if not self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True

        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_on_menu()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2
        if self.death_count == 0:
            text, text_rect = tex_utils.get_centered_message('Press any Key to start')
            self.screen.blit(text, text_rect)
            self.screen.blit(DINO_S[0], (half_screen_width - 40 , half_screen_height - 150))
        else:
            image_width = GAME_OVER.get_rect()
            

            self.screen.blit(GAME_OVER,(half_screen_width - 200, half_screen_height - 220))
            text, text_rect = tex_utils.get_centered_message('Press any Key to Restart')
            score, score_rect = tex_utils.get_centered_message('Your Score: ' + str(self.points), height = half_screen_height + 50)
            death, death_rect = tex_utils.get_centered_message('Death count: ' + str(self.death_count), height = half_screen_height + 100)
            self.screen.blit(score, score_rect)
            self.screen.blit(text, text_rect)
            self.screen.blit(death, death_rect)
            self.screen.blit(DINO_S[1], (half_screen_width - 40, half_screen_height - 150))

            

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        if self.points > self.max_points:
            self.max_points = self.points
        text, text_rect = tex_utils.get_score_element(self.points)
        max_score, max_score_rect = tex_utils.get_score_element(self.max_points, height = 70)
        self.screen.blit(text, text_rect)
        self.screen.blit(max_score, max_score_rect)
        self.player.check_invincibility(self.screen)

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)