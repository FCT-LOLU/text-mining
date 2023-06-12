# Project Text Mining

## Introduction

This project has been realised by Lucie Boucher (66862) and Lola Montignier (66860).\
In the context of the text mining course, we had to implement the local max extractor algorithm in aim to find the most relevant expression of documents of a corpus

## Local Max Extractor

We provide the folder source/ with all the python files.\
We also provide the folders corpus2mw/ and frenchCorpus/ with all the texts used in the algorithm.

### How to run the code

To run the code, you will have to open a terminal and run the command python3 source/localMax.py 

You can find the results for the english and french corpus respectively in the files corpus2.csv and frenchcorpus.csv

### Quality of our results

To evaluate the quality of our algorithm, we calculated the precision, recall and F metric for each of our corpus and each metric (SCP, Dice, MI).\
 You can find the results by running the command python3 source/recall.py in your terminal. \
 To see in further details, every relevant expressions used to calculate those measures can be found in the following files : 
* RE.txt
* PrecisionSCP.txt
* PrecisionDice.txt
* PrecisionMI.txt
* FrenchRecal.txt
* FrenchPrecisionSCP.txt
* FrenchPrecisionDice.txt
* FrenchPrecisionMI.txt

### 15 most relevant expression

Finally, we extract the 15 most relevant expression for each document of the english corpus, you can find all the result in the file corpus_15_most_specific_relevant_expressions.csv 