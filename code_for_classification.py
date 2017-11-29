from sys import argv
from math import log
import pymysql

cursor = ""
class_prob={}
prob={}

def global_variables():
	global class_prob
	global prob
	global cursor
	db = pymysql.connect("localhost","root","root","naive" )
	cursor = db.cursor()
	sql = "select * from probability_class"
	cursor.execute(sql)
	resultSet=cursor.fetchall()
	for row in resultSet:
		class_prob[row[0]]=row[1]

	# print('How many times will there statments over execute ? ................... test #26')

	sql = "select * from probability_word_given_class"
	cursor.execute(sql)
	resultSet=cursor.fetchall()
	for row in resultSet:
		if row[1] not in prob:
			prob[row[1]]={}
		prob[row[1]][row[0]]=row[2]

	db.close()


def read_words(words_file):
    return [word for line in open(words_file, 'r') for word in line.split()]


def findClass(target):
	global_variables()
	# target = read_words(target)
	max_prob = float("-inf")
	max_class = ""
	for _class in class_prob:
		_prob = log(class_prob[_class])
		for _word in target:
			if _word in prob:
				_prob += log(prob[_word][_class])
		if _prob>max_prob:
			max_prob = _prob
			max_class = _class

	return max_class

if __name__=="__main__":
	# script,filename = argv
	filename="test_input.txt"
	text = read_words(filename)
	global_variables()
	print(findClass(text))