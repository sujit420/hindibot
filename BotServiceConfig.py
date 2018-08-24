import os

curr_dir_path = os.path.dirname(os.path.abspath(__file__))

# configs start below

#embedings path
ner_embed_path = os.path.join(curr_dir_path,'embeddings','hindi_word2Vec_small.w2v')

#intent file
intentR_file = os.path.join(curr_dir_path,'data','intent','hindi_intentR.tsv')
intent_file = os.path.join(curr_dir_path,'data','intent','hindi_intent.tsv')
intent_model = 'intent_classifier.pkl'
intent_model_path = os.path.join(curr_dir_path,'models','intent_model',intent_model)
columnA = 'sentences'
columnB = 'type'

#ner file
ner_file = os.path.join(curr_dir_path,'data','ner','hin_train.txt')
nerR_file = os.path.join(curr_dir_path,'data','ner','hin_trainR.txt')
ner_model1 = os.path.join(curr_dir_path,'models','ner_models','hindi_model')
ner_model2 = os.path.join(curr_dir_path,'models','ner_models','extra.pkl')

#smalltalk files
smalltalk_dir = os.path.join(curr_dir_path,'data','smalltalk','hindiR')
