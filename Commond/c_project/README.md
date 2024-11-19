# Základní projekt pro jazyk C

# Makefile překladová pravidla
Soubor Makefila obsahuje překladová pravidla, díky kterým je možné libovlý projekt se svou vlastní strukturou souborů překládat jednotným způsobem. Pro spuštění daného překladového pravidla stačí zavolat prorgam make, který si automaticky načte soubor Makefile a předá se mu název požadovaného překladového pravidla.

## Překlad projektu na spustitelný soubor
Tento příkaz spustí překlad zdrojových kódu a vytvoří na výstupu spustitelný soubor.

```
$ make build
```

## Spuštění přeloženého souboru
Protože přeložený soubor ještě nemusí existovat a nebo nemusí být aktuální, protože došlo ke změně zdrojových kódu, je před spuštění samotného spustitelného souboru nejprve automaticky spuštěn překlad.
```
$ make exec
```

## Vyčištění projektového adresáře
Projektový adresář může obsahovat nežádoucí soubory, jako jsou objektové soubory, logové soubory, starý spustitelný soubor, ... Aby se projektový adresář vyčistil od těchto souborů stačí zavolat tento příkaz.

```
$ make clean
```




