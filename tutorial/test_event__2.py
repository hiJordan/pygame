import sys, pygame

pygame.init()
size = width, height = 700, 600
fps = 1
num = 1
fclock = pygame.time.Clock()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('pygame事件处理')

while True:
    uevent = pygame.event.Event(pygame.KEYDOWN, {'unicode':123, 'key':pygame.K_SPACE, 'mod':pygame.KMOD_ALT})
    pygame.event.post(uevent)
    num += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.unicode == '':
                print('keydown: ', num, '#', event.key, event.mod)
            else:
                print('keydown: ', num, event.unicode, event.key, event.mod)

    pygame.display.update()
    fclock.tick(fps)
