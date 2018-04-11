import sys, pygame
from math import pi

pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Pygame游戏之旅")
GOLD = 255, 255, 0
RED = pygame.Color('red')
WHITE = 255, 255, 255
GREEN = pygame.Color('green')
plist = [(295, 170), (285, 250), (260, 280), (340, 280), (315, 250)]

r1rect = pygame.draw.rect(screen, GOLD, (300, 120, 200, 120), 0)
r2rect = pygame.draw.rect(screen, RED, (130, 150, 200, 120), 5)
e1rect = pygame.draw.ellipse(screen, GREEN, (30, 30, 100, 80), 3)
c1rect = pygame.draw.circle(screen, GOLD, (320, 300), 30, 5)
c2rect = pygame.draw.circle(screen, GOLD, (400, 380), 30)
l1rect = pygame.draw.lines(screen, WHITE, True, plist, 2)
a1rect = pygame.draw.arc(screen, RED, (200, 220, 200, 100), 1.4*pi, 1.9*pi, 3)
test = pygame.draw.rect

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()