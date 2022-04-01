import pygame
import os
import re

pygame.init()
pygame.mixer.init()

size = weight, height = (500, 500)

screen = pygame.display.set_mode(size)

pygame.display.set_caption('Music Player')

font = pygame.font.SysFont("comicsans", 66)
text = font.render('Music Player', True, (72, 61, 139))

music_list = []

regex = re.compile('(.*mp3$)')

with os.scandir() as entries:
    for entry in entries:
        if entry.is_file():
            if regex.match(entry.name):
                music_list.append(entry.name)

# music_list = ["1.mp3","2.mp3","3.mp3","4.mp3","5.mp3","6.mp3","7.mp3","8.mp3","9.mp3", "10.mp3", "11.mp3"]

SONG_END = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(SONG_END)
pygame.mixer.music.load(music_list[0])
pygame.mixer.music.play()

done = False
pause = False
cnt = 0
pos = 0
font_song = pygame.font.SysFont("comicsans", 20)

def draw_name(num):
    font_song = pygame.font.SysFont("comicsans", 25)
    song = font_song.render(music_list[num], True, (72, 61, 139))
    screen.blit(song, [140, 163])
    pygame.display.update()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == SONG_END:
            cnt += 1
            if cnt == 11:
                cnt = 0
            else:
                pos = pos + cnt
                pygame.mixer.music.load(music_list[pos])
                pygame.mixer.music.play()
                cnt = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            pause = not pause
            # if not pause:
            #     pygame.mixer.music.unpause()
            if pause:
                pygame.mixer.music.pause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            pause = not pause
            if not pause:
                pygame.mixer.music.unpause()
            # pygame.mixer.music.load(music_list[5])
            # pygame.mixer.music.play() 
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            cnt += 1
            if cnt == 11:
                cnt = 0
            else:
                pos = pos + cnt
                pygame.mixer.music.load(music_list[pos])
                pygame.mixer.music.play()
                cnt = 0
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            cnt += 1
            if cnt == 11:
                cnt = 0
            else:
                pos = pos - cnt
                pygame.mixer.music.load(music_list[pos])
                pygame.mixer.music.play()
                cnt = 0
    draw_name(pos)
    screen.fill((199, 21, 133))
    screen.blit(text, [60, 60])
    pygame.display.update()

pygame.quit()