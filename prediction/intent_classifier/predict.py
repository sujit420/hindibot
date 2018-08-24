#coding=utf-8
import common.load_models as models
from tornado import gen

@gen.coroutine
def predict_classifier(sentence):
    trainer = models.classifier['trainer']
    transformer = models.classifier['transformer']
    le = models.classifier['encoder']
    print(le.inverse_transform(trainer.predict(transformer.transform([sentence]))))
    result = le.inverse_transform(trainer.predict(transformer.transform([sentence])))
    raise gen.Return(result[0])

if __name__ == '__main__':
    test = 'mEM jEsalamera havAI adde para jAnA cAhUMgA'
    predict_classifier(test)