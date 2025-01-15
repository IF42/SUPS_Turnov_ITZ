# zavedení knihovny pyray/raylib do zdrojového kódu
from pyray import *

# inicializace grafického okna a nastavení frekvence vykreslování, 
# to znamená kolikrát se vykoná tělo vykreslovací smyčky za sekundu
init_window(800, 600, "GUI Windows")
set_target_fps(25)

# proměnná defunující pozici textu v x-ové ose 
text_pos_x = 0

# vykreslovací smyčka, která se vykonává dokud není okno programu zavřeno
# funkce window_should_close vrací True ve chvíli kdy je okno programu zavřeno, 
# v opačném případě vrací hodnotu False 
#
# příkaz while vytváří podmíněný cyklus, který se cyklicky opakuje doku platí podmínka
while window_should_close() is False:
    # cokoli je vykreslováno do grafického okna se musí nacházet mezi begin/end_drawing příkazy
    begin_drawing()

    #vyčištění pozadí okna do určité barvy
    clear_background(WHITE)

    #vykreslení aktuální hodnoty FPS, pozice [0, 0] se nachází v levém horním rohu grafického okna
    draw_fps(10,10)

    draw_text("Hello World", text_pos_x, 300, 15, RED)
    end_drawing()

    # aktualizace pozice textu v každé vykreslovací iteraci
    text_pos_x = (text_pos_x + 1) % 600

# korektní uzavření grafického okna
close_window()




