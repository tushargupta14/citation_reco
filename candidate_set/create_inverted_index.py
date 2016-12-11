# File creates inverted index for words present in the corpus 
# Input : takes input your nlp corpus dictionary , idf dictionary with all unique words
#Output : A dictionary with key as a word and set of documents in which it is present as list with the idf values

import cPickle as cp
from nltk.corpus import stopwords
import json 

def get_citer_doc(c_id,nlp_cit_dict):
	return nlp_cit_dict[c_id][1]
	

def create_inverted_index(idf_dict,nlp_context_dict,nlp_cit_dict):

	stop_words = set(stopwords.words("english"))
	# running over all the words in the idf dictionary
	inverted_index = {}
	word_count =0 
	for word,value in idf_dict.iteritems():
		doc_list = set() 
		n_docs = 0
		if word.lower in stop_words:
			continue
		for k,v in nlp_context_dict.iteritems():
			if word in v :
				doc_list.add(get_citer_doc(k,nlp_cit_dict))
				n_docs+=1

		inverted_index[word] = list(doc_list),n_docs
		word_count+=1
		if word_count%100 == 0:
			print word_count

	print "Dumping to json"	
	with open("nlp_inverted_index.json","wb+") as f:
		json.dump(inverted_index,f)
	print "Dumping to pickle file "
	with open("nlp_inverted_index.pkl","wb+") as f:
		cp.dump(inverted_index,f) 
		 		
			
if __name__ == "__main__" :

	 idf_dict = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/tfidf_vocab_with_idf_stats.pkl","rb"))
	 nlp_context_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_dictionary_nlp.pkl","rb+"))
	 nlp_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_to_doc_map.pkl","rb+"))
	 #n_docs : number of total documents 
	 print "loaded dicts"	
	 create_inverted_index(idf_dict,nlp_context_dict,nlp_cit_dict)
	 	
