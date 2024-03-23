def isomorphic_strings(s, t):
    #write code here
    temp={}
    for i in range(len(s)):
        if s[i] not in temp:
            temp[s[i]]=t[i]
        
        if temp[s[i]]!=t[i]:
            return False
    
    return True