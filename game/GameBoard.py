class GameBoard:

    def __init__(self, size=3):
        # TODO: make dynamic
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def make_move(self, value, pos_x, pos_y):
        if pos_x > 3 or pos_y > 3:
            print("invalid index")
            return
        if self.board[pos_x][pos_y] < 1:
            self.board[pos_x][pos_y] = value
            # TODO: REMOVE DEBUG
            print("player " + str(value) + " made move on " + str(pos_x) + " " + str(pos_y))
        else:
            # TODO: handle invalid moves
            print("invalid move")

    def get_board(self):
        return self.board
