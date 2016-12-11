#this script divides the cited_citer_dump_processed_v3 , paper_abstract and paper_title into before and after a particular year (2005 currently)
#input : the files mentioned above and paper_years_final
#ouput : it dumps the above files with a before_ and after_concatenated before their file names into train and test folders


import cPickle as pickle

def year_wise_dict():
	file = open('/home/du3/13CS30045/citation_reco/paper_years_final','rw')
	lines = file.readlines()
	
	year_dict={line.split('\t')[0]:line.split('\t')[1] for line in lines}
	
	pickle.dump(year_dict,open('year_wise_dictionary.pkl','w+'))
	return year_dict

def cit_split(year_dict):
	file = open('/home/du3/13CS30045/citation_reco/dataset/cited_citer_dump_processed_v3','rw')
	lines = file.readlines()

	output_file_before = open('/home/du3/13CS30045/citation_reco/papers_before_and_after/train/before_cited_citer_dump_processed_v3','w+')
	output_file_after = open('/home/du3/13CS30045/citation_reco/papers_before_and_after/test/after_cited_citer_dump_processed_v3','w+')

	count=0

	for line in lines:
		d=line.split(' ',2)
		
		if d[1] not in year_dict:
			count+=1
			
		try:
			if int(year_dict[d[1]]) < 2008:
				output_file_before.write(line)
			else:
				output_file_after.write(line)

		except Exception as e:
			#print e
			continue

	print count
	output_file_before.close()
	output_file_after.close()

if __name__ == '__main__':
	cit_split(year_wise_dict())
