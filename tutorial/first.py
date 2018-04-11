import sys, pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pygame游戏之旅")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()