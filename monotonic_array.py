def monotonic_array(array):
    #write code here
    if len(array)==1 or len(array)==0:
        return True
    i=array[0]
    j=array[1]
    
    increasing = False
    decreasing = False
    
    if i>=j:
        decreasing = True
    else:
        increasing = True
    
        
    for i in range(2,len(array)):
        if increasing:
            if array[i-1]>=array[i]:
                return False
        
        if decreasing:
            if array[i-1]<=array[i]:
                return False
    
    return True