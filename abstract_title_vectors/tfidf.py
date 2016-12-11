#this file creates tfidf vectors for abstract_title 
#Input : abstract_title_corpus_dump.txt , abstract_title list (abstract_title_dictionary_nlp.pkl) for which tfidf is to be calculated
#Output : abstract_title dictionary with key as abstract_title id and value as tfidf vector and norm and length stored as a list


import numpy as np
import cPickle as pickle
import math
from numpy import linalg as lg


def idf_vocab_creator():
	print 'creating vocab for idf'
	file=open('abstract_title_corpus_dump.txt','rw')
	lines=file.readlines()
	#vocab={}
	idf={}
	counter=1
	for line in lines:
		print(str(counter)+'/'+str(len(lines)))
		counter+=1
		line_word_vocab={}
		for word in line.split(' '):
			#if word in vocab:
			#	vocab[word]+=1
			#else:
			#	vocab[word]=1
			if word not in line_word_vocab:
				line_word_vocab[word]='present'
		for word in line_word_vocab:
			if word in idf:
				idf[word]+=1
			else:
				idf[word]=1
	pickle.dump(idf,open('tfidf_vocab_with_idf_stats.pkl','w+'))
	return idf,len(lines)

def create_feature_list(idf,number_of_docs):
	#features=sorted(idf,key=idf.get)[1:number_of_features]
	print 'creating feature list'
	feature_idf={}
	word_id_map={}
	counter=-1
	for words in idf:
		if idf[words] > 5:
			counter+=1
			word_id_map[words]=counter
			feature_idf[words] = math.log((1+number_of_docs)/(1+idf[words]))+1
	pickle.dump(feature_idf,open('idf_values_for_feature_words.pkl','w+'))
	pickle.dump(word_id_map,open('feature_word_to_id_map.pkl','w+'))
	return feature_idf,counter,word_id_map
	
def create_tfidf_for_context(context,feature_idf,number_of_features,word_id_map):
	#a=np.zeros(number_of_features)
	context_word_list={}
	output_word_list={}
	for words in context.split(' '):
		if words not in context_word_list:
			context_word_list[words]=1
		else:
			context_word_list[words]+=1
	for words in context_word_list:
		if words in feature_idf:
			output_word_list[words]=feature_idf[words]*context_word_list[words]
	
	return output_word_list

def norm_cal(a):
	sum=0
	for words in a:
		sum+=a[words]**2
	sum=sum**(0.5)
	return sum	


def tfidf_dictionary_creator():
	contexts=pickle.load(open('abstract_title_dictionary_nlp.pkl','rw'))
	idf,number_of_docs = idf_vocab_creator()
	#already created the idf vocab in previous runs
	
	#idf=pickle.load(open('tfidf_vocab_with_idf_stats.pkl','rw'))
	#number_of_docs=26037781
	
	#output
	tfidf={}
	
	feature_idf,counter,word_id_map=create_feature_list(idf,number_of_docs)
	con_count=1
	
	for context in contexts:
		print(str(con_count)+'/'+str(len(contexts)))
		con_count+=1
		a = create_tfidf_for_context(contexts[context],feature_idf,counter,word_id_map)
		norms=norm_cal(a)	
		tfidf[context]=[a,norms,len(a)]		
			 
	#file_name='nlp_abstract_title_tfidf_'+str(int((end-start)/117823))+'.pkl'
	pickle.dump(tfidf,open('nlp_abstract_title_tfidf.pkl','w+'))




if __name__ == '__main__':
	tfidf_dictionary_creator()
	
