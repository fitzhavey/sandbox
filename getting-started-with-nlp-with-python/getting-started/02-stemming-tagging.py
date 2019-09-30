import nltk

# stemming
text = 'Mary closed on closing night when she was in the mood to close.'
from nltk.stem.lancaster import LancasterStemmer
from nltk.tokenize import word_tokenize
stemmer = LancasterStemmer()
stemmedWords = [stemmer.stem(word) for word in word_tokenize(text)]
print ('stemmed words:')
print(stemmedWords)

# parts of speech tagging
partsOfSpeechTags = nltk.pos_tag(word_tokenize(text))
print('parts of speech tags:')
print(partsOfSpeechTags)