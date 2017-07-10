

class GameSession:
    def __init__(self, game_id=-1, player1_id=-1, player2_id=-1):
        self.game_id = game_id
        self.player1 = player1_id
        self.player2 = player2_id

    def set_player_one(self, player_id):
        self.player1 = player_id

    def set_player_two(self, player_id):
        self.player2 = player_id

    def get_game_id(self):
        return self.game_id
