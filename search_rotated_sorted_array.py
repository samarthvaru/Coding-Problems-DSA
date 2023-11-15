def search_rotated_sorted_array(nums,target):
    #write your code here
    left=0
    right=len(nums)-1
    
    while(left<=right):
        middle=(left+right)//2
        if nums[middle]==target: return middle
        if nums[left]<=nums[middle]:
            #left part is sortedd
            if target >= nums[left] and target <nums[middle]:
                right = middle-1
            else:
                left = middle +1
            
        else:
            #right part is sorted
            if target <=nums[right] and target > nums[middle]:
                left = middle+1
            else:
                right = middle - 1
    return -1