// IMPLEMENTARE - HANGMAN

#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// structura pentru lista SIMPLU INLANTUITA folosita
typedef struct element
{
    char litera;
    struct element *urmator;
} nod;

// structura pentru stocarea string-urilor-cheie din sectiunea de intrebari
typedef struct intrebari
{
    char *intrebare;
    char *var_A;
    char *var_B;
    char *var_C;
    char *var_D;
    char *raspuns;
} intrebare;

// functie de extragere aleatorie a cuvantului de ghicit din lista de cuvinte
void extrag_cuvant(char word_hangman[], int *dimensiune)
{
    FILE *fisier_text;
    int index_cuvant_exp; // marcheaza randul in care e afla cuvantul propus de ghicit
    fisier_text = fopen("cuvinte.txt", "rt");
    if (fisier_text == NULL) // se verifica daca se poate efectua citirea din fisierul de cuvinte
    {
        printf("ERROR! THE WORD LIST FILE COULD NOT BE READ!");
        return;
    }
    else
    {
        srand(time(0)); // Se asigura ca la fiecare utilizare / timp de executie se alege cu cuvant diferit din cadrul generatorului de cuvinte
        index_cuvant_exp = rand() % 100;

        for (int indice = 1; indice < index_cuvant_exp; indice++)
        {
            fgets(word_hangman, 100, fisier_text);
        }

        fgets(word_hangman, 100, fisier_text);
        word_hangman[strcspn(word_hangman, "\n")] = '\0'; // inlocuieste caracterul '\n' cu terminatorul de sir ('\0')
        *dimensiune = strlen(word_hangman);
        fclose(fisier_text);
    }
}

// functie de adaugare caracter cuvant in lista simplu inlantuita (creare lista)
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

// functie de afisare a caracterelor (pe masura in care sunt ghicite) - a se vedea functiile de modificari
void afisare_element_lista_CODIFICAT(nod *inceput)
{
    nod *curent;
    for (curent = inceput; curent != NULL; curent = curent->urmator)
    {
        if (curent->litera == ' ')
        {
            printf(" | ");
        }
        else
        {
            if (curent->litera > 'Z')
                printf("%c", curent->litera);
            else
                printf("%c", (curent->litera) + 32);
        }
    }
}

// modifica a doua lista (identica initial cu prima) sub o forma codificata
void modificare(nod **inceput2, int *dimensiune)
{
    nod *curent;
    for (curent = (*inceput2); curent != NULL; curent = curent->urmator)
    {
        if (curent->litera != ' ')
        {
            curent->litera = '_';
        }
        else
        {
            (*dimensiune)--;
        }
    }
}

// modifica lista 2 in timp ce parcurge ambele liste in paralel!
// daca este ghicit un caracter de pe o anumita pozitie din lista 1, codificarea se schimba in elementul simetric din lista 2!
// se tine cont de case insensitive si de literele ghicite!
void modificare2(nod **inceput2, nod *inceput, char caracter, int *ghicit, int *nr_litere_ghicite)
{
    nod *curent, *curent2;
    for (curent = inceput, curent2 = *inceput2; curent != NULL && curent2 != NULL; curent = curent->urmator, curent2 = curent2->urmator)
    {
        if (curent->litera == caracter || curent->litera == caracter + 32)
        {
            curent2->litera = caracter;
            *ghicit = 1;
        }
        if ((curent2->litera >= 'a' && curent2->litera <= 'z') || (curent2->litera >= 'A' && curent2->litera <= 'Z'))
        {
            (*nr_litere_ghicite)++;
        }
    }
}

// functie de extragere string-uri necesare intrebarii pentru puncte bonus
void extrag_intrebare(char intrebari_hangman[], intrebare *intrebatoare)
{
    FILE *fisier_text;
    char *expresie;
    int index_intrebare_exp; // marcheaza randul in care se afla intrebarea
    fisier_text = fopen("Intrebari.csv", "rt");
    if (fisier_text == NULL) // se verifica daca se poate efectua citirea din fisierul de cuvinte
    {
        printf("ERROR! IMPOSIBLE TO READ THIS FILE!");
        exit(1); // Iesirea din program daca citirea fisierului esueaza
    }
    else
    {
        srand(time(0));                        // Asigurarea alegerii unui cuvant diferit la fiecare utilizare/timp de executie
        index_intrebare_exp = rand() % 20 + 1; // se evita primul rand, introductiv al fisierului csv

        for (int indice = 0; indice < index_intrebare_exp; indice++)
        {
            fgets(intrebari_hangman, 1000, fisier_text);
        }

        fgets(intrebari_hangman, 1000, fisier_text);
        fclose(fisier_text);

        expresie = strtok(intrebari_hangman, ",");
        int column = 0; // indică coloana curentă (1 - intrebare, 2 - var_A, 3 - var_B, 4 - var_C, 5 - var_D, 6 - raspuns)

        while (expresie != NULL)
        {
            switch (column) // extragere string-uri pe coloane adecvate / impartirea pe expresii separate prin virgula
            {
            case 1:
                intrebatoare->intrebare = strdup(expresie); // duplicare de string
                printf("\n%s", intrebatoare->intrebare);
                break;
            case 2:
                intrebatoare->var_A = strdup(expresie);
                printf("\nA) %s", intrebatoare->var_A);
                break;
            case 3:
                intrebatoare->var_B = strdup(expresie);
                printf("\nB) %s", intrebatoare->var_B);
                break;
            case 4:
                intrebatoare->var_C = strdup(expresie);
                printf("\nC) %s", intrebatoare->var_C);
                break;
            case 5:
                intrebatoare->var_D = strdup(expresie);
                printf("\nD) %s", intrebatoare->var_D);
                break;
            case 6:
                intrebatoare->raspuns = strdup(expresie);
                size_t len = strlen(intrebatoare->raspuns); // Obtine lungimea șirului
                if (len > 0 && intrebatoare->raspuns[len - 1] == '\n')
                {
                    intrebatoare->raspuns[len - 1] = '\0'; // Eliminare '\n' de la sfarsitul sirului
                    // pentru a se face compararea corespunz cu raspunsul tastat
                }
                break;
            default:
                break;
            }
            expresie = strtok(NULL, ",");
            column++;
        }
    }
}

// functie de ghicire caracter + implementare mod salvare cu intrebari si raspunsuri pentru doua vieti extra
void ghicire_si_sansa(nod *inceput, nod *inceput2, int dimensiune, int nr_sanse, char word_hangman[], intrebare *intrebatoare, char intrebari_hangman[], char caractere_introduse[])
{
    char caracter, alegere, variante_alese[10];
    int nr_greseli = 0, ghicit, nr_litere_ghicite = 0;
    nod *curent;

    // ghicirea se termina cand numarul de vieti (nr_sanse) e mai mic decat cel de greseli sau cand au fost ghicite toate seturile de litere
    while (nr_greseli < nr_sanse && nr_litere_ghicite < dimensiune)
    {
        nr_litere_ghicite = 0;
        ghicit = 0;
        printf("\nCHOOSE A LETTER & GUESS!\n");

        char input[100]; // Presupunem ca input-ul NU va depasi 100 de caractere
        fgets(input, sizeof(input), stdin);

        // Extragerea primului caracter
        caracter = input[0];

        // Verificare daca caracterul/ inputul introdus este o litera (intre A si Z)
        if ((caracter < 'A' || caracter > 'Z') && (caracter < 'a' || caracter > 'z'))
        {
            printf("Invalid input! Please enter a letter (A-Z).\n");
            continue; // Trecere la urmatoarea iteratie, fara a scadea din sanse daca caracterul tastat NU e litera
        }

        // Convertire lowercase - uppercase
        if (caracter >= 'a' && caracter <= 'z')
            caracter -= 'a' - 'A';

        // Verificare daca litera respectiva a fost anterior ghicita / introdusa
        if (caractere_introduse[caracter - 'A'] == 1)
        {
            printf("You have already typed this letter. Please choose another one.\n");
            continue; // Trecere la urmatoarea iteratie
        }

        // marcare litera ghicita in cadrul vectorului de litere (alfabet englez, cu 26 de litere)
        caractere_introduse[caracter - 'A'] = 1;

        // Actualizare modificare2
        modificare2(&inceput2, inceput, caracter, &ghicit, &nr_litere_ghicite);
        afisare_element_lista_CODIFICAT(inceput2);

        if (ghicit == 1)
        {
            printf("\n\nYou guessed: %c\n--------------------\n", caracter);
        }
        else
        {
            int numar_vieti = nr_sanse - nr_greseli - 1;
            printf("\n\nWrong guess! Lives: %d | TRY AGAIN!\n--------------------------\n", numar_vieti);
            nr_greseli++;
        }
    }

    // daca s-a epuizat numarul de vieti, jucatorul poate alege sa paraseasca jocul
    // sau sa raspunda la o intrebare pentru doua vieti extra
    if (nr_greseli >= nr_sanse)
    {
        printf("YOU HAVE NO LIVES LEFT! WOULD YOU LIKE TO ANSWER A QUESTION TO GET 2 (EXTRA) LIVES? [y/n]\n");
        scanf("%c", &alegere);
        if (alegere == 'n')
        {
            printf("GAME OVER! The word/expression you had to guess was: %s.", word_hangman);
        }
        else
        {
            extrag_intrebare(intrebari_hangman, intrebatoare);
            printf("\n\nTO ANSWER, PRESS ONE OR MORE KEYS (LETTERS) (FOLLOWED BY <<&>>, FROM LETTER A TO D - IF THERE ARE MULTIPLE CORRECT CHOISES) - EXAMPLE: <<X&Y&Z>>: ");
            scanf("%s", &variante_alese);
            if (strcmp(variante_alese, intrebatoare->raspuns) == 0)
            {
                printf("YOU ANSWERED CORRECTLY! 2 BONUS LIVES ADDED! LET'S CONTINUE...");
                getchar(); // se preia caracterul '\n' din buffer
                ghicire_si_sansa(inceput, inceput2, dimensiune, 2, word_hangman, intrebatoare, intrebari_hangman, caractere_introduse);
            }
            else
            {
                printf("INCORRECT ANSWER! ANSWER: %s", intrebatoare->raspuns);
                printf("\nGAME OVER! The word/expression you had to guess was: %s.", word_hangman);
            }
        }
    }

    // mesaj specific in cazul in care cuvantul e ghicit in intregime
    else if (nr_greseli < nr_sanse && nr_litere_ghicite == dimensiune)
    {
        printf("CONGRATULATIONS! YOU GUESSED THE ENTIRE WORD / EXPRESSION: %s", word_hangman);
    }
}

int main()
{
    char cuvant_hangman[100], caracter, intrebari_hangman[1000];
    int dimensiune, nr_sanse = 7;
    char caractere_introduse[26] = {0}; // Vector pentru a stoca caracterele introduse (A-Z)
    nod *inceput = NULL, *inceput2 = NULL;
    intrebare *intrebatoare = malloc(sizeof(intrebare));

    extrag_cuvant(cuvant_hangman, &dimensiune);
    adaug_in_lista(cuvant_hangman, dimensiune, &inceput);
    adaug_in_lista(cuvant_hangman, dimensiune, &inceput2);
    modificare(&inceput2, &dimensiune);

    printf("\nTHE EXPRESSION YOU HAVE TO GUESS LOOKS LIKE THIS: ");
    afisare_element_lista_CODIFICAT(inceput2);
    ghicire_si_sansa(inceput, inceput2, dimensiune, nr_sanse, cuvant_hangman, intrebatoare, intrebari_hangman, caractere_introduse);
    return 0;
}