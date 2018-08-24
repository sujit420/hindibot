# coding=utf-8
from sklearn.svm import SVC
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import numpy,pickle
from sklearn.feature_extraction.text import TfidfVectorizer
import BotServiceConfig as env
from logger import *
from sklearn import preprocessing

def train_evaluate():

    df = pd.read_csv(env.intentR_file)
    print(df)
    df = shuffle(df)

    X_train, X_test, y_train, y_test = train_test_split(df[env.columnA], df[env.columnB], test_size=0.1)

    le = preprocessing.LabelEncoder()
    labels = le.fit_transform(y_train)

    vect = TfidfVectorizer(min_df=5).fit(X_train)

    X_train_vectorized = vect.transform(X_train)

    # embeddings_index = {}
    # for i, line in enumerate(open('/Users/sujitmishra/Downloads/hindi_word2Vec_small_roman.text')):
    #     values = line.split()
    #     embeddings_index[values[0]] = numpy.asarray(values[1:], dtype='float32')
    #
    # # create a tokenizer
    # token = text.Tokenizer()
    # token.fit_on_texts(df['sentences'])
    # word_index = token.word_index
    #
    # # convert text to sequence of tokens and pad them to ensure equal length vectors
    # train_seq_x = sequence.pad_sequences(token.texts_to_sequences(X_train), maxlen=10)
    # # valid_seq_x = sequence.pad_sequences(token.texts_to_sequences(y_train), maxlen=10)
    #
    # # create token-embedding mapping
    # embedding_matrix = numpy.zeros((len(word_index) + 1, 50))
    # for word, i in word_index.items():
    #     embedding_vector = embeddings_index.get(word)
    #     if embedding_vector is not None:
    #         embedding_matrix[i] = embedding_vector

    svclassifier = SVC(kernel='linear')

    svclassifier.fit(X_train_vectorized, labels)
    logger.info('Model trained......')

    classifier = {'trainer':svclassifier,'transformer':vect,'encoder':le}
    pickle.dump(classifier,open(env.intent_model_path, 'wb'))

    logger.info('Model saved......')
    y_pred = svclassifier.predict(vect.transform(X_test))
    olabels = le.inverse_transform(y_pred)
    print(olabels)

    print(confusion_matrix(y_test,olabels))
    print(classification_report(y_test,olabels))

if __name__ == '__main__':
    train_evaluate()
    loaded_model = pickle.load(open(env.intent_model_path, 'rb'))

    print('model loaded....')

    test = 'mEM jEsalamera havAI adde para jAnA cAhUMgA'
    trainer = loaded_model['trainer']
    transformer = loaded_model['transformer']
    le = loaded_model['encoder']
    print(le.inverse_transform(trainer.predict(transformer.transform([test]))))
