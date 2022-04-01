import pygame
import math
import datetime

time = datetime.datetime.now()

pygame.init()

size = width, height = (1400, 1050)

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey Mouse Clock")

angle = -(int(time.strftime("%S")) * 6) - 6
angleM = -(int(time.strftime("%M")) * 6 + (int(time.strftime("%S")) * 6 / 60)) - 54

mickey = pygame.image.load('mickey.png')
seconds = pygame.image.load('seconds.png')
minutes = pygame.image.load('minutes.png')
# pygame.display.update()

def rotate(image, rect, angle):
    new_image = pygame.transform.rotate(image, angle)
    rect = new_image.get_rect(center = rect.center)
    return new_image, rect

image = pygame.Surface((63, height), pygame.SRCALPHA)
image.blit(seconds, (0, 0))
orig_image = image
rect = image.get_rect(center=(width//2, height//2))

imagem = pygame.Surface((width, height), pygame.SRCALPHA)
imagem.blit(minutes, (0, 0))
orig_imagem = imagem
rect1 = imagem.get_rect(center=(width//2, height//2))

clock = pygame.time.Clock()
done = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    screen.blit(mickey, (0, 0))
    screen.blit(image, rect)
    screen.blit(imagem, rect1)
    image, rect = rotate(orig_image, rect, angle)
    imagem, rect1 = rotate(orig_imagem, rect1, angleM)

    angle -= 0.099
    angleM -= 0.099 / 60


pygame.quit()