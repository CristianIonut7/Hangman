import pygame
import os
import sys
import time


pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Hangman Game")

button_image = pygame.image.load("Assets\Start_button.png")  
button_rect = button_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
random_image_button = pygame.image.load("Assets\surprise.png")
random_image_rect = random_image_button.get_rect(topright=(WIDTH - 10, 10))


font = pygame.font.Font(None, 48)
running = True

def remove_spaces(string):
    return string.replace(" ", "")
def game():
    global screen,running
    print("Game started")
    # Add your game code here

    lives = 6
    word = "XYZ"
    word_underline = "_ " * len(word) #the word to be guessed
    background = pygame.image.load("Assets\image-06.jpg")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    pygame.display.update()


    # XYZ
    # _ _ _
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    typed_letter = chr(event.key).upper()
                    print(typed_letter)
                    if typed_letter in word:
                        print("Correct")
                        # Update the word with the correctly guessed letter
                        word_underline = list(word_underline)
                        for i in range(len(word)):
                            if word[i] == typed_letter:
                                word_underline[i * 2] = typed_letter
                        word_underline = "".join(word_underline)
                    else:
                        print("Incorrect")
                        print("Lives left:", lives)
                        lives -= 1

       


                            
                
        
        
        text_surface = font.render(word_underline, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        lives_surface = font.render(f"Lives: {lives}", True, (0,0,0))

        screen.blit(background, (0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(lives_surface, (10, 10))


        # Check if the game is over
        if lives == 0:
            background = pygame.image.load("Assets\lose.png")
            background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
            screen.blit(background, (0, 0))
            print("Game Over")
            main()
        # Check if the player has won
        copy = remove_spaces(word_underline)
        if copy == word:
            print("You won!")
            background = pygame.image.load("Assets\Win.png")
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
    running = True
    background = pygame.image.load("Assets\Start_game.png")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)


        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        button_rect = button_image.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
        random_image_rect = random_image_button.get_rect(topright=(screen.get_width() - 10, 10))
        
        screen.blit(button_image, button_rect)
        screen.blit(random_image_button, random_image_rect)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                game()
        if random_image_rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                random()
        pygame.display.update()



if __name__ == "__main__":
    main()