from nltk import word_tokenize  #punctuation not accurate
from nltk.tokenize import RegexpTokenizer
from nltk.stem import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from sys import argv
import os

fo=open("/home/akshat/Desktop/trainset.txt","w")

### Initialize tokenizer, stopset, stemmer and lemmatizer ###
tokenizer = RegexpTokenizer(r'\w+')  #used this because this regex gets rid of punctuations al well....alternativly word_tokenize could also have been used
stemmer = SnowballStemmer('english')
stopset = set(stopwords.words('english'))
lemm = WordNetLemmatizer()
##################################################

path="/home/akshat/Desktop/20news-18828"
for dirname in os.listdir(path):
	if os.path.isdir(path+"/"+dirname):
		print path+"/"+dirname
		for fname in os.listdir(path+"/"+dirname):
			print fname
            with open(path+"/"+dirname+"/"+fname, 'r') as f:
               	text = f.read()
                text= unicode(text, errors='replace')
                text=text.splitlines(True)
            text = " ".join(text[1:])
            tokens = tokenizer.tokenize(text) #tokenize the text
            tokens = list(set(tokens))   ##doubt about this in the algorithm
            tokens = [lemm.lemmatize(w) for w in tokens if not w in stopset] #stem the tokens and remove stop words
            fo.write(dirname+" "+" ".join(tokens)+"\n")
fo.close()


