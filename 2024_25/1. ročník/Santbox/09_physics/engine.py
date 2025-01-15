from pyray import Vector2, Rectangle
import math


class Signal:
    def __init__(self):
        self.event = {}

    def connect(self, name, slot):
        self.event[name] = slot

    def emit(self, name, *args, **kwargs):
        if name in self.event:
            self.event[name](*args, **kwargs)
     

class Colision_Rect:
    def __init__(self, size: Rectangle):
        self.size = size

    def check_colision(self, other: Rectangle):
        x_center_1 = (self.size.x + self.size.x + self.size.width) / 2
        y_center_1 = (self.size.y + self.size.y + self.size.height) / 2
        x_center_2 = (other.size.x + other.size.x + other.size.width) / 2
        y_center_2 = (other.size.y + other.size.y + other.size.height) / 2

        normal_x = x_center_2 - x_center_1
        normal_y = y_center_2 - y_center_1

        distance = math.sqrt((normal_x) ** 2  + (normal_y) ** 2)

        if distance > 0 and (distance < (self.size.width + other.size.width) / 2 or distance < (self.size.height + other.size.height) / 2):
            return Vector2(normal_x / distance, normal_y / distance)
        else:
            return None
        

class MassPoint(Signal):
    def __init__(self, pos: Vector2, vel: Vector2, acc: Vector2):
        super().__init__()
        self.pos = pos
        self.vel = vel
        self.acc = acc

    def reflection(self, normal: Vector2):
        # update of acceleration
        dot_product = (self.acc.x * normal.x) + (self.acc.y * normal.y)
        self.acc.x = self.acc.x - 2 * dot_product * normal.x
        self.acc.y = self.acc.y - 2 * dot_product * normal.y

        # update of velocity
        dot_product = (self.vel.x * normal.x) + (self.vel.y * normal.y)
        self.vel.x = self.vel.x - 2 * dot_product * normal.x
        self.vel.y = self.vel.y - 2 * dot_product * normal.y

    def inertia(self, normal: Vector2):
        self.acc.x += normal.x
        self.acc.y += normal.y
        
        self.vel.x += self.acc.x
        self.vel.y += self.acc.y

        self.pos.x += self.vel.x
        self.pos.y += self.vel.y

    def colision(self, other):
        pass

    def update(self):
        pass


class Engine:
    def __init__(self):
        self.obj_list = []

    # observer pattern for handling user inputs
    def emit_signal(self, signal, *args, **kwargs):
        for obj in self.obj_list:
            obj.emit(signal, *args, **kwargs)

    def add_object(self, obj):
        self.obj_list.append(obj)

    def update(self):
        for i, obj in enumerate(self.obj_list):
            for other in self.obj_list:
                obj.colision(other)

            obj.update()


