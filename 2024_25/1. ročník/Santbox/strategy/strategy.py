
class Game_StrategyStart:
    def __init__(self):
        pass
    
    def execute(self):
        draw_text("Wait for key press", 300, 300, 20, BLACK)
    

class Game_StrategyRun:
    def __init__(self):
        pass

    def execute(self):
        draw_text("Game is running", 300, 300, 20, GREEN)


class Game_StrategyGameOver:
    def __init__(self):
        pass

    def execute(self):
        draw_text("Game Over", 300, 300, 20, RED)



# třída která obsahuje popis herní logiky
class Game:
    def __init__(self, strategy):
        self.strategy = strategy
        self.game_state = 0

    def set_strategy(self, strategy):
        self.strategy = strategy

    def execute(self):
        self.strategy.execute()


from pyray import *
from raylib import *

# inicializace okna
set_config_flags(FLAG_VSYNC_HINT)
init_window(800, 600, "Strategy")
set_target_fps(144)

strategy_start = Game_StrategyStart()
strategy_run = Game_StrategyRun()
strategy_game_over = Game_StrategyGameOver()

# vytvoření objektu hry
my_game = Game(strategy_start)

while window_should_close() is False:
    if is_key_pressed(KEY_ENTER):
        my_game.game_state = (my_game.game_state + 1) % 3

        if my_game.game_state == 0:
            my_game.set_strategy(strategy_start)
        elif my_game.game_state == 1:
            my_game.set_strategy(strategy_run)
        elif my_game.game_state == 2:
            my_game.set_strategy(strategy_game_over)

    begin_drawing()
    clear_background(WHITE)
    my_game.execute()
    end_drawing()

close_window()

