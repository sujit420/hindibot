import BotServiceConfig as env
from logger import *
from keras.models import load_model
import os,pickle
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

curr_dir_path = os.path.dirname(os.path.abspath(__file__))
tagger1 = None
tagger2 = None
classifier = None
smalltalk = None
converter = None

def load_models():
    global tagger1
    tagger1 = load_model(env.ner_model1)

    global tagger2
    with open(env.ner_model2, 'r') as p:
        tagger2 = pickle.load(p)

    global classifier
    classifier = pickle.load(open(env.intent_model_path, 'rb'))

    global smalltalk
    try:
        print "training chatterBot for smallTalk"
        if os.path.isfile(os.path.join(curr_dir_path, '../../', 'database.db')):
            os.remove(os.path.join(curr_dir_path, '../../', 'database.db'))
        smalltalk = ChatBot(
            "chatBotGeneral",
            storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
            input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
            tie_breaking_method="random_response",
            logic_adapters=[
                "chatterbot.adapters.logic.ClosestMatchAdapter"],
            # read_only = True
        )
        smalltalk.set_trainer(ChatterBotCorpusTrainer)
        smalltalk.train(env.smalltalk_dir)
    except Exception as err:
        print err
        return False
    # smalltalk = ChatBot(
    #     "chatBotGeneral",
    #     storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
    #     input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
    #     output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
    #     tie_breaking_method="random_response",
    #     logic_adapters=[
    #         "chatterbot.adapters.logic.ClosestMatchAdapter"],
    #     read_only=True
    #)
    # if os.path.isfile(os.path.join(curr_dir_path,'../', 'database.db')):
    #     os.remove(os.path.join(curr_dir_path,'../', 'database.db'))
    # smalltalk = ChatBot(
    #     'Cab_Book_Bot',
    #     trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
    # )

    # smalltalk.train(env.smalltalk_dir)
    # print str(smalltalk.get_response("AkASagaMgA ke nikatawama pramuKa AkASagaMgA kA nAma kyA hE?"))
    print('all models loaded in memory....')


