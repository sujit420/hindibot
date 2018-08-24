import os,sys
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import BotServiceConfig as env

curr_dir_path = os.path.dirname(os.path.abspath(__file__))

def train():
    try:
        print "training chatterBot for smallTalk"
        if os.path.isfile(os.path.join(curr_dir_path,'../../', 'database.db')):
            os.remove(os.path.join(curr_dir_path,'../../', 'database.db'))
        bot = ChatBot(
            "chatBotGeneral",
            storage_adapter="chatterbot.adapters.storage.JsonFileStorageAdapter",
            input_adapter="chatterbot.adapters.input.VariableInputTypeAdapter",
            output_adapter="chatterbot.adapters.output.OutputFormatAdapter",
            tie_breaking_method="random_response",
            logic_adapters=[
                "chatterbot.adapters.logic.ClosestMatchAdapter"]
        )
        bot.set_trainer(ChatterBotCorpusTrainer)
        bot.train(env.smalltalk_dir)

        return True
    except Exception as err:
        print err
        return False

if __name__ == '__main__':
    train()


