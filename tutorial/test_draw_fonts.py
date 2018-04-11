import sys
import pygame.freetype


pygame.init()
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Pygame文字绘制")
GOLD = 255, 251, 0
WHITE = pygame.Color('white')

f1 = pygame.freetype.Font(r'C:\Windows\Fonts\simsun.ttc', 36)
f1rect = f1.render_to(screen, (250, 220), '世界和平', fgcolor=GOLD, bgcolor=WHITE, rotation=100, size=50)
#   render方法从参数上较之rende_to方法只缺少surf与dest参数
f2surf, f2rect = f1.render('世界和平', fgcolor=GOLD, size=50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.blit(f2surf, (350, 320))
    pygame.display.update()