
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))

example_sentence = "this is the yummy buff momo that we are eating this evening"

sample =[]

for w in word_tokenize(example_sentence):
    if w not in stop_words:
        sample.append(w)

print(sample)