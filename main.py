from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url, asynchronous, HTTPError, RedirectHandler
from tornado.httpclient import AsyncHTTPClient
from tornado.escape import json_decode, json_encode
from tornado.gen import coroutine

from gameServer import make_game_server

__ITEM__ = [
    "someItem1",
    "Item 2",
    "The 3rd item",
    "4th Item"
]

__PORT_NUMBER = 9000


# basic handler
class MainHandler(RequestHandler):
    def get(self):
        self.write("hello world")
        self.write("<br>")
        self.write("testing")


# html template example
class ItemListHandler(RequestHandler):
    def get(self):
        self.render("templates/basic_item_list.html", title="Item List", items=__ITEM__)


# json handler
class ItemJsonHandler(RequestHandler):
    def get(self):
        self.write(json_encode(__ITEM__))


# handler with parameters
class StoryHandler(RequestHandler):
    def get(self, story_id):
        self.write("This is page is url %s" % story_id)


class MultipleStoryHandler(RequestHandler):
    def get(self, story_id, content_id):
        self.write("This is page is url %s" % story_id)
        self.write("<br>")
        self.write("content of page %s " % content_id)


# handler that can receive post data
class MyFormHandler(RequestHandler):
    def get(self):
        self.render("templates/form.html")

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


# call an api and print the response text
class AsyncHandler(RequestHandler):
    @asynchronous
    def get(self):
        http = AsyncHTTPClient()
        http.fetch("some api url",
                   callback=self.on_response)

    def on_response(self, response):
        if response.error: raise HTTPError(500)
        json = json_decode(response.body)
        self.write(json)


# co-routine version
class CoroHandler(RequestHandler):
    @coroutine
    def get(self):
        http = AsyncHTTPClient()
        response = yield http.fetch("some api url")
        json = json_decode(response.body)
        self.write(json)


# url pattern mapping
def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r"/items", ItemListHandler),
        url(r"/items_api", ItemJsonHandler),
        url(r"/story/([0-9]+)", StoryHandler, name="story"),
        url(r"/m_story/([0-9]+)/([0-9]+)", MultipleStoryHandler),
        url(r"/myform", MyFormHandler),
        # example of a redirect
        url(r"/app", RedirectHandler, dict(url="/"))
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)

    gameServer = make_game_server()
    gameServer.listen(__PORT_NUMBER)
    print("Starting server in port:" + str(__PORT_NUMBER))

    IOLoop.current().start()
