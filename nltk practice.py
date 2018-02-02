from nltk.tokenize import sent_tokenize, word_tokenize

example_sentense= "Hey MFCS! What are you doing this days. Its better to fuck a bitch rather than hanging at other girls."

for i in sent_tokenize(example_sentense):
    print(i)

print('this is the next line to be priented \n')
for j in word_tokenize(example_sentense):
    print(j)