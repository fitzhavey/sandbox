# download the text
import urllib2
from bs4 import BeautifulSoup

def getWashingtonPostText(url):
	page = urllib2.urlopen(url).read().decode('utf8', 'ignore')
	soup = BeautifulSoup(page, 'lxml')
	rawText = ' '.join(map(lambda p: p.text, soup.find_all('article')))
	text = rawText.encode('ascii', errors='replace').replace('?', ' ')
	return text

articleURL = 'https://www.washingtonpost.com/news/the-switch/wp/2016/10/18/the-pentagons-massive-new-telescope-is-designed-to-track-space-junk-and-watch-out-for-killer-asteroids'

text = getWashingtonPostText(articleURL)
print('text:')
print(text)


# preprocess the text
from nltk.tokenize import sent_tokenize as sentence_tokenize, word_tokenize
from nltk.stem.lancaster import LancasterStemmer # stemming not included in original tutorial
from nltk.corpus import stopwords
from string import punctuation
stemmer = LancasterStemmer()

sentences = sentence_tokenize(text)
wordsIncludingStopwords = word_tokenize(text.lower())

wordsToRemove = set(stopwords.words('english') + list(punctuation))
unStemmedWords = [word for word in wordsIncludingStopwords if word not in wordsToRemove]
words = [stemmer.stem(word) for word in unStemmedWords]
print('sanitized words:')
print(words)

# extracting  a summary
from nltk.probability import FreqDist
frequency = FreqDist(words)
print('word frequency:')
print(frequency)

from heapq import nlargest
mostFrequentWords = nlargest(10, frequency, key=frequency.get)

from collections import defaultdict
ranking = defaultdict(int)
for i, sentence in enumerate(sentences):
	for word in word_tokenize(sentence.lower()):
		stemmedWord = stemmer.stem(word)
		if stemmedWord in frequency:
			ranking[i] += frequency[stemmedWord]

topSentenceIds = nlargest(4, ranking, key=ranking.get)
sortedTopSentences = [sentences[i] for i in sorted(topSentenceIds)]
print('summary:')
print(sortedTopSentences)