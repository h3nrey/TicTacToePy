import pygame;
from sys import exit
pygame.init();

screen = pygame.display.set_mode((600, 450));
clock = pygame.time.Clock();
FPS = 60;

while True:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            pygame.quit();
            exit();

    pygame.display.update();
    clock.tick(FPS);