#include <stdio.h>


// řádkové komentáře, pouze v rámci jednoho řádku

/*
blokové komentáře na více řádků
*/

/*
 * Datové typy slouží k definici velikosti potřebné 
 * paměti pro uložená data a operace které s nimi lze
 * provádět

 * Základní datové typy v jazyce C
 * char - 8bity - pro uložení jednoho znaku
 * short - 16tbitů - pro uložení celého čísla
 * int - 32bitů - pro uložení celého čísla
 * long - 64bitů - pro uložení celého čísla
 * float - 32bitů - pro uložení desetinného čísla
 * double - 64bitů pro uložení desetinného čísla
 */

/*
 * Proměnná je rezervovaná oblast paměti, která slouží k
 * ukládání hodnot v programu
 * Proměnná je definována svým datovým typem a jedinečným
 * identifikátorem
 * 
 * Deklarace proměné:
 * <Datový Typ> <Identifikátor>; 
 *
 * Definice proměnné:
 * <Datový Typ> <Identifikátor> = <Hodnota>;
 */

int main(void) {
    //deklarace proměné 
    int promena1;

    //následovaná její definicí
    promena1 = 27;

    //definice proměnné
    int promena2 = 42;

    printf("promena2 = %d\n", promena2);

    printf("Program exit..\n");
    return 0;
}


