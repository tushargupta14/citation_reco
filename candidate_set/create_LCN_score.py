







#file for returnting a candidate dataset list with the scores  . The input is  a local context c* on the basis of which context aware methods LCN and LN are implemented .

import sys
import cPickle as cp
from collections import Counter
import vector_cal_for_new_queries as vc
#from getvector import get_vector
from comp_similarity import comp_similarity

def LCN(c_query,nlp_context_dict,nlp_cit_dict,N):

        score_dict={}
        feature_idf = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/idf_values_for_feature_words.pkl"))
        tfidf_dict = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/nlp_context_tfidf.pkl","rw+"))
        c_query_vec = vc.query_vector(c_query,feature_idf)
        for key,value in nlp_context_dict.iteritems():
                value_vec = tfidf_dict[key]
                #print "context vector obtained"
                #c_query_vec = vc.query_vector(c_query,feature_idf)
                #c_query_vec = tfidf_dict[2]
                #print c_query_vec
                score = comp_similarity(value_vec,c_query_vec)
                #print "Similarity obtained" 
                score_key = nlp_cit_dict[key]
                score_dict[score_key] = score
                #print score

        cnt = Counter(score_dict)
        candidate_score_list = cnt.most_common(N)
     	

        # List to store all the elements for LN 
        LN_score = []
        LCN_score = [] # List to store all the elements of LCN --> d1+d2
        for item in candidate_score_list:
               	d1 = item[0][0]
                d2 = item[0][1]
		score = item[1]
                #LN.append(d1)
                LCN_score.append((d1,score))
                LCN_score.append((d2,score))
        return LCN_score


