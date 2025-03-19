class Strategy_Start:
    def __init__(self):
        pass
    
    def execute(self):
        print("Wait for key press...")

class Strategy_Run:
    def __init__(self):
        pass
    
    def execute(self):
        print("Game is running")

class Strategy_GameOver:
    def __init__(self):
        pass
    
    def execute(self):
        print("Game Over")

class Game:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.execute()


from pyray import *
from raylib import *

init_window(800, 600, "Strategy")
set_target_fps(30)

strategy_start = Strategy_Start()
strategy_run = Strategy_Run()
strategy_game_over = Strategy_GameOver()

my_game = Game(strategy_start)

while window_should_close() is False:
        

    begin_drawing()
    clear_background(WHITE)
    my_game.execute()
    end_drawing()

close_window()

my_game.set_strategy(strategy_run)
my_game.execute()

my_game.set_strategy(strategy_game_over)
my_game.execute()



