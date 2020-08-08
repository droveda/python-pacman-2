class GameState:
    RUNNING = 0
    PAUSED_USER = 1
    GAME_OVER = 2
    FINISH = 3
    PAUSED = 4

    def __init__(self):
        self.__current_state = GameState.PAUSED

    def get_current_state(self):
        return self.__current_state

    def set_current_state(self, value):
        self.__current_state = value

    def is_game_running(self):
        return self.__current_state == GameState.RUNNING

    def is_paused_by_user(self):
        return self.__current_state == GameState.PAUSED_USER

    def is_game_over(self):
        return self.__current_state == GameState.GAME_OVER

    def is_paused(self):
        return self.__current_state == GameState.PAUSED

    def is_finished(self):
        return self.__current_state == GameState.FINISH
