# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    
    #print(files)
    #files=files[1:]
    ans=[]
    for file in files:
        i=0
        #print(file)
        texts=get_text(file)
        words_in_txt = words(texts)
        #print(words_in_txt)
        #print(terms)
        for term in terms:
            if term in words_in_txt:
                i+=1
        if i==len(terms):
            ans.append(file)
    #print(ans) # Should I remove the path??
    
    return ans
            