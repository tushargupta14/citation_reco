#this is a module which requires the document representation and local context to calculate similarity score
#input:list of contexts for doc , local context c* (their vector representation) , send the tfidf dictionary (nlp_context_tfidf.pkl)
#output:similarity score according to the formula (1/k)*sigma(i=1->k)(bi*c)**2

import sys
sys.path.insert(0, '/home/du3/13CS30045/candidate_set')

import comp_similarity as cs
import vector_cal_for_new_queries as vq

def similarity_score(list_k,c_star,tfidf_dict,feature_idf,stopwords):
	score=0
	c_star_vec=vq.query_vector(c_star,feature_idf,stopwords)
	score_list = [(cs.comp_similarity(tfidf_dict[key],c_star_vec))**2 for key in list_k]
	score=reduce((lambda x,y: x+y),score_list)
	#for context in list_k:
	#	l_score=cs.comp_similarity(tfidf_dict[context],c_star_vec)
	#	score+=l_score**2
	score/=len(list_k)
	
	return score							 

