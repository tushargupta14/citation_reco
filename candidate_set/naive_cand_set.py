# file generetaes candidates set for a given query by splitting it into words and generating a set of documents where the word occured 
# Input : Inverted index of all the unqiue words in the corpus except the stop words, a query 
# Output : A candidate set and a ranking dictionary keyed by the document  
import json 
import nltk 
def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        return clean_parag

def create_candidate_set(query,inverted_index_dict):
	
	query = clean_parag(query)

	rank_dict = {}
	candidate_set = set()
	for word in query.split(" "):
		word_doc_list = set()
		try :
			word_doc_list = inverted_index_dict[word][0]
			for doc in word_doc_list:
				if doc in rank_dict:
					rank_dict[doc]+=1
				else : 
					rank_dict[doc]=1
			candidate_set.add(word_doc_list)
		except Exception as e:
			continue
	#print candidate_set
	#print rank_dict

if __name__ == "__main__"
	
	
	create_candidate_set(query,inverted_index_dict)
	
