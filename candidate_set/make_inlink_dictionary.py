#this script makes an inlink dictionary for each doc in the nlp dataset (train set)
#first_edit: this needs to be changed because their are inlinks which weren't there before 2008
#input:(train set) citation to doc mapping (citation_to_doc_map.pkl),year_wise_dictionary:/home/du3/13CS30045/citation_reco/papers_before_and_after/
#year_wise_dictionary.pkl
#ouput:dictionary before_nlp_inlink_dicitionary.pkl with key=docID and value=dictionary of citationIDs



import cPickle as pickle

def make_dict():
	#contexts = pickle.load(open('citation_dictionary_nlp.pkl','rw'))
	docMap = pickle.load(open('/home/du3/13CS30045/citation_reco/citation_vectors/train/citation_to_doc_map.pkl','rw'))
	
	year_dict=pickle.load(open('/home/du3/13CS30045/citation_reco/papers_before_and_after/year_wise_dictionary.pkl','rw'))

	inlinkDict={}
	counter=0	
	
	for context in docMap:
		try:
			if int(year_dict[str(docMap[context][1])]) > 2008:
				continue
		except Exception as e:
			print e
		print(str(counter)+'/'+str(len(docMap)))
		counter+=1
		d1=docMap[context][0]
		if d1 in inlinkDict:
			if context in inlinkDict[d1]:
				continue
			else:
				inlinkDict[d1].append(context)
		else:
			inlinkDict[d1]=[]
			inlinkDict[d1].append(context)

	pickle.dump(inlinkDict,open('before_nlp_inlink_dictionary.pkl','w+'))

if __name__ == '__main__':
	make_dict()
