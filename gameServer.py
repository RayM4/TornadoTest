from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop


# hit server root
class RootHandler(RequestHandler):
    def get(self):
        self.write("Connected to Game Server")


def make_game_server():
    return Application([
        url(r"/", RootHandler)
    ])
