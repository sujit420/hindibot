import gensim.models.word2vec as w2v
import numpy as np
import os
import BotServiceConfig as env

trained_model = w2v.Word2Vec.load(env.ner_embed_path)

def get_sentence_vectors(sentence):
	"""
	Returns word vectors for complete sentence as a python list"""
	s = sentence.strip().split()
	vec = [ get_word_vector(word) for word in s ]
	return vec

def get_word_vector(word):
	"""
	Returns word vectors for a single word as a python list"""
	s = word.decode("utf-8")
	try:
		vect = trained_model.wv[s]
	except:
		vect = np.zeros(50, dtype = np.float32)
	return vect

	