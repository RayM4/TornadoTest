class GameBoard:
    __SIZE = 3

    def __init__(self, size=__SIZE):
        # TODO: make dynamic
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

    def make_move(self, value, pos_x, pos_y):
        if pos_x > __SIZE or pos_y > __SIZE:
            print("invalid index")
            return
        if self.board[pos_x][pos_y] < 1:
            self.board[pos_x][pos_y] = value
            # TODO: REMOVE DEBUG
            print("player " + str(value) + " made move on " + str(pos_x) + " " + str(pos_y))
        else:
            # TODO: handle invalid moves
            print("invalid move")
