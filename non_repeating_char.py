def non_repeating_char(str):
    #Write code here
        for i in range(len(str)):
            repeat = False
            for j in range(len(str)):
                if i!=j and str[i]==str[j]:
                    repeat=True
            if repeat == False:
                return i
        return None
        
#solution 2

def non_repeating_char(str):
    ht={}
    for i in str:
        if i in ht:
            ht[i]+=1
        else:
            ht[i]=1
            
    for i in range(len(str)):
        if ht[str[i]]==1:
            return i
    return None