# disambiguating word meanings
from nltk.corpus import wordnet
print('definitions of "bass":')
for synset in wordnet.synsets('bass'):
	print(synset, synset.definition())

# getting definition from context
from nltk.tokenize import word_tokenize
from nltk.wsd import lesk
## context 1
text1 = 'Sing in a lower tone, along with the bass'
interpretation1 = lesk(word_tokenize(text1), 'bass')
print('interpretation of "bass" in the following sentence. "' + text1 + '"')
print(interpretation1)
### context 2
text2 = 'This sea bass was really hard to catch'
interpretation2 = lesk(word_tokenize(text2), 'bass')
print('interpretation of "bass" in the following sentence. "' + text2 + '"')
print(interpretation2)