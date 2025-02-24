# Školní rok 2024/25

# Pololetní práce
* Dohodněte se jestli chcete pracovat samostatně nebo ve skupině případně s kým ve skupině chcete pracovat (velikosti skupiny bude odpovídat rozsah výsledné práce)
* Vytvořte si návrh téma na kterém budete pracovat (neomezujte se, buďte kreativní)
* Připravte si malou prezentaci, kterou mi představíte své téma (stačí v bodech na papír, skici, scénáře, zápletky, pointa, ...)
* Ve dnech 12. a 13.3 si společně odprezentujeme připravené návrhy a já vám k tomu dám komentář k realizovatelnosti, případně k postupu realizace

# Tutoriál pro programovací jazyk Python
[https://youtube.com/playlist?list=PLq-XS4UmIwfqCWywdox6fgHSWDuNCjHZ-&si=sOUrMXMBvre-ow5r](https://youtube.com/playlist?list=PLq-XS4UmIwfqCWywdox6fgHSWDuNCjHZ-&si=sOUrMXMBvre-ow5r)

# Tutoriál pro Raylib (PyRay)
[https://youtu.be/UoAsDlUwjy0](https://youtu.be/UoAsDlUwjy0)

# Klon hry Dino
[https://github.com/IF42/Dino](https://github.com/IF42/Dino)


# FPS - frame per second
FPS se používá k měření plynulosti animace ve videohrách a grafických animacích. Vyjadřuje, kolik snímků (obrazů) je zobrazováno/vykresleno za jednu sekundu. Vyšší počet snímků za sekundu znamená plynulejší pohyb a lepší dojem z grafického výstupu. 

Při programování grafické aplikace, nemá cenu nastavovat vyšší vykreslovací frekvenci, než jakou je schopný vykreslovat monitor. Pokud bychom vykreslovali frekvencí 300 FPS, bylo by to zbytečně zatěžující pro hardware počítače, protože monitor tuto frekvenci stejně nedokáže vykreslit a kvalita obrazu by nebyla jiná než u frekvence 100 FPS (v případě běžnoho monitoru, který dokáže vykreslovat cca 60 FPS).

## FPS v kontextu počítačových her
* Pod 30 FPS: Hra se stává trhanou a neplynulou, což může výrazně zhoršit zážitek a způsobit nepříjemné pocity. Například u velmi náročných grafických her je tento výkon často považován za nehratelný.
* 30 FPS: Považováno za minimální akceptovatelnou úroveň pro konzistentní hraní, zejména u konzolových her. Hra je hratelná, ale nemusí být zcela plynulá. Pro pomalejší hry, jako jsou strategie nebo simulátory, je tato úroveň dostatečná.
* 60 FPS: Ideální a považované za standard pro většinu her. Hra je plynulá a responzivní, což výrazně zlepšuje herní zážitek. Toto je běžná cílová hodnota pro mnoho konzolových a PC her.
* 120 FPS a více: Považováno za optimální pro konkurenční hraní a rychlé akční hry, jako jsou FPS (first-persone shooter nebo-li střílečka z pohledu první osoby) a bojové hry. Vyšší FPS poskytuje ještě plynulejší a responzivnější zážitek, což může být výhodou v konkurenčním prostředí.

## Obnovovací frekvence monitoru
Jedná se o schopnost monitoru vykreslit určitý počet snímků během jedné sekundy. Udává se v Hz. Obecně platí, že čím vyšší obnovovací frekvenci monitor má, tím plynulejší obraz poskytuje. Monitory s vyšší obnovovací frekvencí také méně unavují oči. Nejčastěji se setkáte s obnovovací frekvencí 60-75 Hz, u herních monitorů pak dosahují hodnoty až 200 Hz.

Obnovovací frekvence udává, kolikrát se za jednu sekundu překreslí obraz na monitoru. Vyšší frekvence však znamená nejen ostřejší hrany během pohyblivých scén, ale i menší únavu očí. Proto se obrazovky s obnovovací frekvencí (neboli framerate) přes 120 Hz někdy označují jako „flicker free“, protože u nich obraz nebliká. Skvěle se proto hodí pro práci na počítači a hry.

# Zdroj pro studium herní fyziky
[https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics)
[https://www.toptal.com/game/video-game-physics-part-ii-collision-detection-for-solid-objects](https://www.toptal.com/game/video-game-physics-part-ii-collision-detection-for-solid-objects)
[https://www.toptal.com/game/video-game-physics-part-iii-constrained-rigid-body-simulation](https://www.toptal.com/game/video-game-physics-part-iii-constrained-rigid-body-simulation)


# Nastavení prostředí pro programování
Pukud si chcete nastavit prostředí pro vývoj v jazyce Python a v multimediální knihovně raylib, je třeba nainstalovat interpret programovacího jazyka Python, editor zdrojových kódu Microsoft VS code a nainstalovat knihovnu Raylib.
## MS Windows
Na platformě Windows je nejjednodušší si stáhnout interpret programovacího jazyka Python z oficiálních webových stránek [https://www.python.org](https://www.python.org/) a nainstalovat do systému (nezapoměntě před spuštěním instalace zaškrtnou nastavení, že chcete instalaci zahrnout do proměnné PATH, aby systém windows věděl kde je interpret nainstalován).

Editor zdrojových kódů VS code je možné rovněž nainstalovat z oficiálních webových stránek [https://code.visualstudio.com](https://code.visualstudio.com). Instalace je rychlá a přímočará. Po instalaci je pouze třeba si v okně rozšíření nainstalovat plugin Python. 

## GNU Linux 
Na systémech GNU Linux je většinou interpret Pythonu instalován již ve výchozí konfiguraci, ale pokud ne, najděte si postup instalace pro vašidistribuci zadáním klíčových slov do vyhledávače google: <jméno vaší distribuce> install Python

Editor zdrojových kódů VS code je možné instalovat buď z oficiálních stránek [https://code.visualstudio.com](https://code.visualstudio.com/) a nebo bývá součástí balíčkového systému dané distribuce. Po instalaci je pouze třeba si v okně rozšíření nainstalovat plugin Python. 

## Mac OS
Na systémech Mac OS je interpret Pythonu nejsnazší instalovat z oficiálních stránek [https://www.python.org](https://www.python.org/)

Editor zdrojových kódu VS code je možné instalovat z oficiálních stránek [https://code.visualstudio.com](https://code.visualstudio.com/). Po instalaci je pouze třeba si v okně rozšíření nainstalovat plugin Python. 

## Instalace knihovny Raylib
Knihovnu Raylib je možné instalovat na všech platformách stejným způsobem a to v okně terminálu editoru VS code (Terminál -> Nový Terminál) pomocí příkazu: pip install raylib

# Založení projektu
Založení projektu spočívá ve vytvoření projektového adresáře (běžný adresář) a souboru main.py. V editoru VS code přes menu: File -> Open Folder -> Nová složka -> Vybrat Složku.
Do nového složky vytvořit soubor main.py buď přes menu: File -> New File a nebo přes ikony v projektovém EXPLORERU. Pokud byl plugin v editoru VS code správně nainstalován, měly by se po otevření souboru main.py v pravém horním rohu oběvit ikony pro spuštění programu v interpreteru Python.



