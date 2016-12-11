#this code takes in context and returns a list of candidate papers, this is implemented for only local context yet global context needs changes
#input: c_star(in text), n1,n2=>number of candidates for LCN and GN respectively , feature_idf_abstract_title , feature_idf_context 
# tfidf_abstract,tfidf_context
#output: a list of candidates

import cPickle as cp
import create_LCN as cl
import create_GN as cg
import itertools

def candidate_set(c_star,n1,n2,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context):
	candidate_list=[]
	
	#nlp_context_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_dictionary_nlp.pkl","rb+"))
	#nlp_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_to_doc_map.pkl","rb+")) 
	
	#abs_tit_context_dict =cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/abstract_title_dictionary_nlp.pkl","rb+"))
	#abs_tit_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/abstract_title_id_to_doc_map.pkl","rb+"))

	temp1=cg.GN(c_star,abs_tit_context_dict,abs_tit_cit_dict,n2,feature_idf_abstract_title,tfidf_abstract)
	temp2=cl.LCN(c_star,nlp_context_dict,nlp_cit_dict,n1,feature_idf_context,tfidf_context)
	candidate_list.append(temp1)
	candidate_list.append(temp2)
	#for x in temp:
	#	candidate_list.append(x)
	
	candidate_list = list(itertools.chain.from_iterable(candidate_list))
	
	####################### this is a test module *****************************
	#return temp2

	return candidate_list	 
