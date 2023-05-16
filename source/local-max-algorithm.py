#the local max algorithm to get all the relevant expressions in a corpus of documents
#input: a file
#output: a list of relevant expressions
def local_max_algorithm(corpuspath):
    #open the file
    with open(corpuspath, 'r') as corpus:
        #create a dictioionary of ngrams
        ngrams = {}
        #read the file line by line
        for line in corpus:
            #split the line into words
            words = line.split()
            #create a list of ngrams and get all the ngrams lenght 2 to 8
            for i in range(1,8):
                bysize = {}
                for j in range(len(words)-i+1):
                    ngram = ' '.join(words[j:j+i])
                    #if the ngram is not in the dictioionary, add it
                    first = ngram[0]
                    if first not in bysize:
                        bysize[first]={}
                        bysize[first][ngram] = 1
                    else:
                        if ngram not in bysize[first]:
                            bysize[first][ngram] = 1
                        else:
                            #increment the ngram value
                            bysize[first][ngram] += 1
                ngrams[i] = bysize
            
        #print the ngrams
        print_dictio(ngrams, level=0)

def print_dictio(dictio, level=0):
    for cle, value in dictio.items():
        if isinstance(value, dict):
            print('\t' * level + str(cle) + ':')
            print_dictio(value, level + 1)
        else:
            print('\t' * level + str(cle) + ': ' + str(value))


#test
local_max_algorithm('test.txt')