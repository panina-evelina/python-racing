import pygame
import random

class CarRacing:
    def __init__(self):
        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None
        self.initialize()

    def initialize(self):
        self.crashed = False
        self.car = pygame.image.load('../img/car.png')
        self.car_x = (self.display_width * 0.45)
        self.car_y = (self.display_height * 0.8)
        self.car_width = 49

        self.enemy_car = pygame.image.load('../img/enemy_car.png')
        self.enemy_car_x = random.randrange(310, 450)
        self.enemy_car_y = -600
        self.enemy_car_width = 49
        self.enemy_car_height = 100
        self.enemy_car_speed = 5

        # background
        self.bg_img = pygame.image.load('../img/road.png')
        self.bgx1 = (self.display_width / 2) - (360/2)
        self.bgx2 = (self.display_width / 2) - (360/2)
        self.bgy1 = 0
        self.bgy2 = -600
        self.bgspeed = 3
        self.count = 0

    def car(self, car_x, car_y):
        self.gameDisplay.blit(self.car, (car_x, car_y))
    def racing_windows(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Car Race -- Randhir')

    def run_car(self):
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.crashed = True

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.car_x -= 50
                    if (event.key == pygame.K_RIGHT):
                        self.car_x += 50

            self.gameDisplay.fill(self.black)
            self.back_ground_road()
            self.run_enemy_car(self.enemy_car_x, self.enemy_car_y)
            self.enemy_car_starty += self.enemy_car_speed

            if self.enemy_car_starty > self.display_height:
                self.enemy_car_y = 0 - self.enemy_car_height
                self.enemy_car_x = random.randrange(310, 450)

            self.car(self.car_x, self.car_y)
            self.highscore(self.count)
            self.count +=1




