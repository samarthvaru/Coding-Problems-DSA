
def rotate_array(array,k):
    #write code 
    if len(array)==0 or k==0 or k==len(array):
        return array

    k=k%len(array)
    
    temp=array[-k:]
    
    for i in reversed(range(0,len(array)-k)):
        array[i+k]=array[i]
    
    for i in range(len(temp)):
        array[i]=temp[i]
    
    return array
    