import pygame
import time
import random

pygame.init()
#crash_sound = pygame.mixer.Sound("Car Crash Sound.mp3")



display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)

red = (200, 0, 0)
green = (0, 200, 0)

bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

car_width = 73

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('pacman')
clock = pygame.time.Clock()

pacimg = pygame.image.load('pac.png')
gameIcon = pygame.image.load('pac.png')

pygame.display.set_icon(gameIcon)

pause = False

def pac(x, y, dir):
    gameDisplay.blit(pygame.transform.scale(pacimg,(70,70)), (x, y))

def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def main():
    x_change = 0
    y_change = 0

    x = 0
    y = 0
    dir = "right"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP  or event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = 0
        x += x_change
        y += y_change
        gameDisplay.fill(white)
        pac(x,y,dir)
        pygame.display.update()


main()