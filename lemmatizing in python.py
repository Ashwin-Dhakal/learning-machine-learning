
from nltk.stem import WordNetLemmatizer

lemmatizer= WordNetLemmatizer()

print(lemmatizer.lemmatize('better', pos="a"))

# this better is printed as good in the output since it is refected as the better option than s`temming