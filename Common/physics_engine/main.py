from pyray import *
import engine


WIN_WIDTH=800
WIN_HEIGHT=600

if __name__ == '__main__':
    init_window(WIN_WIDTH, WIN_HEIGHT, "Physics")
    set_target_fps(30)

    while window_should_close() is False:
        begin_drawing()
        clear_background(WHITE)
        end_drawing()

    close_window()



    

