# File carries out query expansion Input : a query ; Need to define the wordnet class in the main function 
# Output : set of alternative words for the query including the query words itself 


import time
from nltk.corpus import wordnet    
class MyWordNet:
    def __init__(self, wn):
        self._wordnet = wn

    def synsets(self, word, pos=None):
        return self._wordnet.synsets(word, pos=pos)


def find_synonyms(word_list,wn):
 
	alternative_words = []
	
	for word in word_list :
		hypernyms = []
		synonyms = []
		hypernyms = [lemma.name() for synset in wn.synsets(word) for val in synset.hypernyms() for lemma in val.lemmas()]
	 
		#hypernyms.append(lemma.name() for synsets in wn.synsets(word) for lemma in synsets.lemmas())
		
		synonyms  = [lemma.name() for synsets in wn.synsets(word) for lemma in synsets.lemmas()]
		

		synonyms = synonyms+hypernyms 
		#print hypernyms 
		alternative_words+= synonyms 
		alternative_words.append(word)
		
	#print alternative_words 
	
	return set(alternative_words)

def expand_query(query,wn,stop_word_dict=None):

	# Returns a set of alternative words for a query  
	
	query_list = []
	stop_word_dict = []
	query_list = [word.rstrip() for word in query.split(" ") if word not in stop_word_dict]
	
	return find_synonyms(query_list,wn)
	


if __name__ == "__main__" :
	
	start = time.time()
	wn = MyWordNet(wordnet)
	time1 = time.time()-start
	print time1 

	
	print expand_query("computation education general\n",wn)
	#find_synonyms("program",wn)
	
	time2 = time.time() - start 
	print time2
	a =  expand_query(" mathematics calculation sets\n",wn)
	print time.time() - start 
	#find_synonyms("calculation",wn)
	#time3 = time.time()  - time2 
	#print time3 
	
