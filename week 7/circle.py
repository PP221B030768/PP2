import pygame 

pygame.init()

size = weight, height = (500, 500)
RED = (255, 0, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(size)

screen.fill(WHITE)

pygame.display.set_caption('Cirle')

clock = pygame.time.Clock()

x = 25
y = 25

pygame.draw.circle(screen, RED, (x, y), 25)

done = False

def Draw_Circle(q):
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), 25)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            y += 20
            if y >= 484:
                y = 25
                Draw_Circle(y)
            else:
                Draw_Circle(y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            y -= 20
            if y <= 15:
                y = 475
                Draw_Circle(y)
            else:
                Draw_Circle(y)
            # Draw_Circle(y)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            x += 20
            if x >= 484:
                x = 25
                Draw_Circle(x)
            else:
                Draw_Circle(x)
            # Draw_Circle(x)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            x -= 20
            if x <= 15:
                x = 475
                Draw_Circle(x)
            else:
                Draw_Circle(x)
            # Draw_Circle(x)
    clock.tick(60)
    pygame.display.update()

pygame.quit()