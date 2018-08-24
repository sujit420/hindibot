import os
import tornado.web
from tornado import gen
from logger import *
import traceback
from prediction.ner.predict import predict_tags
from prediction.intent_classifier.predict import predict_classifier
from prediction.smalltalk.getResponse import get_response
from wxconv import WXC

cur_dir = os.path.dirname(os.path.abspath(__file__))
con = WXC(order='utf2wx')
con1 = WXC(order='wx2utf', lang='hin')
@gen.coroutine
def process(data):
    print(data)
    module = data['module']
    input_string = data['data']['queries'][0]
    transformed_query = con.convert(unicode(input_string))
    try:
        if(module == 'ner'):
            output = yield predict_tags(input_string)
        if(module == 'all'):
            output1 = yield predict_classifier(transformed_query)
            if output1 == 'cab_book':
                output = yield predict_tags(input_string)
            else:
                output = yield get_response(transformed_query)
                output = con1.convert(output)
        if(module == 'smalltalk'):
            output = yield get_response(transformed_query)
            output = con1.convert(output)
        if(module == 'intent'):
            output = yield predict_classifier(transformed_query)
    except Exception as error:
        traceback.print_exc()
        log_traceback()
        raise tornado.web.HTTPError(500)

    raise gen.Return(output)
