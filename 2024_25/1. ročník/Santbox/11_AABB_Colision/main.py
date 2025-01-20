from pyray import *
from math import sqrt


#set_config_flags(FLAG_VSYNC_HINT)
init_window(800, 600, "Kolize")
set_target_fps(500)

circle_1 = Vector2(400, 300)
circle_1_r = 40

circle_2 = Vector2(400, 500)
circle_2_r = 50

SPEED_FACTOR = 150
circle_color = Color(23, 42,55, 255)
alfa = 255

while window_should_close() is False:
    frame_time = get_frame_time()

    # pohyb v ose y
    if is_key_down(KEY_UP):
        circle_1.y -= SPEED_FACTOR * frame_time
    elif is_key_down(KEY_DOWN):
        circle_1.y += SPEED_FACTOR * frame_time
    
    # pohyb v ose x
    if is_key_down(KEY_LEFT):
        circle_1.x -= SPEED_FACTOR * frame_time
    elif is_key_down(KEY_RIGHT):
        circle_1.x += SPEED_FACTOR * frame_time

    distance = sqrt((circle_2.x - circle_1.x) ** 2 + (circle_2.y - circle_1.y) ** 2)
    
    if circle_1_r + circle_2_r > distance:
        # došlo ke kolizi
        if alfa > 0:
            alfa -= (30 * frame_time)
    else:
        alfa = 255

    circle_color.a = int(alfa)

    begin_drawing()
    clear_background(WHITE)
    draw_fps(10, 10)

    draw_circle_v(circle_1, circle_1_r, RED)
    draw_circle_v(circle_2, circle_2_r, circle_color)    

    end_drawing()

close_window()



