#this script takes in a local context and gives scores to the candidate set
#input:c_star,inlink dictionary (/home/du3/13CS30045/citation_reco/candidate_set/nlp_inlink_dictionary.pkl),tfidf_dictionary=/home/du3/13CS30045/citation_reco/
#citation_vectors/train/nlp_context_tfidf.pkl
#ouput:sorted dictionary of final recommendations

import sys
sys.path.insert(0, '/home/du3/13CS30045/citation_reco/candidate_set')
sys.path.insert(1, '/home/du3/13CS30045/citation_reco/candidate_set/novel_method')

import nov_candidate_set_generator as ncsg
import candidate_set_generator as csg
import local_similarity as ls
import cPickle as cp
import time
from nltk.corpus import stopwords

stopword = stopwords.words('english')

#this recommender function is for the novel method 

def recommender_novel(c_star,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,doc_idf,N,full_idf):
        #check for duplicacies in candidate_set
	#check for duplicacies in candidate_set

        #start_time = time.time()
        print 'generating candidate set'
        candidate_list=ncsg.naive_idf_candidate_set(full_idf,doc_idf,c_star,N)
        #print ("--- %s seconds ---" % (time.time()-start_time))

        #print 'loading inlinks'
        #inlinks=pickle.load(open('/home/du3/13CS30045/citation_reco/candidate_set/nlp_inlink_dictionary.pkl','rw'))

        final_reco_dict={}

        #print 'loading dependencies'
        #tfidf_dict = pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/nlp_context_tfidf.pkl','rw'))
        #citation_dictionary=pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/citation_dictionary.pkl','rw'))
        #feature_idf_context=pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/idf_values_for_feature_words.pkl','rw'))
        #counter = 0
        #start_time = time.time()
        print "ranking"

        ######## this is a test module ****************
        #nlp_docu = cp.load(open('/home/du3/13CS30045/citation_reco/dataset/natural_language_and_speech_paper_list.pkl','rw'))
        ###############################################

  #      for docs in candidate_list:
                #print (str(counter)+'/'+str(len(candidate_list)))
                #counter+=1
 #               if docs in inlinks:
                        #try:
#                        final_reco_dict[docs] = ls.similarity_score(inlinks[docs],c_star,tfidf_dict,feature_idf_context)
                        #except Exception as e:
                        #	if docs not in tfidf_dict:
                        #               print docs
                                #print e
			 #       continue
       		 #print ("--- %s seconds ---" % (time.time()-start_time))

	final_reco_dict={docs:ls.similarity_score(inlinks[docs],c_star,tfidf_dict,feature_idf_context,stopword) for docs in candidate_list}
       	return final_reco_dict



def recommender(c_star,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,
tfidf_dict):
	#check for duplicacies in candidate_set
	
	#start_time = time.time()
	print 'generating candidate set'
	candidate_list=csg.candidate_set(c_star,1000,1000,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context) #harcoded the values of n1 and n2 
	#print ("--- %s seconds ---" % (time.time()-start_time))
	
	#print 'loading inlinks'
	#inlinks=pickle.load(open('/home/du3/13CS30045/citation_reco/candidate_set/nlp_inlink_dictionary.pkl','rw'))

	final_reco_dict={}
	
	#print 'loading dependencies'	
	#tfidf_dict = pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/nlp_context_tfidf.pkl','rw'))
	#citation_dictionary=pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/citation_dictionary.pkl','rw'))
	#feature_idf_context=pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/idf_values_for_feature_words.pkl','rw'))
	#counter = 0
	#start_time = time.time()
	print "ranking"

	######## this is a test module ****************
	#nlp_docu = cp.load(open('/home/du3/13CS30045/citation_reco/dataset/natural_language_and_speech_paper_list.pkl','rw'))
	###############################################
	
	for docs in candidate_list:
		#print (str(counter)+'/'+str(len(candidate_list)))
		#counter+=1
		if docs in inlinks:
			#try:
			final_reco_dict[docs] = ls.similarity_score(inlinks[docs],c_star,tfidf_dict,feature_idf_context,stopword)
			#except Exception as e:
			#	if docs not in tfidf_dict:
			#		print docs
				#print e
			#	continue
	#print ("--- %s seconds ---" % (time.time()-start_time))
	return final_reco_dict

query_dict={}

def query_fire(doc_idf,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,full_idf):
	#this funtion fires n queries , stores their results as a dictionary of list with every list
	#containing top 10 recommendations indexed by the quereies ID
	
	final_query_list=[]
	contexts_to_test = cp.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/test/citation_dictionary_nlp.pkl','rw'))
	context_to_doc_map = cp.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/test/citation_to_doc_map.pkl','rw'))
	final_query_list=[key for key in context_to_doc_map if context_to_doc_map[key][0] in inlinks if len(inlinks[context_to_doc_map[key][0]]) > 5 if key not in query_dict][:1000]
	temp={key:'present' for key in final_query_list}
	query_dict.update(temp)

	if len(final_query_list)<900:
		print 'len of list'
		print(len(final_query_list))
	#except Exception as e:
	#	print e
	print ('time for 1000 queries')

	start_time = time.time()
	result_doc = {key : recommender(contexts_to_test[key],nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict) for key in final_query_list}
	#result_doc = {key : recommender_novel(contexts_to_test[key],nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
#,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,doc_idf,2000,full_idf) for key in final_query_list}
	#print("------------%s seconds -------" % (time.time()-start_time))
	
	#time to print 
	end_time=time.time()
	

	result_list={}

	counter = 0
	for x in result_doc:
		if context_to_doc_map[x][0] in result_doc[x]:
			counter+=1
			count = 0
			for y in result_doc[x]:
				if result_doc[x][y] > result_doc[x][context_to_doc_map[x][0]]:
					count+=1
			if int(count/10) in result_list:
				result_list[int(count/10)]+=1
			else:
				result_list[int(count/10)]=1
			print(count)
	print 'found in'
	print(counter)
	print result_list
	print 'total time taken'
	print("------------%s seconds -------" % (end_time-start_time))
	#return result_doc

	return result_list,counter

def evaluator(doc_idf,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,full_idf):
	results = []
	for x in xrange(100):
		result_list,counter = query_fire(doc_idf,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,full_idf)
		results.append((result_list,counter))
		if x%5 == 0:
			cp.dump(results,open('temp_final_results.pkl','w+'))
	
	

if __name__ == '__main__':
	start_time = time.time()
	print 'loading dependencies'
	mod_doc_idf = cp.load(open('/home/du3/13CS30045/citation_reco/candidate_set/novel_method/mod_doc_idf.pkl','rw'))
	full_idf=cp.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/train/full_idf.pkl','rw'))
	doc_idf = cp.load(open('/home/du3/13CS30045/citation_reco/candidate_set/novel_method/doc_idf.pkl','rw'))
	nlp_context_dict = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/train/citation_dictionary_nlp.pkl","rb+")) 
	nlp_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/train/citation_to_doc_map.pkl","rb+"))
	abs_tit_context_dict = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/train/abstract_title_dictionary_nlp.pkl","rb+"))
	abs_tit_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/train/abstract_title_id_to_doc_map.pkl","rb+"))
	feature_idf_abstract_title = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/train/idf_values_for_feature_words.pkl"))
	feature_idf_context = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/train/idf_values_for_feature_words.pkl"))
	tfidf_abstract = cp.load(open("/home/du3/13CS30045/citation_reco/abstract_title_vectors/train/nlp_abstract_title_tfidf.pkl","rw+"))
	tfidf_context = cp.load(open("/home/du3/13CS30045/citation_reco/citation_vectors/train/nlp_context_tfidf.pkl","rw+"))
	inlinks = cp.load(open('/home/du3/13CS30045/citation_reco/candidate_set/before_nlp_inlink_dictionary.pkl','rw'))
	tfidf_dict = cp.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/train/nlp_context_tfidf.pkl','rw'))
	print("--- %s seconds ---" % (time.time()-start_time))
	
	evaluator(doc_idf,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,full_idf)

	#result_doc = query_fire(doc_idf,nlp_context_dict,abs_tit_context_dict,nlp_cit_dict,abs_tit_cit_dict
#,feature_idf_abstract_title,feature_idf_context,tfidf_abstract,tfidf_context,inlinks,tfidf_dict,full_idf)
	


#	cp.dump(result_doc,open('temp_resu.pkl','w+'))
