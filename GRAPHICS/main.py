import pygame
import os
import sys
import time
import ctypes

lib = ctypes.CDLL("./lib.so")

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

used_letters = []

def remove_spaces(string):
    return string.replace(" ", "")


def game():
    global screen,running
    print("Game started")
    # Add your game code here
    lives = 6
    with open("./cuvant.txt", "r") as file:
        word = file.read()
        if not word.strip():
            print("File is empty.")
    print(word)
    
    length = len(word)

    lib.codificare_cuvant.argtypes = [ctypes.c_char_p, ctypes.c_int]
    lib.codificare_cuvant.restype = ctypes.c_char_p

    codificat = lib.codificare_cuvant(word.encode("utf-8"), length)

    codificat = str(codificat) # convert from bytes to string

    word_underline = "" # _ _ _ _ _ _ _ _ _
    for i in codificat:
        if i == "_":
            word_underline += "_ "
        if i == " ":
            word_underline += "  "




    lib.extrag_cuvant()

    
    
    print(word_underline)
    
            
    background = pygame.image.load("Assets\image-06.jpg")
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    screen.blit(background, (0, 0))
    pygame.display.update()


    # mediu verde
    # _ _ _ _ _ _ _ _ _
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.VIDEORESIZE:
                screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key >= pygame.K_a and event.key <= pygame.K_z:
                    typed_letter = chr(event.key).lower()
                    if typed_letter in word:
                        print("Correct")
                        word_underline = list(word_underline)
                        for i in range(len(word)):
                            if word[i] == typed_letter:
                                word_underline[i * 2] = typed_letter
                        word_underline = "".join(word_underline)
                        used_letters.append(typed_letter)

                                    
                    else:
                        print("Incorrect")
                        print("Lives left:", lives)
                        if typed_letter not in used_letters:
                            lives -= 1
                            used_letters.append(typed_letter)



        
        match lives:
            case 6:
                background = pygame.image.load("Assets\image-06.jpg")  
            case 5:
                background = pygame.image.load("Assets\Fundaluri\In-game1.png")
            case 4:
                background = pygame.image.load("Assets\Fundaluri\In-game2.png")
            case 3:
                background = pygame.image.load("Assets\Fundaluri\In-game3.png")
            case 2:
                background = pygame.image.load("Assets\Fundaluri\In-game4.png")
            case 1:
                background = pygame.image.load("Assets\Fundaluri\In-game5.png")
            case _:
                background = pygame.image.load("Assets\image-06.jpg")


        if lives == 1:
            pass #bonus question
            


        
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))                    
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
            python_executable = sys.executable
    
            # Get the path of the current script
            script_path = os.path.abspath(__file__)
    
            # Call another instance of the program
            os.execl(python_executable, python_executable, script_path)
            
        # Check if the player has won
        copy = remove_spaces(word_underline)
        copyword = word.replace(" ", "")
        if copy == copyword:
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



