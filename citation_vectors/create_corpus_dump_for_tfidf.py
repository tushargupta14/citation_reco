#this code creates a dump of all the papers for tfidf (not only for nlp)
#first_edit: Now this code creates a dump of only nlp corpus
#Input : cited_citer_dump_processed_v3 file,nlp papers dictionary (natural_language_and_speech_paper_list.pkl)
#Output : Corpus Dump corpus_dump.txt file which only has alphanumeric characters

import re
import cPickle as pickle

def clean_para(parag):
	clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
	clean_parag=clean_parag.lower()
	clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        return clean_parag


def create_dump():
	counter=0
	outputfile=open('nlp_corpus_dump.txt','w+')
	file=open('/home/du3/13CS30045/citation_rec/cited_citer_dump_processed_v3','rw')
	nlp_paper = pickle.load(open('natural_language_and_speech_paper_list.pkl','rw'))
	lines=file.readlines()
	for line in  lines:
		print (str(counter)+'/'+str(len(lines)))
		counter+=1
		corp_line=line.split(' ',2)
		try :
			d1=corp_line[0]
			d2=corp_line[1]
			corpus=corp_line[2]
		
		except Exception as e:
			continue
		if d1 in nlp_paper:
			if d2 in nlp_paper:		
				corpus=clean_para(corpus)

				outputfile.write(corpus+'\n')
	outputfile.close()

if __name__ == '__main__':
	create_dump()
