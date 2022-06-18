import pygame
from models.Car import Car

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Racing')

white = (255, 255, 255)

clock = pygame.time.Clock()
car = Car('car.png')
enemy_car = Car('enemy_car.png')

x_car = (display_width * 0.45)
x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0

gameExit = False
gameDisplay.fill(white)
bg = pygame.image.load("img/road.png")
bg = pygame.transform.scale(bg, (display_width/1.5, display_height))
gameDisplay.blit(bg, (150, 0))

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
    x_car += x_change
    gameDisplay.fill(white)
    gameDisplay.blit(bg, (150, 0))
    car.draw_car(gameDisplay, x_car, y - 40)
    enemy_car.draw_car(gameDisplay, x + 50, y - 200)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
