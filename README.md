# Document Classification

We build a document classifier web service in which a document is uploaded and is classified using naive bayes classifier.  

## Dataset
We used 20news_group dataset for our classification.

[20 newsgroup dataset](http://qwone.com/~jason/20Newsgroups/)

## Workflow

1. Dataset was combined  into one file.
1. Stopwords were removed.
1. Lemmatization was performed on the datasets.
1. Probabilies of each word against each cataegory was calculated and stored in the database.
1. Classification was performed based on the probabilities(**naive bayes theorem**) 


### Results

Bag of Words 
![](https://github.com/Gitesh-Narula/naive-bayes-classifier-/blob/master/Results/Bag%20of%20words.png)


Probabilities of each word was calculated
![](https://github.com/Gitesh-Narula/naive-bayes-classifier-/blob/master/Results/Probabilites.png)


Website and Document Upload
![](https://github.com/Gitesh-Narula/naive-bayes-classifier-/blob/master/Results/Website.png)


Classification
![](https://github.com/Gitesh-Narula/naive-bayes-classifier-/blob/master/Results/Classification.png?raw=true)
