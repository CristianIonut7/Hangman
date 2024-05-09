import pygame
import os
import sys



pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Hangman Game")

button_image = pygame.image.load("Assets\Start_button.png")  # Replace "button_image.png" with your image file
random_image = pygame.image.load("Assets\surprise.png")
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
button_random = random_image.get_rect(topright=(WIDTH - 10, 10))


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


def random():
    global screen
    background = pygame.image.load("Assets\DnPdIe4A.jpeg")
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
        background = pygame.image.load("Assets\Start_game.png")
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        
        screen.blit(button_image, button_rect)
        screen.blit(random_image, button_random)
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                game()
        if button_random.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                random()
        pygame.display.update()



if __name__ == "__main__":
    main()