from pyray import *

init_window(800, 600, "Colision detection")
set_target_fps(30)

square = Rectangle(400, 300, 50, 50)
SPEED_FACTOR = 5

fixed_point = Rectangle(400, 500, 50, 50)

while window_should_close() is False: 
    old_x = square.x
    old_y = square.y

    # posouvání čtverce pomocí kláves 
    if is_key_down(KEY_UP):
        square.y -= SPEED_FACTOR
    
    if is_key_down(KEY_DOWN):
        square.y += SPEED_FACTOR

    if is_key_down(KEY_LEFT):
        square.x -= SPEED_FACTOR

    if is_key_down(KEY_RIGHT):
        square.x += SPEED_FACTOR 

    d1x = fixed_point.x - (square.x + square.width)         # průnik do levé hrany fixního čtverce
    d1y = fixed_point.y - (square.y + square.height)        # průnik do spodní hrany fixního čtverce
    d2x = square.x - (fixed_point.x + fixed_point.width)    # průnik do pravé hrany fixního čtverce
    d2y = square.y - (fixed_point.y + fixed_point.height)   # průník do horní hrany fixního čtverce

    # detekce kolize s fixním čtvercem, v takovém případě se nepovolí posun pohyblívého čtverce
    # při průniku do hrany čtverce je rozdíl koncových bodů záporný
    if not(d1x >= 0 or d1y >= 0 or d2x >= 0 or d2y >= 0):
        square.x = old_x
        square.y = old_y

    begin_drawing()
    clear_background(WHITE)
    draw_fps(10, 10)

    # vykreslení objektů v okně
    draw_rectangle_rec(square, RED);
    draw_rectangle_rec(fixed_point, YELLOW);
    
    end_drawing()

close_window()

