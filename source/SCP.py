from math import log

ngrams = {}

def calculSCP(ngram, value):
    num_SCP=  pow(value["freq"],2)
    words = ngram.split()
    if(len(words)!=1):
        if(len(words)==2):
            deno_SCP = ngrams[1][words[0]]["freq"]*ngrams[1][words[1]]["freq"]
        else:    
            n=len(words)
            deno_SCP =1/(n-1)
            for i in range(1,n-1):
                word_one_to_i = ' '.join(words[0:i])
                size_word_one_to_i = len(word_one_to_i.split())
                word_i_plus_1_to_n = ' '.join(words[i+1:n])
                size_word_i_plus_1_to_n = len(word_i_plus_1_to_n.split())
                deno_SCP +=ngrams[size_word_one_to_i][word_one_to_i]["freq"]*ngrams[size_word_i_plus_1_to_n][word_i_plus_1_to_n]["freq"]
        value["SCP"] = round(num_SCP/deno_SCP,4)

def calculDice(ngrams):

    for i in range(1,9):
        j= 9-i
        
        for ngram in ngrams[j]:
            if j==1:
                ngrams[j][ngram]["Dice"] = 0
            else:
                num_Dice=  2*ngrams[j][ngram]["freq"]
                deno_Dice =1
                words = ngram.split()
                
                for word in words:
                    deno_Dice +=ngrams[1][word]["freq"]
        
                ngrams[j][ngram]["Dice"] = round(num_Dice/deno_Dice,4)

    return ngrams

def calculMI(ngrams):

    for i in range(1,9):
        j= 9-i
        
        for ngram in ngrams[j]:
            if j==1:
                ngrams[j][ngram]["MI"] = 0
            else:
                num_MI= ngrams[j][ngram]["freq"]
                deno_MI=1
                words = ngram.split()
                
                for word in words:
                    deno_MI =deno_MI*ngrams[1][word]["freq"]

                if deno_MI!=0:
                    ngrams[j][ngram]["MI"] = log(num_MI/deno_MI)
                else:
                    ngrams[j][ngram]["MI"] = 0

    return ngrams