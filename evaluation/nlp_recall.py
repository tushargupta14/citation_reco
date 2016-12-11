#File for calculating recall for a particular citation context and evaluating the candidate set 
# Input : citation context c*
# Ouput : recall value for the citation context 
import cPickle as cp 
import sys
sys.path.insert(0, '/home/du3/13CS30045/citation_reco/candidate_set')
import create_LCN_score as L
#import			
		
def cal_recall(doc_dict,nlp_context_dict,nlp_cit_dict):
	
	# Recall for top K 
	K = 10 
	recall_dict = {}
	for key,value in doc_dict.iteritems():
		recall = 0.0
		candidate_LCN_score = L.LCN(key,nlp_context_dict,nlp_cit_dict,50)	
		candidate_GN_score = G.GN(key,nlp_context_dict,nlp_cit_dict,50)
		top_K = candidate_LCN_score[2:2*K]
		top_K_docs = [x[0] for x in top_K ]
		print top_K_docs
		for c_k,c_v in nlp_context_dict.iteritems():
			 if key == c_v:
				c_key = c_k
		docs = nlp_cit_dict[c_key]
		d1 = docs[0]
		d2 = docs[1]
		if d1 in top_K_docs:
			c_d1 = top_K_docs.count(d1)
			print "yes",d1,c_d1
			recall = float(c_d1)/(2*K-1)
			print recall
		recall_dict[key]=recall
	

if __name__ == "__main__" :

	nlp_context_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_dictionary_nlp.pkl","rb+"))
	nlp_cit_dict = cp.load(open("/home/du3/13CS30045/citation_reco/dataset/citation_to_doc_map.pkl","rb+"))
	doc_dict = {}
	#doc_stack = {}
	doc_list = set()
	con_stack = set()
	for key,value in nlp_context_dict.iteritems():
		if value not in con_stack :
			doc_list = set()	
		con_stack.add(value)
		doc_list.add(nlp_cit_dict[key][0])	
		doc_dict[value] = doc_list
	print "Documemnt dictionary made"	
	cal_recall(doc_dict,nlp_context_dict,nlp_cit_dict)
