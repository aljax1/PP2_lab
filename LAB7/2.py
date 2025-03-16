import pygame
import os

pygame.init()
pygame.mixer.init()  

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")
def show_hotkeys():
    print(" keys:")
    print(" SPACE - Play music")
    print(" S - Stop the music")
    print(" N - Next track")
    print(" P - Previous track")

show_hotkeys()  

music_path = "musics/"
musics = [
    os.path.join(music_path, "1song.mp3"),
    os.path.join(music_path, "2song.mp3"),
    os.path.join(music_path, "3song.mp3"),
    os.path.join(music_path, "4song.mp3"),
    os.path.join(music_path, "5song.mp3")
]

track = 0

pygame.mixer.music.load(musics[track])  
pygame.mixer.music.play()

def play():
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def next_track():
    global track
    track = (track + 1) % len(musics)
    pygame.mixer.music.load(musics[track])
    play()

def prev_track():
    global track
    track = (track - 1) % len(musics)
    pygame.mixer.music.load(musics[track])
    play()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play()
            elif event.key == pygame.K_s:
                stop()
            elif event.key == pygame.K_n:
                next_track()
            elif event.key == pygame.K_p:
                prev_track()

pygame.quit()
