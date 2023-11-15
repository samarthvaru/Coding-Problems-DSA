def sorted_squared(array):
  #write code here.make sure to return desired array
    new_array=[]
    
    if len(array)==0:
        return array
        
    for i in array:
        new_array.append(i**2)
      
    return sorted(new_array)