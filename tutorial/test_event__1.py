import sys, pygame

pygame.init()
size = width, height = 700, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame事件处理")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                print('keydown: ', '#', event.key, event.mod)
            else:
                print('keydown: ', event.unicode, event.key, event.mod)
        elif event.type == pygame.MOUSEMOTION:
            print('mousemotion: ', event.pos, event.rel, event.buttons)
        elif event.type == pygame.MOUSEBUTTONUP:
            print('mousebuttonup: ', event.pos, event.button)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('mousebuttondown: ', event.pos, event.button)

    pygame.display.update()