from game.GameBoard import GameBoard


class GameSession:
    def __init__(self, game_id=-1, player1_id=-1, player2_id=-1):
        self.game_id = game_id
        self.player1 = player1_id
        self.player2 = player2_id
        self.game_board = GameBoard()

    def set_player_one(self, player_id):
        self.player1 = player_id

    def set_player_two(self, player_id):
        self.player2 = player_id

    def get_game_id(self):
        return self.game_id

    def make_move(self, player_id, pos_x, pos_y):
        # TODO: Do something about the type safety...
        self.game_board.make_move(int(player_id), int(pos_x), int(pos_y))
