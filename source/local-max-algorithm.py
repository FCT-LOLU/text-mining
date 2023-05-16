#the local max algorithm to get all the relevant expressions in a corpus of documents
#input: a file
#output: a list of relevant expressions
def local_max_algorithm(corpuspath):
   
    for i in range(5,1, -1):
        #get all the expressions of length i
        print(i)

#test
local_max_algorithm("test.txt")