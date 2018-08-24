# coding=utf-8
from keras.models import load_model
from training.ner.get_word_vectors import get_word_vector,get_sentence_vectors
from keras.preprocessing import sequence
import numpy as np,pickle
import BotServiceConfig as env
from tornado import gen
import common.load_models as models
from wxconv import WXC

con = WXC(order='wx2utf', lang='hin')

@gen.coroutine
def predict_tags(sentence):
    sentence = str(sentence.encode('utf-8','ignore'))
    sentence_list = sentence.strip().split()
    sent_len = len(sentence_list)
    # Get padded word vectors
    x = encode_sentence(sentence)
    tags = models.tagger1.predict(x, batch_size=1)[0]

    tags = tags[-sent_len:]
    pred_tags = decode_result(tags)
    entityList = []
    for i in xrange(len(pred_tags)):
        en = {}
        if 'B-' in pred_tags[i]:
            en[pred_tags[i][2:]] = None
            st = sentence_list[i]
            j = i + 1
            for k in range(j, len(pred_tags)):
                if 'I-' in pred_tags[k]:
                    st = st + ' '+ sentence_list[k]
                else:
                    break
            en[pred_tags[i][2:]] = st
        if len(en.keys()) > 0:
            entityList.append(en)
    raise gen.Return(entityList)


def encode_sentence(sentence):
    vectors = get_sentence_vectors(sentence)
    vectors = [v[:50] for v in vectors]
    return sequence.pad_sequences([vectors], maxlen=models.tagger2['maxlen'], dtype=np.float32)

def decode_result(result_sequence):
    pred_named_tags = []
    for pred in result_sequence:
        _id = np.argmax(pred)
        pred_named_tags.append(models.tagger2['tag_id_map'][_id])
    return pred_named_tags

if __name__ == '__main__':
    sentence = u'मैं इंदिरानगर से यशवंतपुर रेलवे स्टेशन जाना चाहता हूं'
    predict_tags(sentence)
