def merge_sorted_array(array1,array2):
    merged_array = []
    i,j = 0,0
    
    while i<len(array1) and j<len(array2):
        if array1[i] <= array2[j]:
            merged_array.append(array1[i])
            i+=1
        else:
            merged_array.append(array2[j])
            j+=1
    
    while i<len(array1):
        merged_array.append(array1[i])
        i+=1
    
    while j<len(array2):
        merged_array.append(array2[j])
        j+=1
    
    return merged_array


def merge_sort(array):
    #write your code here
    if len(array)<=1:
        return array
    
    middle = len(array)//2
    
    left_side = merge_sort(array[:middle])
    right_side = merge_sort(array[middle:])
    
    return merge_sorted_array(left_side,right_side)