#include <stdio.h>

/*
 * Základní řídící konstrukce slouží k řízení toku proramu
 * umožňují větvit program na základě podmínky/stavu a
 * iterovat/opakovat určité sekvence kódu pro dosažení 
 * flexibilního chování
 */

/* 
 * Pro větvení programu slouží konstrukce if-else
 * if (<podmínka>) {<sekvence kódu pokud podmínka platí>}
 * else {<selvence kód pokud podmínka neplatí>}
 */

/*
 * iterace s přesný počtem opakování je v jazyce C definovaná pomocí 
 * klíčového slova for, slouží k opakování určité sekvence kódu

 * for(<řídící proměnné>; <podmínka>; <aktualizace stavu>) 
 * {opakovaná sekvence kódu}
 */

/*
 * podmíněná iterace, která slouží k opakování určité sekvence, ale na 
 * základě platné podmínky, tedy není předem znám počet opakování
 * v každém iteračním cyklu by se tedy měla podmínka změnit a testovat
 * její platnost

 * while(<podmínka>) {opakovaná sekvence kódu}
 */

int main(void) {
    char a = 5;

    if(a > 10) {
        // sekvence kódu pokud podmínka platí
        printf("Promena 'a' je větší než 10\n");
    } else {
        // sekvence kódu pokud podmínka neplatí
        printf("Promena 'a' je menší nebo rovno 10\n");
    }

    for(int i = 0; i < 10; i = i + 1) {
        printf("%d - Hello World\n", i);
    }

    int podminka = 30;
    while(podminka != 21) {
        if(podminka > 21) {
            podminka = podminka - 1;
        } else {
            podminka = podminka + 1;
        }

        printf("%d\n", podminka);
    }

    printf("Program exit..\n");
    return 0;
}