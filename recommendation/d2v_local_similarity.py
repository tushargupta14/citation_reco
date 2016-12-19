#this module calculates similarity based on d2v vectors
#input: model /home/du3/13CS30045/citation_reco/citation_vectors/train/word_embeddings/models/doc_vectors.d2v , two textual queries
#output : similarity score

#from gensim.models import doc2vec

def similarity_score(model,list_k,c_star_list,citation_dict):
	score=0
        #c_star_vec=vq.query_vector(c_star,feature_idf)
	
	score_list = [model.n_similarity(c_star_list,citation_dict[key].split(' '))**2 for key in list_k]
        score=reduce((lambda x,y: x+y),score_list)
        #for context in list_k:
        #	l_score=cs.comp_similarity(tfidf_dict[context],c_star_vec)
        #	score+=l_score**2
        score/=len(list_k)

        return score


