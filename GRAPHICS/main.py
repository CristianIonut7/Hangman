import pygame
import os
import sys



pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Hangman Game")

button_image = pygame.image.load("Start.png")  # Replace "button_image.png" with your image file
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))


def game():
    global screen
    print("Game started")
    # Add your game code here
    background = pygame.image.load("ingame.jpeg")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        pygame.display.update()

def main():
    global screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        background = pygame.image.load("background.png")
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        screen.blit(button_image, button_rect)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                game()
        pygame.display.update()



if __name__ == "__main__":
    main()