import sys, pygame
import pygame.freetype

pygame.init()
size = width, height = 700, 500
f1speed = [1, 1]
f2speed = [1, 1]
BLACK = 0, 0, 0
GOLD = 255, 251, 0
f1pos = [300, 200]
f2pos = [400, 300]
fps = 300

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygam文字壁球")
f1 = pygame.freetype.Font(r'C:\Windows\Fonts\simsun.ttc', 36)
f1rect = f1.render_to(screen, f1pos, '李安平', fgcolor=GOLD, size=50)
f2surf, f2rect = f1.render('妄想之国', fgcolor=GOLD, size=50)
fclock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if f1pos[0] < 0 or f1rect.width+f1pos[0] > width:
        f1speed[0] = -f1speed[0]
    if f2rect.left < 0 or f2rect.right > width:
        f2speed[0] = -f2speed[0]
    if f1pos[1] < 0 or f1rect.height+f1pos[1] > height:
        f1speed[1] = -f1speed[1]
    if f2rect.top < 0 or f2rect.bottom > height:
        f2speed[1] = -f2speed[1]
    f1pos[0] += f1speed[0]
    f2rect.left += f2speed[0]
    f1pos[1] += f1speed[1]
    f2rect.top += f2speed[1]

    screen.fill(BLACK)
    #screen.blit(f2surf, f1pos)
    screen.blit(f2surf, f2rect)
    f1rect = f1.render_to(screen, f1pos, '李安平', fgcolor=GOLD, size=50)
    pygame.display.update()
    fclock.tick(fps)