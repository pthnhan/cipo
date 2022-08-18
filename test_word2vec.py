from nltk.test.gensim_fixt import setup_module
setup_module()
import gensim
from nltk.corpus import brown
train_set = brown.sents()[:10000]
model = gensim.models.Word2Vec(train_set)
model.save('brown.embedding')
new_model = gensim.models.Word2Vec.load('brown.embedding')