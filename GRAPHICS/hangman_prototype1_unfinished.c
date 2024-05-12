#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

//structura pentru lista SIMPLU INLANTUITA folosita
typedef struct element
{
    char litera;
    struct element *urmator;
} nod;

//functie de extragere aleatorie a cuvantului de ghicit din lista de cuvinte
char* extrag_cuvant()
{
    FILE *fisier_text;
    int index_cuvant_exp; //marcheaza randul in care e afla cuvantul propus de ghicit
    fisier_text = fopen("cuvinte.txt", "rt");
    char *word_hangman = (char *)malloc(100 * sizeof(char));
    if (fisier_text == NULL) //se verifica daca se poate efectua citirea din fisierul de cuvinte
    {
        printf("ERROR! THE WORD LIST FILE COULD NOT BE READ!");
        return 0;
    }
    else
    {
        srand(time(0)); //Se asigura ca la fiecare utilizare / timp de executie se alege cu cuvant diferit din cadrul generatorului de cuvinte
        index_cuvant_exp = rand() % 10;

        for (int indice = 1; indice < index_cuvant_exp; indice++)
        {
            fgets(word_hangman, 100, fisier_text);
        }

        fgets(word_hangman, 100, fisier_text);
        word_hangman[strcspn(word_hangman, "\n")] = '\0'; //inlocuieste caracterul '\n' cu terminatorul de sir ('\0')
        fclose(fisier_text);
    }
    FILE *fisier_cuvant;
    fisier_cuvant = fopen("cuvant.txt", "w");
    fprintf(fisier_cuvant, "%s", word_hangman);
    return word_hangman;

}

//funnctie de adaugare caracter cuvant in lista simplu inlantuita (creare lista)
void adaug_in_lista(char word_hangman[], int dimensiune, nod **inceput)
{
    nod *intermediar = NULL;

    for (int indice = 0; indice < dimensiune; indice++)
    {
        if (*inceput == NULL)
        {
            (*inceput) = malloc(sizeof(nod));
            (*inceput)->litera = word_hangman[0];
            (*inceput)->urmator = NULL;
            intermediar = (*inceput);
        }
        else
        {
            intermediar->urmator = malloc(sizeof(nod));
            intermediar = intermediar->urmator;
            intermediar->litera = word_hangman[indice];
            intermediar->urmator = NULL;
        }
    }
}

char* afisare_element_lista_CODIFICAT(nod *inceput)
{
    nod *curent;
    int i = 0;
    char *elementcodificat = (char *)malloc(100 * sizeof(char));
    for (curent = inceput; curent != NULL; curent = curent->urmator)
    {
        if (curent->litera == ' ')
        {
            printf(" | ");
            elementcodificat[i] = ' ';
            i++;
        }
        else
        {
            printf("%c", curent->litera);
            elementcodificat[i] = curent->litera;
            i++;
        }

    }
    return elementcodificat;
}

void modificare(nod **inceput2)
{
    nod *curent;
    for (curent = (*inceput2); curent != NULL; curent = curent->urmator)
    {
        if (curent->litera != ' ')
        {
            curent->litera = '_';
        }
        
    }
}

void modificare2(nod **inceput2, nod *inceput, char caracter, int *ghicit, int *nr_litere_ghicite)
{
    nod *curent, *curent2;
    for (curent = inceput, curent2 = *inceput2; curent != NULL && curent2 != NULL; curent = curent->urmator, curent2 = curent2->urmator)
    {
        if (curent->litera == caracter)
        {
            curent2->litera = caracter;
            *ghicit = 1;
            (*nr_litere_ghicite)++;
        }
    }
}

void ghicire(nod *inceput, nod *inceput2, int dimensiune, int nr_sanse, char word_hangman[])
{
    char caracter;
    int nr_greseli = 0, ghicit, nr_litere_ghicite = 0;
    nod *curent;
    while (nr_greseli < nr_sanse && nr_litere_ghicite < dimensiune - 1)
    {
        ghicit = 0;
        printf("\nCHOOSE A LETTER & GUESS!\n");
        scanf(" %c", &caracter);
        modificare2(&inceput2, inceput, caracter, &ghicit, &nr_litere_ghicite);
        afisare_element_lista_CODIFICAT(inceput2);
        if (ghicit == 1)
            {
                printf("\n\nYou guessed: %c\n-----------------\n", caracter);
            }
            else
            {
                printf("\n\nWrong guess! TRY AGAIN!\n--------------------------\n");
                nr_greseli++;
            }
    }
    if (nr_greseli >= nr_sanse)
    {
        printf("GAME OVER! The word/expression you had to guess was: %s", word_hangman);
    }
    else if (nr_greseli < nr_sanse && nr_litere_ghicite == dimensiune - 1)
    {
        printf("CONGRATULATIONS! YOU GUESSED CORRECTLY THE ENTIRE WORD: %s", word_hangman);
    }
}

char* codificare_cuvant(char cuvant_hangman[100], int dimensiune)
{
    char *elementcodificat = malloc(100 * sizeof(char));

    for (int indice = 0; indice < dimensiune; indice++)
    {
        if (cuvant_hangman[indice] == ' ')
        {
            elementcodificat[indice] = ' ';

        }
        else
        {
            elementcodificat[indice] = '_';
            elementcodificat[indice + 1] = ' ';
        }
    }

    return elementcodificat;
}

int main()
{

    char *cuvant_hangman, caracter;
    int dimensiune;
    cuvant_hangman = (char *)malloc(100 * sizeof(char));
    nod *inceput = NULL, *inceput2 = NULL;
    strcpy(cuvant_hangman,extrag_cuvant());
    printf("THE WORD/EXPRESSION TO GUESS IS: %s\n", cuvant_hangman);
    dimensiune = strlen(cuvant_hangman);
    adaug_in_lista(cuvant_hangman, dimensiune, &inceput);
    adaug_in_lista(cuvant_hangman, dimensiune, &inceput2);

    modificare(&inceput2);

    

    

    
    char *cuvant_codificat = (char *)malloc(100 * sizeof(char));
    strcpy(cuvant_codificat, codificare_cuvant(cuvant_hangman, dimensiune));
    printf("cuvant_codificat: %s", cuvant_codificat);
    


    //ghicire(inceput, inceput2, dimensiune, 7, cuvant_hangman);
    return 0;
}