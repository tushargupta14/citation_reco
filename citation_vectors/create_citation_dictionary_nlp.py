#this script creates citation dictionary , it gives every citaion an id and 
#also creates a citation id to document id map 
#Input:cited_citer_dump_processed_v3, nlp papers dictionary 
#Output:Citation dictionary , citation id to document id map

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
	file=open('/home/du3/13CS30045/citation_rec/cited_citer_dump_processed_v3','rw')
	nlp_docs=pickle.load(open('natural_language_and_speech_paper_list.pkl'))
	print('loaded dependencies')
	lines=file.readlines()
	citation_dic={}
	citation_to_doc_map={}
	counter=1
	line_count=1
	for line in lines:
		print(str(line_count)+'/'+str(len(lines)))
		line_count+=1
		instance=line.split(' ',2)
		#print instance
		try:
			d1=instance[0]
			d2=instance[1]
			context=instance[2]
		except Exception as e:
			print 'caught'
			continue
		if d1 in nlp_docs:
			if d2 in nlp_docs:
				context=clean_para(context)
				if len(context) < 10 :
					continue
				citation_dic[counter]=context
				citation_to_doc_map[counter]=(d1,d2)
				counter+=1		
	pickle.dump(citation_dic,open('citation_dictionary_nlp.pkl','w+'))
	pickle.dump(citation_to_doc_map,open('citation_to_doc_map.pkl','w+'))

if __name__ == '__main__':
	create_dictionary()
