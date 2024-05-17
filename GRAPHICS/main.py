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
fontquestion = pygame.font.Font("Assets\Fonts\DSketch.otf",80)
fonttext = pygame.font.Font("Assets\Fonts\scoobydoo.ttf",22)
fonttext2 = pygame.font.Font("Assets\Fonts\scoobydoo.ttf",20)
fonttext3 = pygame.font.Font("Assets\Fonts\scoobydoo.ttf",25)
running = True

used_letters = []

lives = 6
score = 0

def remove_spaces(string):
    return string.replace(" ", "")

def intrebare():
    global screen,running
    screen.fill((255, 255, 255))

    ###  partea asta e pentru generarea intrebarii bonus
    class Intrebare(ctypes.Structure):
                _fields_ = [("text", ctypes.c_char * 100)]  # Adjust size accordingly

    lib.extrag_intrebare.argtypes = [ctypes.c_char_p, ctypes.POINTER(Intrebare)]
    intrebatoare = Intrebare()
    intrebari_hangman = "intrebari_hangman.txt"
    lib.extrag_intrebare(intrebari_hangman.encode(), ctypes.byref(intrebatoare))

    with open("intrebare.txt", "r") as file:
        content = file.read()
        content = content.split("\n")
        intrebare = content[0]
        vara = content[1]
        varb = content[2]
        varc = content[3]
        vard = content[4]

            
    with open("raspuns.txt", "r") as file:
        raspuns = file.read()

            
            
    print(intrebare)
    print(vara)
    print(varb)
    print(varc)
    print(vard)
    print(raspuns)

    runintrebare = True
    raspunsjucator = ""

    while runintrebare:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                raspunsjucator += event.unicode
                
        RASPUNS = fonttext3.render(raspunsjucator, True, (0,0,0))
        raspunsjucator_rect = RASPUNS.get_rect(center=(screen.get_width() // 2, screen.get_height()-(screen.get_height()-500)))
        raspunsjucator = raspunsjucator.upper()
        print(raspunsjucator)
        if pygame.key.get_pressed()[pygame.K_RETURN]:
            raspunsjucator = raspunsjucator.upper()
            raspunsjucator = raspunsjucator.strip()
            if raspunsjucator == raspuns:
                print("Correct")
                global lives
                runintrebare = False
                lives +=2
                damintrebare = False
                return
            else:
                lose()
        
        
        background = pygame.image.load("Assets\Question display mode.png")
        text = "QUESTION"
        text_surface = fontquestion.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height()-(screen.get_height()-50)))
        text_intrebare = fonttext.render(intrebare, True, (0,0,0))
        text_vara = fonttext2.render(vara, True, (0,0,0))
        text_varb = fonttext2.render(varb, True, (0,0,0))
        text_varc = fonttext2.render(varc, True, (0,0,0))
        text_vard = fonttext2.render(vard, True, (0,0,0))
       

        screen.blit(background, (0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(text_intrebare, (screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-100)))
        screen.blit(text_vara, (screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-200)))
        screen.blit(text_varb, (screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-250)))
        screen.blit(text_varc, (screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-300)))
        screen.blit(text_vard, (screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-350)))
        screen.blit(RASPUNS, raspunsjucator_rect)
        
        pygame.display.update()  

def win():
    global score
    print("You won!")
    score += 100
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background = pygame.image.load("Assets\imaginefinal.png")
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        pygame.display.update()
        time.sleep(3)
        game()      


def lose():
    global score
    score_text = font.render(f"Your score was: {score}", True, (0,0,0))
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        background = pygame.image.load("Assets\lose.png")
        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
        screen.blit(background, (0, 0))
        screen.blit(score_text, (10, screen.get_height() // 2 + 50))
        print("Game Over")
        pygame.display.update()
        


def game():
    
    global screen,running,lives
    lives = 6
    print("Game started")
    # Add your game code here
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


        demintrebare = False
        runintrebare = True
        if lives == 0:
            while runintrebare:
                timetochoose = "Do you want to answer a bonus question? y/n"
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_y:
                            damintrebare = True
                            runintrebare = False
                        if event.key == pygame.K_n:
                            damintrebare = False
                            runintrebare = False

                lives_surface = font.render(f"Lives: {lives}", True, (0,0,0))
                text_surface = fonttext3.render(timetochoose, True, (0,0,0))
                screen.blit(text_surface,(screen.get_width()-(screen.get_width()-10), screen.get_height()-(screen.get_height()-100)))
                screen.blit(lives_surface, (10, 10))
                pygame.display.update()
                
                


        if lives == 0 and damintrebare == False:
            lose()



        if lives == 0 and damintrebare == True:
            intrebare()


        background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))                    
        text_surface = font.render(word_underline, True, (0,0,0))
        text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

        lives_surface = font.render(f"Lives: {lives}", True, (0,0,0))
        score_surface = font.render(f"Score: {score}", True, (0,0,0))
        

        screen.blit(background, (0, 0))
        screen.blit(text_surface, text_rect)
        screen.blit(lives_surface, (10, 10))
        screen.blit(score_surface, (10, 50))


        # Check if the player has won
        copy = remove_spaces(word_underline)
        copyword = word.replace(" ", "")
        if copy == copyword and copy != "":
            win()

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



