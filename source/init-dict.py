def init_dict_multiwords_expression(corpuspath):
    #open the file
    with open(corpuspath, 'r') as corpus:
        #create a dictioionary of ngrams
        ngrams = {}
        #read the file line by line
        for line in corpus:
            #split the line into words
            words = line.split()
            #create a list of ngrams and get all the ngrams lenght 2 to 8
            for i in range(1,9):
                bysize = {}
                for j in range(len(words)-i+1):
                    ngram = ' '.join(words[j:j+i])
                    #if the ngram is not in the dictioionary, add it
                    if ngram not in bysize:
                        bysize[ngram]={}
                        bysize[ngram]["freq"] = 1
                        bysize[ngram]["SCP"] = 0
                        bysize[ngram]["MaxOmegaPlusSCP"] = 0
                        bysize[ngram]["MaxOmegaMinusSCP"] = 0
                    else:
                        #increment the ngram freq value
                        bysize[ngram]["freq"] += 1
                ngrams[i] = bysize
        
        return ngrams

