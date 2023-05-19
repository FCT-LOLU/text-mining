from math import log

def calculSCP(ngrams):

    for i in range(1,9):
        j= 9-i
        
        for ngram in ngrams[j]:
            if j==1:
                ngrams[j][ngram]["SCP"] = 0
            else:
                num_SCP=  pow(ngrams[j][ngram]["freq"],2)
                deno_SCP =1
                words = ngram.split()
                
                for word in words:
                    deno_SCP =deno_SCP*ngrams[1][word]["freq"]
        
                ngrams[j][ngram]["SCP"] = round(num_SCP/deno_SCP,4)

    return ngrams

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