from pyray import *
import engine as eng
import random 


WIN_WIDTH=800
WIN_HEIGHT=600
FPS=60 


class Player(eng.MassPoint):
    def __init__(self):
        self.width = 50
        self.height = 50

        super().__init__(Vector2(random.randint(1, WIN_WIDTH), random.randint(1, WIN_HEIGHT)), Vector2(10, 10), Vector2(0, 0))
        self.colision_rect = eng.Colision_Rect(Rectangle(self.pos.x, self.pos.y, self.width, self.height));    
        self.colision_status = False 

        self.NORMAL_VEC_TOP = Vector2(0, -1)
        self.NORMAL_VEC_BOTTOM = Vector2(0, 1)
        self.NORMAL_VEC_LEFT = Vector2(-1, 0)
        self.NORMAL_VEC_RIGHT = Vector2(1, 0)
        self.NORMAL_ACC_G = Vector2(0, 9.81)
        

    def colision(self, other):
        overlap = self.colision_rect.check_colision(other.colision_rect)

        if overlap is not None:
            if self.colision_status is False:
                self.reflection(overlap)
                self.colision_status = True
        else:
            self.colision_status = False

    def update(self):
        self.inertia(Vector2(0, 0))

        # update of position of colision rectangle 
        # TODO: improve internal structure of mass object for automatic update of colision rectangle position
        self.colision_rect.size.x = self.pos.x
        self.colision_rect.size.y = self.pos.y        

        if self.pos.y == WIN_HEIGHT:
            self.reflection(self.NORMAL_VEC_BOTTOM)
        elif self.pos.y > WIN_HEIGHT:
            self.vel.y = -5
        elif self.pos.y == 0:
            self.reflection(self.NORMAL_VEC_TOP)
        elif self.pos.y < 0:
            self.vel.y = 5
        elif self.pos.x == WIN_WIDTH:
            self.reflection(self.NORMAL_VEC_RIGHT)
        elif self.pos.x > WIN_WIDTH:
            self.vel.x = -5
        elif self.pos.x == 0:
            self.reflection(self.NORMAL_VEC_LEFT)
        elif self.pos.x < 0:
            self.vel.x = 5

        draw_rectangle_v(self.pos, Vector2(50, 50), RED)


init_window(WIN_WIDTH, WIN_HEIGHT, "Physics")
set_target_fps(FPS)

engine = eng.Engine()
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())
engine.add_object(Player())

while window_should_close() is False:
    begin_drawing()
    clear_background(WHITE)
    draw_fps(10, 10)
    engine.update()
    end_drawing()

close_window()

