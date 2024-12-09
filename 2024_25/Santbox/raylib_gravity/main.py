from pyray import *

# konstanty, velikost okna a gravitační zrychlení
WIN_WIDTH = 800
WIN_HEIGHT = 600
G_COEFICIENT = 9.81

# stav objektu, zrychlení, rychlost a aktuální pozice v ose y
acc_y = 0
vel_y = 0
pos_y = WIN_HEIGHT -100

# inicializace okna a nastavení FPS
init_window(WIN_WIDTH, WIN_HEIGHT, "Gravity symulation")
set_target_fps(30)

# vykreslovací smyčka
while window_should_close() is False:
    # detekce stisku klávesy šipka nahoru a nastavení zrychlení v opačném směru gravitace
    if is_key_pressed(KEY_UP):
        acc_y = -30 

    # úprava aktuální rychlosti na základě zrychlení a pozici na základě aktuální rychlosti
    vel_y += acc_y
    pos_y += vel_y

    # detekce dopadu na povrch
    if pos_y < WIN_HEIGHT - 100:
        acc_y += G_COEFICIENT
    else:
        pos_y = WIN_HEIGHT - 100
        acc_y = 0
        vel_y = 0

    # vykreslování
    begin_drawing()
    clear_background(WHITE)
    draw_circle(int(WIN_WIDTH/2), int(pos_y), 10, RED)
    end_drawing()

close_window()




