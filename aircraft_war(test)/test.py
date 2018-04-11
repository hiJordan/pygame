import sys, pygame

pygame.init()
size = width, height = 1000, 600
BLACK = 0, 0, 0
fps = 250
screen = pygame.display.set_mode(size)
pygame.display.set_caption('飞机大战')
bullet = pygame.image.load(r'C:\Users\Administrator.SKY-20170216AOX\Desktop'
                           r'\aircraft_war_material\bullet\bullet_2_orange.png')
bullet_rect = bullet.get_rect()
f_clock = pygame.time.Clock()
print(bullet_rect)
while True:
    count = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # bullet_rect = bullet_rect.move(1, 1)
    position = width/2, height - bullet_rect.bottom + count

    screen.fill(BLACK)
    screen.blit(bullet, position)
    print(bullet_rect)
    pygame.display.update()
    f_clock.tick(fps)
    count += 1
