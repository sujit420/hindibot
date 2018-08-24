import BotServiceConfig as env
import common.load_models as models
from tornado import gen
import traceback

@gen.coroutine
def get_response(input_query):
    try:
        output = models.smalltalk.get_response(input_query)
    except :
        output = 'getting response from smalltalk failed....'
        traceback.print_exc()

    raise gen.Return(str(output))