# coding=utf-8

from process_data import DataHandler
from NER_model import NER
import pickle
import BotServiceConfig as env
from logger import *


def train_evaluate():
    s = DataHandler(env.ner_file)
    logger.info(s.get_data()[0].shape)
    logger.info(s.tag_id_map)
    dic = {'maxlen': s.max_len , 'tag_id_map' : s.tag_id_map,'tags':s.tags}
    with open(env.ner_model2, 'wb') as output:
        pickle.dump(dic,output,pickle.HIGHEST_PROTOCOL)
    logger.info('pickle saved....')
    m = NER(s)
    m.make_and_compile()

    m.train(epochs=50)

    m.evaluate()

    print(m.predict_tags("संग्राम साबत के लिए रांची से पटना हवाई अड्डे तक एक कैब बुक करें"))

    m.model.save(env.ner_model1)

    logger.info('ner model saved....')

if __name__ == '__main__':
    train_evaluate()
