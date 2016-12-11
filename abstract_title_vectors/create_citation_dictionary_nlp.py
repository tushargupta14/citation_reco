#this script creates abstract_title dictionary for nlp papers only , and also creates a abstract_title id to doc map
#Input:paper_abstract_title, nlp papers dictionary 
#Output:abstract_title dictionary , abstract_title id to document id map

import cPickle as pickle
import re

def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag = clean_parag.lower()
	clean_parag = ' '.join( [w for w in clean_parag.split() if len(w)>1] )
	return clean_parag

def create_dictionary():
	file=open('/home/du3/13CS30045/citation_reco/paper_abstract_title','rw')
	nlp_docs=pickle.load(open('/home/du3/13CS30045/citation_reco/dataset/natural_language_and_speech_paper_list.pkl'))
	print('loaded dependencies')
	lines=file.readlines()
	abstract_title_dic={}
	abstract_title_id_to_doc_map={}
	counter=1
	line_count=1
	for line in lines:
		print(str(line_count)+'/'+str(len(lines)))
		line_count+=1
		instance=line.split('\t')
		#print instance
		try:
			d=instance[0]
			context=instance[1]
		except Exception as e:
			print 'caught'
			continue

		if d in nlp_docs:
			context=clean_para(context)
			if len(context.split(' ')) < 10 :
				continue
			abstract_title_dic[counter]=context
			abstract_title_id_to_doc_map[counter]=d
			counter+=1		
	pickle.dump(abstract_title_dic,open('abstract_title_dictionary_nlp.pkl','w+'))
	pickle.dump(abstract_title_id_to_doc_map,open('abstract_title_id_to_doc_map.pkl','w+'))

if __name__ == '__main__':
	create_dictionary()
