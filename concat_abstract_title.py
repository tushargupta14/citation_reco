#this script concats title and abstract for tfidf purposes
#first edit:this script now does the same just creates two corpus one before(including) 2007 and one after 2007
#input: paper_abstract ,paper_title and /home/du3/citation_reco/papers_before_and_after/year_wise_dictionary.pkl
#output: before_paper_abstract_title and after_paper_abstract_title

import re
import cPickle as pickle

def clean_para(parag):
        clean_parag = re.sub("[^a-zA-Z]"," ",parag)
        clean_parag = re.sub(" +"," ",clean_parag)
        clean_parag = re.sub("\n","",clean_parag)
        clean_parag=clean_parag.lower()
        clean_parag=' '.join( [w for w in clean_parag.split() if len(w)>1] )
        return clean_parag



def abstract():
	print 'abstract file'
	file=open('paper_abstract','rw')
	lines=file.readlines()
	
	abstract_dict={key.split('\t')[0]:clean_para(key.split('\t')[1]) for key in lines}
	

	#for line in lines:
	#	lister=line.split('\t')
	#	abstracts=clean_para(lister[1])
	#	abstract_dict[lister[0]]=abstracts

	return abstract_dict

def title():
	print 'title file'
	file=open('paper_title','rw')
        lines=file.readlines()

        #title_dict={}

	title_dict={key.split('\t')[0]:clean_para(key.split('\t')[1]) for key in lines}

       # for line in lines:
        #        lister=line.split('\t')
         #       titles=clean_para(lister[1])
          #      title_dict[lister[0]]=titles

        return title_dict	

def corp_dump(abstract_dict,title_dict):
	print 'dumping'
	output_file_before=open('before_paper_abstract_title','w+')
	output_file_after=open('after_paper_abstract_title','w+')
	year_dict=pickle.load(open('/home/du3/13CS30045/citation_reco/papers_before_and_after/year_wise_dictionary.pkl','rw'))

	
	for docs in abstract_dict:
		if docs in title_dict:
			try:
				if int(year_dict[docs]) < 2008:
					outp=title_dict[docs]+' '+abstract_dict[docs]
					output_file_before.write(docs+'\t'+outp+'\n')
				else:
					outp=title_dict[docs]+' '+abstract_dict[docs]
                                	output_file_after.write(docs+'\t'+outp+'\n')
			except Exception as e:
				print e
				continue

	output_file_before.close()
	output_file_after.close()

if __name__ == '__main__' :
	a=abstract()
	t=title()
	corp_dump(a,t)
	
