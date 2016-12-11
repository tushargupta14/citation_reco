# Creates GN 

# Input : d1 (nlp_abstract_title_tfidf.pkl)
# Output List of top N papers simmilar on the basis of abstract and title concatenated 

#File for creating a candidate dataset . The input is  a local context c* on the basis of which context aware methods LCN and LN are implemented .

import sys 
import cPickle as cp 
from collections import Counter 
import vector_cal_for_new_queries as vc  
#from getvector import get_vector
from comp_similarity import comp_similarity

def GN(c_query,abs_tit_context_dict,abs_tit_cit_dict,N,feature_idf,tfidf_dict):
        #edge = []
        #for key,value in abs_tit_context_dict.iteritems():
        #        if c_query == value :
        #                c_counter = key     ## counter of the query 

        #edge = abs_tit_cit_dict[c_counter]
        #print(edge)
        score_dict={}
	
	#these two need to be given as input
	#feature_idf = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/idf_values_for_feature_words.pkl"))
	#tfidf_dict = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/nlp_abstract_title_tfidf.pkl","rw+"))
	
	c_query_vec = vc.query_vector(c_query,feature_idf)
        score_dict = {key:comp_similarity(tfidf_dict[key],c_query_vec) for key in abs_tit_context_dict}
	
	#print score_dict
#	for key,value in abs_tit_context_dict.iteritems():
#		value_vec = tfidf_dict[key]
		#print "context vector obtained"
		#c_query_vec = vc.query_vector(c_query,feature_idf)
		#c_query_vec = tfidf_dict[2]
		#print c_query_vec
 #               score = comp_similarity(value_vec,c_query_vec)
		#print "Similarity obtained" 
  #              score_key = abs_tit_cit_dict[key]
   #             score_dict[score_key] = score
		#print score

	candidate_score_list = sorted(score_dict,key=score_dict.get,reverse=True)[:N]

       # cnt = Counter(score_dict)
       # candidate_score_list = cnt.most_common(N)
#	print candidate_score_list
	
        # List to store all the elements for LN 
        GN = []
    
	GN=[abs_tit_cit_dict[key] for key in candidate_score_list]

	################### this is a test module ###########################################3
#	print 'GN called'
#	nlp_docu = cp.load(open('/home/du3/13CS30045/citation_reco/dataset/natural_language_and_speech_paper_list.pkl','rw'))
#	for docs in GN: 
#		if docs not in nlp_docu:
#			print 'in GN:'
#			print(docs)
	
     #   for item in candidate_score_list:
      #          d = item[0]
       #         GN.append(d)
                #LCN.append(d1)
                #LCN.append(d2)
	return GN


#if __name__== "__main__":
#        edge1 = []
#        N =100
#        abs_tit_context_dict =cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/abstract_title_dictionary_nlp.pkl","rb+"))
#        abs_tit_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/abstract_title_id_to_doc_map.pkl","rb+"))
#        c_query = abs_tit_context_dict[2]
#        edge1 = abs_tit_cit_dict[1]
#        print("from the main",edge1)
#        GN(c_query,abs_tit_context_dict,abs_tit_cit_dict,N)









