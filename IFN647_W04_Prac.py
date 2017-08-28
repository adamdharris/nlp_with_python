# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 17:18:02 2017

@author: adamd
"""
'''
Occurrence matrix for set of terms (t) and documents (D).
Each entry in the matrix specifies the number of times the term occurs in a 
document.  For example t1 occurs in Document D3 three times.

    |    | D1 | D2 | D3 |
    | t1 |  3 |  0 |  6 |
    | t2 |  0 |  3 |  4 |
    | t3 |  6 |  3 |  0 |
    | t4 |  0 |  4 |  2 |
    | t5 |  1 |  0 |  3 |

'''
import numpy as np

occurrence_matrix = ([[3,0,6],[0,3,4],[6,3,0],[0,4,2],[1,0,3]])

no_Doc = 3 #number of documents in the collection


'''
Activity 1(a)
For each of the documents (Doc 1 – Doc 3) identify the inverse document frequency weight (idf)

IDF(t) = log_e(Total number of documents / Number of documents with term t in it).
'''

# calculating number of Documents (D) with term (t)
doc_with_term = np.count_nonzero(occurrence_matrix, axis=1)

for index, d in enumerate(doc_with_term):
    print("Documents with t",index+1,"=",d)

print('-'*50)
print('Activity 1(a)\n')
print('The idf weight for each term in documents D1-D3\n')

# calculating idf
idf = []

for index, d in enumerate(doc_with_term):
        x = np.log(no_Doc/d) # numpy log is base (e)
        idf = np.append(idf,x)
        print ("idf of t",index+1,"=", x)
        
'''
Activity 1(b)

Construct a term Χ document matrix which lists the term frequency weight (tf) 
for each term in each document [tf]
'''        
print('-'*50)
print('Activity 1(a)\n')

# Calculating the total number of terms in the collection
total_terms = np.sum(occurrence_matrix) 

# Calculating the total number of terms in each Document D1-D3

terms_per_Doc = np.sum(occurrence_matrix, axis=0)

for index, t in enumerate(terms_per_Doc):
    print ("Terms in D",index+1, "=",t)

print("\nTotal number of terms in the collection =",total_terms)

# Calculating the term frequency for each term (t) in Document (D) for the 
# collection

tf = np.divide(occurrence_matrix, terms_per_Doc)

print("\nTerm frequency (tf) matrix for each term (t) in Document (D)")
print(nk)

'''
Activity 1(c)

Matrix that lists the tf.idf weight for each term (t) in each document (D)
'''
print('-'*50)
print('Activity 1(c)\n')
tf_idf = []

for index, i in enumerate(idf):
    tf_idf = np.multiply(tf[:index],i) 
    
print('The tf-idf matrix for each term (t) in each document (D)\n')
print(tf_idf)

'''
Activity 1(d)

Determine which set of documents would be retrieved if the user issued the 
follow Boolean query “t2 AND t3”.
'''
print('-'*50)
print('Activity 1(d)')

# Creating a true false matrix of the occurence table by converting values
# greater than zero in the tf-idf to 1.
t_f = tf_idf
t_f[tf_idf > 0] = 1 

# extracting t2 t3 values from the true_false table
t2 = np.array(t_f[1:2])
t3 = np.array(t_f[2:3])

# chcecking where columns in t2 AND t3 are true
t2t3 = np.logical_and(t2,t3)

for index, row in enumerate(t2t3):
        for index, t in enumerate(row):
            if t == True:
                print ('D',index+1,t,'- will be retrieved')

'''
Activity 1(e)

Determine which set of documents would be retrieved if the user issued 
the follow Boolean query “t2 OR t3”.
''' 
print('-'*50)
print('Activity 1(e)')

# checking where columns in t2 OR t3 are true               
t2t3 = np.logical_or(t2,t3)

for index, row in enumerate(t2t3):
        for index, t in enumerate(row):
            if t == True:
                print ('D',index+1,t,'- will be retrieved')

'''
Activity 1(f)

Determine the rank of documents retrieved if the user issued 
the following query “t2 t3” using the cosine similarity in equation 4. 
Each term in the query has the weighting of 1.
'''
tf_idf = []

for index, i in enumerate(idf):
    tf_idf = np.multiply(tf[:index],i) 

t2_weight = 1.0
t3_weight = 1.0    

tfidf_t2t3 = tf_idf[1:3]

print(tf_idf_t2t3) 
