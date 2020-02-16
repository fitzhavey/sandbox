import nltk;

# tokenising the text
from nltk.tokenize import word_tokenize, sent_tokenize as sentence_tokenize
text = "Mary had a little lamb. Her fleece was white as snow"
sentences = sentence_tokenize(text)
words = [word_tokenize(sentence) for sentence in sentences] # seemingly this is not used below
print('words:')
print(words)

# remove stop words
from nltk.corpus import stopwords
from string import punctuation
customStopWords = customStopWords = set(stopwords.words('english') + list(punctuation))

# remove stop words from the text
wordsWithoutStopWords = [word for word in word_tokenize(text) if word not in customStopWords]
print('words without stop words')
print(wordsWithoutStopWords)

# find bigrams
from nltk.collocations import *
bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(wordsWithoutStopWords)
sortedWords = sorted(finder.ngram_fd.items())
print('sorted words')
print(sortedWords)