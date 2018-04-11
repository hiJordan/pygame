import pygame
import sys

#   初始化参数游戏设置以及载入相关资源
pygame.init()
size = width, height = 1000, 600
BLACK = (0, 0, 0)
enemy_plane_num = 3
score = 0
attacked = 0
pygame.display.set_caption('Aircraft War')
screen = pygame.display.set_mode(size)
# 载入我方飞机并确定初始位置
friendly_plane = pygame.image.load(r"C:\Users\Administrator.SKY-20170216AOX"
                                   r"\Desktop\aircraft_war_material\friendly\Ares.png")
friendly_plane_rect = friendly_plane.get_rect()
plane_position = (width / 2 - friendly_plane_rect.right, height - friendly_plane_rect.bottom)
# 载入我方飞机子弹
friendly_plane_bullet = pygame.image.load(r"C:\Users\Administrator.SKY-20170216AOX"
                                          r"\Desktop\aircraft_war_material\bullet\bullet_2_orange.png")
friendly_plane_bullet_rect = friendly_plane_bullet.get_rect()
bullet_position = (2000, 2000)

#   游戏主体控制
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                plane_position_x = plane_position[0] - 10 if plane_position[0] - 10 > 0 else 0
                plane_position = (plane_position_x, plane_position[1])
            elif event.key == pygame.K_RIGHT:
                plane_position_x = plane_position[0] + 10 if plane_position[0] + 10 < width - \
                                   friendly_plane_rect.right else width-friendly_plane_rect.right
                plane_position = (plane_position_x, plane_position[1])
            elif event.key == pygame.K_UP:
                plane_position_y = plane_position[1] - 10 if plane_position[1] - 10 > 0 else 0
                plane_position = (plane_position[0], plane_position_y)
            elif event.key == pygame.K_DOWN:
                plane_position_y = plane_position[1] + 10 if plane_position[1] + 10 < height - \
                                   friendly_plane_rect.bottom else height-friendly_plane_rect.bottom
                plane_position = (plane_position[0], plane_position_y)
            elif event.key == pygame.K_SPACE:
                bullet_position_x = plane_position[0]+33
                bullet_position_y = plane_position[1]-15
                bullet_position = bullet_position_x, bullet_position_y
                # friendly_plane_bullet_rect = (0, 0, bullet_position_x, bullet_position_y)
            elif event.key == pygame.K_ESCAPE:
                sys.exit()
    friendly_plane_bullet_rect = friendly_plane_bullet_rect.move(1, 1)
    screen.fill(BLACK)
    screen.blit(friendly_plane_bullet, friendly_plane_bullet_rect)
    screen.blit(friendly_plane, plane_position)
    pygame.display.update()
