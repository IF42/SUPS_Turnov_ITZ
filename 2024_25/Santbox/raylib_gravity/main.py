from pyray import *


WIN_WIDTH = 800
WIN_HEIGHT = 600
G_COEFICIENT = 9.81


if __name__ == '__main__':
    acc_y = 0
    vel_y = 0
    pos_y = WIN_HEIGHT -100

    init_window(WIN_WIDTH, WIN_HEIGHT, "Gravity symulation")
    set_target_fps(30)

    while window_should_close() is False:
        if is_key_pressed(KEY_UP):
            acc_y = -30 

        vel_y += acc_y
        pos_y += vel_y

        if pos_y < WIN_HEIGHT - 100:
            acc_y += G_COEFICIENT
        else:
            pos_y = WIN_HEIGHT - 100
            acc_y = 0
            vel_y = 0

        begin_drawing()
        clear_background(WHITE)
        draw_circle(int(WIN_WIDTH/2), int(pos_y), 10, RED)
        end_drawing()

    close_window()




