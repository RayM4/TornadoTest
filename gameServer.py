from tornado.web import Application, RequestHandler, url, HTTPError

from game.SessionController import SessionController

__Game_Session__ = SessionController()

# hit server root
class RootHandler(RequestHandler):
    def get(self):
        self.write("Connected to Game Server")


class GameCreateHandler(RequestHandler):
    def get(self, user_id):
        __Game_Session__.add_user(user_id)


def make_game_server():
    return Application([
        url(r"/", RootHandler),
        url(r"/createGame/([0-9]+)", GameCreateHandler)
    ])
