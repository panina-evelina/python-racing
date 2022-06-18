import pygame

class Car:


    def __init__(self, img):
        self.crashed = False
        self.car_img = pygame.image.load('img/' + img).convert_alpha()
        self.car_width = 80
        self.car_height = 150
        self.car_img = pygame.transform.scale(self.car_img, (self.car_width, self.car_height))
        self.car_img.set_colorkey((0, 0, 0))

    def draw_car(self, display, x, y):
        display.blit(self.car_img, (x,y))

    def clear_car(self):
        transparent = (0, 0, 0, 0)
        self.car_img.fill(transparent)
