def lensubstring(strr): 
      
    n = len(strr) 
    distinct = len(set([x for x in strr])) 
    dic = {}
    count = 0
    start = 0
    mlen = n 
    
    for j in range(n): 
        if strr[j] in dic.keys():
            dic[strr[j]] +=1
        else:
            dic[strr[j]] = 1
            count += 1


        if count == distinct: 
            while dic[strr[start]] > 1: 
                if dic[strr[start]] > 1: 
                    dic[strr[start]] -= 1
                      
                start += 1
                  
            windowlen = j - start + 1
              
            if mlen > windowlen: 
                mlen = windowlen 
                start_index = start 
  
    return len(str(strr[start_index: start_index + mlen])) 


X = input()                           
print(lensubstring(X))