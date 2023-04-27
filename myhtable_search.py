# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    hash_table=htable(4011)
    
    for file in files:
        texts = get_text(file)
        words_in_txt = set(words(texts))
        for word in words_in_txt:
            #hash_table[hashcode(word)]
            value=htable_get(hash_table,word)
            if value!=None:
                value.append(files.index(file))
                htable_put(hash_table,word,value)
            else:
                htable_put(hash_table,word,[files.index(file)])

    return hash_table
    

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    ans_set=set()
    for i,term in enumerate(terms):
        # key=hashcode(term) % len(index)
        
        bucket = index[hashcode(term) % len(index)]
        #print(bucket)
        #print("---------x---------")
        if bucket != None:
            for tupl in bucket:
                if i==0 and term == tupl[0]:
                    ans_set=set(tupl[1])
                elif term == tupl[0]:
                    next_set=set(tupl[1])
                    ans_set=ans_set & next_set
                # else:
                #     return []
            #print(ans_set)
    soln = [file for j,file in enumerate(files) if j in ans_set]
    #print("ggggggwgwg")
    #print(ans_set)
    if len(ans_set)==0:
        return []
    #print(soln)
    return soln
        
        
#         if i==0 and term in index.keys():
#             ans_set=set(index[term])
#         elif term in index.keys():
#             next_set=set(index[term])
#             ans_set=ans_set & next_set
#         else:
#             return []
    
#     soln = [file for j,file in enumerate(files) if j in ans_set]
#     # print(ans_set)
#     # print(soln)
#     return soln
            