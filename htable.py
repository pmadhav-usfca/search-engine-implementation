"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for i in range(nbuckets)]

def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    
    h=0
    if o == None:
        return None
    elif type(o) == str:
        if o.isnumeric():
            h += int(o)
        else:
            for c in o:
                h = h*31 + ord(c)
    else:
        h+=o
    
    return h
        


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket=table[hashcode(key) % len(table)]
    n=len(table[hashcode(key) % len(table)])
    for tupl in bucket:
        if key == tupl[0]:
            return bucket.index(tupl)
    
    return None

def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    bucket = table[hashcode(key) % len(table)]
    #tuple_indx = bucket_indexof(table,key)
    
    for tupl in bucket:
        if key == tupl[0]:
            bucket[bucket.index(tupl)] = (key,value)
            break
            
    else:
        bucket.append((key,value))
    return table
        
#     bucket = table[hashcode(key)% len(table)]
#     for tpl in bucket:
#         if key == tpl[0]:
#             bucket[bucket.index(tpl)] = (key,value)
#             break
            
#     else:
#         bucket.append((key,value))
#     return table
        
def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket = table[hashcode(key) % len(table)]
    if bucket != None:
        for tupl in bucket:
            if key == tupl[0]:
                return tupl[1]
    else:
        return None
    
    

def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    ans=''
    for i in range(len(table)):
        ans+=str(i).zfill(4)+'->'
        bucket=''
        if table[i]!=None:
            for tupl in table[i]:
                bucket+=str(tupl[0])+':'+str(tupl[1])+', '
            bucket=bucket[:-2]
        ans+=bucket+'\n'
        
    return ans
    

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    ans='{'
    for bucket in table:
        for tupl in bucket:
            ans+=str(tupl[0])+':'+str(tupl[1])+', '
    if len(ans)==1:
        ans += '}'
    else:
        ans = ans[:-2] + '}'
    return ans
    
    
    