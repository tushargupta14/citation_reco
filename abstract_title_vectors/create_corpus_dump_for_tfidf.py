#this code creates a dump of all the papers for tfidf (not only for nlp)
#Input : paper_abstract_title file,nlp papers dictionary (natural_language_and_speech_paper_list.pkl)
#Output : Corpus Dump abstract_title_corpus_dump.txt file which only has alphanumeric characters

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
	outputfile=open('abstract_title_corpus_dump.txt','w+')
	file=open('/home/du3/13CS30045/citation_reco/paper_abstract_title','rw')
	nlp_paper = pickle.load(open('natural_language_and_speech_paper_list.pkl','rw'))
	lines=file.readlines()
	for line in  lines:
		print (str(counter)+'/'+str(len(lines)))
		counter+=1
		corp_line=line.split('\t')
		try :
			d=corp_line[0]
			corpus=corp_line[1]
		
		except Exception as e:
			continue
		
		corpus=clean_para(corpus)
		outputfile.write(corpus+'\n')
	outputfile.close()

if __name__ == '__main__':
	create_dump()
