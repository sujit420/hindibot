import argparse
import sys
import os
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define
from tornado.options import options
import BotServiceConfig as env
from handlers import Handler
from logger import *
from common.load_models import *

def loadApplication():
    return tornado.web.Application([
        (r"/test/?(.*)", tornado.web.StaticFileHandler,
         {"path": options.static, "default_filename": "index.html"}),
        (r"/(?P<module>[^\/]+)/(?P<action>[^\/]+)",
         Handler.ServiceHandler),
    ], debug=False)


def loadConfig():
    define("static", os.path.join(os.path.dirname(__file__), "test"))
    configPath = os.path.join(sys.path[0], "BotServiceConfig.py")
    tornado.options.parse_config_file(configPath)


def runServer(portNum):
    loadConfig()
    application = loadApplication()
    settings = {
        'default_handler_class': Handler.ErrorHandler,
        'default_handler_args': dict(status_code=404),
        "template_path": os.path.join(sys.path[0], "test")
    }
    server = tornado.httpserver.HTTPServer(application, settings)
    server.bind(portNum)  # port
    print 'server started at port ', portNum
    server.start(1)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('-port')
        args = parser.parse_args()
        portNum = args.port
        load_models()
        if portNum is None:
            # if port number is not present lets set the default to 9000
            portNum = '9000'
    except Exception, e:
        traceback.print_exc()

    runServer('8000')
