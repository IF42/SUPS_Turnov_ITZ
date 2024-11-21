#include <stdio.h>

/*
 * Funkce v jazyce C
 * Funkce v jazyce C jsou prostředkem pro budovnání abstrakce ve zdrojovém kódu
 * Pojmenovaná sekvence kód která může mít svůj vstup a svůj výstup
 * 
 * Funkce je definována svým návratovým datovým typem, svým jedinečným identifikátorem a 
 * seznamem vstupních parametrů
 * 
 * <návratový datový typ> <identifikátor> (<sezname vstupních parametrů>) {tělo funkce}
 * 
 * Návratový datový typ funkce říká, že výsledkem činnosti funkce je nějaký výsledek, který
 * bude daného datového typu
 * 
 * Použití definované funkce v programu se nazývá volání funkce. Funkce se zavolá v programu
 * zapsáním identifikátoru funkce a zapsáním vstupních parametrů do závorek.
 * <identifikýtor> (<seznam vstupních hodnot>); 
 */


int secti (int a, int b) {
    int vysledek = a + b; 
    return vysledek;
}

/*
 * V jazyce C je speciální datový typ, který vyjadřuje tzv prázdný datový typ.
 * Tento datový typ má nulovou bytovou šířku a nemá definované žádné operace, které 
 * nad tímto datovým typem lze vykonávat.
 * Tento datový typ se nazývá void a slouží k definici, že funkce nemá žádný výstup a 
 * zároveň umožňuje definovat, že nemá žádný vstup
 * funkce, která nemá, žádný vstup a žádný výstup se nazývá procedůra
 */
void say_hi(void) {
    printf("Hi my lord\n");
}

/*
 * Koncept funkce umožňuje vytvářet logicky členěný kód, díky kterému je možné rozdělit
 * celý program na logické vrstvy, kde na každé vrstvě je možné řešit problém z urité vrstvy
 * abstrakce
 * To znamená pokud potřebujete vypočítat například úhly trojůhelníku pomocí funkce sinus, 
 * nezajímá vás jak funguje funkce sinus, ale pouze to co je jejím vstupem a co je jejím výstupem
 */


int main(void) {
    int vstup_a = 1;
    int vstup_b = 2;
    int muj_vysledek = secti(vstup_a, vstup_b);

    printf("vy%d\n", muj_vysledek);

    say_hi();

    printf("Program exit..\n");
    return 0;
}




