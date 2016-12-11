#this module defines function for calculation of vectors for new queries
#input query,feature_idf(feature words and their idf)
#ouput list <tfidf_dictionary,norm,len>
import re
def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        return clean_parag

def norm_cal(a):
	sum =0
	for words in a:
		sum+=a[words]**2
	sum=sum**(0.5)
	return sum

def query_vector(query,feature_idf):
	query=clean_para(query)
	context_word_list={}
        output_word_list={}
        for words in query.split(' '):
                if words not in context_word_list:
                        context_word_list[words]=1
                else:
                        context_word_list[words]+=1
	
	lists = [key for key in context_word_list if key in feature_idf]
	output_word_list={key:feature_idf[key]*context_word_list[key] for key in lists }
		

        #for words in context_word_list:
        #        if words in feature_idf:
        #                output_word_list[words]=feature_idf[words]*context_word_list[words]
	a = [output_word_list,norm_cal(output_word_list),len(output_word_list)]
        return a

