from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    
    #files=files[1:]
    #print(files)
    index=dict()
    i=0
    for file in files:
        texts = get_text(file)
        words_in_txt = set(words(texts))
        for word in words_in_txt:
            if word in index.keys():
                index[word].append(i)
            else:
                index[word]=[i]
        i+=1
    
    return index

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    ans_set=set()
    for i,term in enumerate(terms):
        if i==0 and term in index.keys():
            ans_set=set(index[term])
        elif term in index.keys():
            next_set=set(index[term])
            ans_set=ans_set & next_set
        else:
            return []
    
    soln = [file for j,file in enumerate(files) if j in ans_set]
    # print(ans_set)
    # print(soln)
    return soln
            
