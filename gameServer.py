from tornado.web import Application, RequestHandler, url, HTTPError
from tornado.escape import json_encode

from game.SessionController import SessionController

__Game_Session__ = SessionController()


# hit server root
class RootHandler(RequestHandler):
    def get(self):
        self.write("Connected to Game Server")


# handles the starting a game between two users
class GameCreateHandler(RequestHandler):
    def get(self, user_id):
        __Game_Session__.add_user(user_id)
        self.write("Adding User to Game")


# handle move
class GameMakeMoveHandler(RequestHandler):
    def get(self, user_id, loc_x, loc_y):
        game = __Game_Session__.get_game(user_id)
        game.make_move(user_id, loc_x, loc_y)
        self.write(json_encode(game.get_game_board().get_board()))


def make_game_server():
    return Application([
        url(r"/", RootHandler),
        url(r"/createGame/([0-9]+)", GameCreateHandler),
        url(r"/makeMove/([0-9]+)/([0-9]+)/([0-9]+)", GameMakeMoveHandler),
    ])
