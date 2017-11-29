from nltk import word_tokenize  #punctuation not accurate
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import string
from sys import argv

def prelim(filename):
	### Initialize tokenizer, stopset, stemmer and lemmatizer ###
	tokenizer = RegexpTokenizer(r'\w+')  #used this because this regex gets rid of punctuations al well....alternativly word_tokenize could also have been used
	stopset = set(stopwords.words('english'))
	#porter_stemmer=PorterStemmer()
	lemm = WordNetLemmatizer()
	#stemmer = SnowballStemmer('english')
	##################################################
	text=open(filename, 'r').read()
	text=unicode(text, errors='replace')

	tokens = tokenizer.tokenize(text) #tokenize the text

	tokens = list(set(tokens))   ##doubt about this in the algorithm

	# tokens = [porter_stemmer.stem(w) for w in tokens if not w in stopset] #stem the tokens and remove stop words

	tokens = [lemm.lemmatize(w,'v') for w in tokens]

	# tokens = [porter_stemmer.stem(w) for w in tokens if not w in stopset]
	# tokens = [lemm.lemmatize(w) for w in tokens if not w in stopset]

	import code_for_classification
	return code_for_classification.findClass(tokens)


if __name__=='__main__':
	# import code_for_classification
	# sys,argv=argv #filename to be classified in the command line
	text = open('test.txt','r').read()
	# text=text.encode('utf-8')
	tokens = prelim(text)
	print(tokens)
	# print(code_for_classification.findClass(tokens))
