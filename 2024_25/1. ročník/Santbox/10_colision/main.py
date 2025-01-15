from pyray import *
import math

init_window(800, 600, "Colision")
set_target_fps(30)

circle_1 = Vector2(400, 300)
circle_1_r = 50
circle_2 = Vector2(400, 500)
circle_2_r=70
SPEED_FACTOR = 5

while window_should_close() is False:
    color = GREEN
    pos_trig = Vector2(circle_1.x, circle_1.y)

    if is_key_down(KEY_UP):
        circle_1.y -= SPEED_FACTOR

    if is_key_down(KEY_DOWN):
        circle_1.y += SPEED_FACTOR

    if is_key_down(KEY_LEFT):
        circle_1.x -= SPEED_FACTOR

    if is_key_down(KEY_RIGHT):
        circle_1.x += SPEED_FACTOR

    distance = math.sqrt(((circle_2.x - circle_1.x) ** 2) + ((circle_2.y - circle_1.y) ** 2))

    if circle_1_r + circle_2_r > distance:
        color = BLUE
        circle_1 = pos_trig

    begin_drawing()
    clear_background(WHITE)
    draw_fps(10, 10)
    draw_circle_v(circle_1, circle_1_r, RED)
    draw_circle_v(circle_2, circle_2_r, color)
    end_drawing()

close_window()



