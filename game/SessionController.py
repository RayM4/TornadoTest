import queue

from game.GameSession import GameSession


class SessionController:
    def __init__(self):
        self.user_id_to_game_id_mapping = {}
        self.active_games = {}
        self.pending_games = queue.Queue()
        # TODO: using game count for game id, replace with different id later
        self.game_count = 0

    def add_user(self, user_id):
        if self.pending_games.empty():
            new_game = GameSession(game_id=self.game_count, player1_id=user_id)
            self.user_id_to_game_id_mapping[user_id] = self.game_count
            self.pending_games.put(new_game)
            # TODO: REMOVE DEBUG MESSAGES
            print("game:" + str(self.game_count) + " added to queue")
            print("player id: " + str(user_id))
            self.game_count += 1
        else:
            current_game = self.pending_games.get()
            game_id = current_game.get_game_id()
            self.user_id_to_game_id_mapping[user_id] = game_id
            self.active_games[game_id] = current_game
            # TODO: REMOVE DEBUG MESSAGES
            print("game:" + str(game_id) + " started")
            print("player id: " + str(user_id))
