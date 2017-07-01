from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, url


class MainHandler(RequestHandler):
    def get(self):
        self.write("hello world")
        self.write("<br>")
        self.write("testing")


class StoryHandler(RequestHandler):
    def get(self, story_id):
        self.write("This is page is url %s" % story_id)


class MyFormHandler(RequestHandler):
    def get(self):
        self.write('<html><body><form action="/myform" method="POST">'
                   '<input type="text" name="message">'
                   '<input type="submit" value="Submit">'
                   '</form></body></html>')

    def post(self):
        self.set_header("Content-Type", "text/plain")
        self.write("You wrote " + self.get_body_argument("message"))


def make_app():
    return Application([
        url(r"/", MainHandler),
        url(r"/story/([0-9]+)", StoryHandler, name="story"),
        url(r"/myform", MyFormHandler)
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()