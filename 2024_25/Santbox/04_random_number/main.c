#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char rand_number = rand() % 10;
    int input_number;

    printf("Zadej číslo: ");
    scanf("%d", &input_number);
    printf("\n");
    /*
    Vytvořte podmínku, která vypíše zda proměnná rand_number je rovna 
    proměnné input_number
     */

    if(rand_number == input_number) {
        printf("rand_number je roven input_number\n");
    } else {
        printf("rand_number není roven input_number\n");
    }

    printf("%d %d\n", rand_number, input_number);

    printf("Program exit..\n");
    return 0;
}