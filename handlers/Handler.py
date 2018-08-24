import tornado.web
from tornado import gen

import actions,os,uuid,time
from logger import *
import shutil
# import  logger
import BotServiceConfig as env
from common.load_models import *
from applicationLogger import ContextFilter
host = None
port = None

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
class BaseHandler(tornado.web.RequestHandler):

    def write_error(self, status_code, **kwargs):

        errorMessageMap = {
            400: "Required parameter is missing.",
            401: "Access denied due to invalid key. Make sure you are subscribed to an API you are trying to call and provide the right key.",
            403: "Out of call volume quota. Quota will be replenished in 2.12 days.",
            404: "Rate limit is exceeded. Try again in 26 seconds.",
            500: "Service not available. Please try again"
        }

        errorMessage = errorMessageMap.get(status_code, "Unknown Error")

        if(status_code in errorMessageMap.keys()):
            self.write(
                {"error": {"statusCode": status_code, "message":  errorMessage}})
        else:
            self.write('Unknown Error')


class ErrorHandler(tornado.web.ErrorHandler, BaseHandler):
    """
    Default handler gonna to be used in case of 404 error
    """
    pass


class MainHandler(BaseHandler):

    def get(self):
        self.render("index.html")


class ServiceHandler(BaseHandler):

    def initialize(self, *args, **kwargs):

        global host
        global port
        if not host and not port:
            val = self.request.host
            valArr = val.split(':')
            host = valArr[0]
            if len(valArr) > 1:
                port = valArr[1]

    @gen.coroutine
    def post(self, **params):

        if not (params['module'] and params['action']):
            logger.error("Check for the module and action Failed..")
            raise tornado.web.HTTPError(400)

        #module can be all(execute everything), ner(only ner), intent(only intent classification), smalltalk(only smalltalk answers)
        module = params['module']

        #action can be train and predict
        action = params['action']
        data = {}
        for key in self.request.arguments:
            data[key] = self.get_argument(key)
        data['module'] = module

        if (action == 'predict'):
            jsondata = tornado.escape.json_decode(self.request.body)
            data['data'] = jsondata
            res = yield actions.process(data)

        #training will be done offline
        if (res is not None):
            responseDict = {'data' : {'output' : None}}
            responseDict['data']['output'] = res #res if isinstance(res, dict) else res.split('\n')
            self.add_header('Content-Type', 'application/json')
            self.write(responseDict)
        else:
            self.write({})

class testHandler(BaseHandler):

    def initialize(self, *args, **kwargs):
        logger.debug(self.request.body)

    def get(self):
        self.write("testing page")
