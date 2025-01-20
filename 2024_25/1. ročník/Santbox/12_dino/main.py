from pyray import *

WIN_WIDTH = 800
WIN_HEIGHT = 600

set_config_flags(FLAG_VSYNC_HINT)
init_window(WIN_WIDTH, WIN_HEIGHT, "Dino")
set_target_fps(144)

road_texture = load_texture("graphics/road_template.png")
cloud_texture = load_texture("graphics/cloud_template.png")

road_x = 0

while window_should_close() is False:
    road_x = (road_x + 1) % road_texture.width

    begin_drawing()
    clear_background(WHITE)
   
    draw_fps(10, 10)
    draw_texture_pro(
        road_texture                                        # Odkaz na texturu
        , Rectangle(road_x, 0, WIN_WIDTH, road_texture.height)   # pozice velikost výřezu obrázku
        , Rectangle(0, 500, WIN_WIDTH, road_texture.height) # pozice vykreslení a škálování velikosti obr.
        , Vector2(0, 0)                                     # počátek pro vykreslení (levý hroní roh obr.)
        , 0                                                 # úhel natočení obrázku
        , WHITE)                                            # barva pozadí obrázku

    end_drawing()

unload_texture(road_texture)
unload_texture(cloud_texture)
close_window()







