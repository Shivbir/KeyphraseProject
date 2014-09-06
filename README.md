KeyphraseProject
================

Project to get keyphrased from articles useing NLTK.


Implementation ToDo List
================

 [ ] Find all articles in the data set and load them one at a time 
 
 [ ] implement tfidf
 
 [ ] Possibly make a document object
 
 [ ] Decide on parser
 
 [ ] Decide on graph library



Steps to create the Graph
================
1.  Tokenization of documents to get tokens
2.  Parse the tokens to get the syntax tree for sentences.   --- apple pie/ NLTK parser will assign the NP 
3.  Extracting all NP's found from the step 2 and then in case the document does not have any NP's then we have to eliminate stop words,  and also to allow words with certain part-of-speech tags(eg. noun,adjectives, verbs)

Steps 1 to 3 is part of the keyphrase extraction/ candidate phrase extraction

Lexical Ranking - step 4 and 5

4.  Make the graph using that candidate phrases(it will be nodes)
5.  For relations or the edges between the keyphrases, we will use Wordnet  ------  tdidf for wt, node wt(tdidf)and edge wt(frequency 

// Checking how many times the term appeared in the whole corpus



 Datasets
================
 http://qwone.com/~jason/20Newsgroups/
 
 http://ota.ahds.ac.uk/desc/2531

