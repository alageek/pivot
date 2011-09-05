import tornado
import tornado.web
from settings import Setting


class BaseHandler(tornado.web.RequestHandler):

    template_name = None

    @tornado.web.addslash
    def get(self, *args):
        context_data = self.get_context_data(*args)
        self.render('%s.html' % self.template_name, **context_data)

    def get_context_data(self, *args):
        context_data = {
            'version': tornado.version,
        }

        return context_data


class IndexHandler(BaseHandler):

    template_name = 'index'

    def __init__(self, *args, **kwargs):
        self.pivot = Setting()

        super(IndexHandler, self).__init__(*args, **kwargs)

    def get_context_data(self, *args):
        context_data = super(IndexHandler, self).get_context_data(*args)
        context_data.update({
            'candidate': self.pivot.candidate
        })

        return context_data
