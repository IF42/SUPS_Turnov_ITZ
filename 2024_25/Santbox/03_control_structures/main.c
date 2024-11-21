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
 * relační operátory
 * relace = vztah, relační operátory umožňují definovat vztah mezi dvěmi hodnotami
 * relační operátory v jazyce C jsou:
 * a > b (a je větší než b)
 * a < b (a je menší než b)
 * a >= b (a je větší nebo rovno b)
 * a <= b (a je menší nebo rovno b)
 * a == b (a je rovno b)
 * a != b (a není rovno b)
 */


/*
 * iterace s přesný počtem opakování je v jazyce C definovaná pomocí 
 * klíčového slova for, slouží k opakování určité sekvence kódu
 *
 * for(<řídící proměnné>; <podmínka>; <aktualizace stavu>) 
 * {opakovaná sekvence kódu}
 */

/*
 * podmíněná iterace, která slouží k opakování určité sekvence, ale na 
 * základě platné podmínky, tedy není předem znám počet opakování
 * v každém iteračním cyklu by se tedy měla podmínka změnit a testovat
 * její platnost
 *
 * while(<podmínka>) {opakovaná sekvence kódu}
 */

int main(void) {
    char a = 10;

    if (a > 10) {
        // sekvence kódu pokud podmínka platí
        printf("Promena 'a' je větší než 10\n");
    } else {
        // sekvence kódu pokud podmínka neplatí
        printf("Promena 'a' je menší nebo rovno 10\n");
    }

    /* smyčka for 
     * zacyklení - stav, kdy nedojde nikdy k zneplatnění relačního výrazu
     * tvořící hlavičku cyklu 
     * To znamená, že cyklus se vykonává do nekonečna a dojde k zablokování
     * programu
     * Jediný způsob jak takový program odblokovat je ho násilně ukončit!!!
     * Zacyklení je jednou z častých chyb v programu
     */
    int max = 5;
    for (int i = 0; i < max; i = i+1) {
        printf("%d - Hello World\n", i);
    }

    int temperature = 15;
    int setpoint = 21;
    while(temperature != setpoint) {
        if(temperature > setpoint) {
            temperature = temperature - 1;
            printf("chladím temperature: %d setpoint: %d\n", temperature, setpoint);
        } else {
            temperature = temperature + 1;
            printf("topím temperature: %d setpoint: %d\n", temperature, setpoint);
        }
    }

    printf("Program exit..\n");
    return 0;
}
