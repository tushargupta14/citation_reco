def comp_similarity(c1,c2):
	
	c1_feature_dict = c1[0]
	c2_feature_dict = c2[0]
	
	def ret(key):
		return c1_feature_dict[key]*c2_feature_dict[key]

	min_len = min(c1[2],c2[2])
	score =0
	if c1[2] < c2[2] :
		#for key,value in c1_feature_dict.iteritems():
		#	if key in c2_feature_dict.keys():
		#		score+= c1_feature_dict[key]*c2_feature_dict[key]
		
		try :
			lists = [key for key in c1_feature_dict if key in c2_feature_dict]
			score = reduce((lambda x,y : x+y),map(ret,lists))
		except Exception as e:
			#print e 
			score = 0 

	else:
	#elif c2[2] >= c1[2] :
		#for key,value in c2_feature_dict.iteritems():
		#	if key in c1_feature_dict.keys():
		#		score+= c2_feature_dict[key]*c1_feature_dict[key]
		try :

			lists = [key for key in c2_feature_dict if key in c1_feature_dict]
        	        score = reduce((lambda x,y : x+y),map(ret,lists))
		except Exception as e:
			#print e
			score = 0

	score = score/(c1[1]*c2[1])
	return score
	

if __name__ == "__main__":
	#comp_similarity(c1,c2)
	pass	
