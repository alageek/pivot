import os
import tornado.web
import tornado.httpserver
import tornado.ioloop
from handlers import IndexHandler
from settings import Setting


class Application(tornado.web.Application):
    def __init__(self):
        pivot = Setting()
        pivot.check_settings_file()

        handlers = [
            (r'/', IndexHandler)
        ]

        settings = {
            'debug': pivot.setting('DEBUG'),
            'template_path': os.path.join(pivot.root, 'templates'),
            'static_path': os.path.join(pivot.root, 'static'),
            'candidate': pivot.candidate
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    httpserver = tornado.httpserver.HTTPServer(Application())
    httpserver.listen(8010)
    tornado.ioloop.IOLoop.instance().start()
