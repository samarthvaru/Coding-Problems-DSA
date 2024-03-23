def selection_sort(nums):
    #write your code here
    for i in range(len(nums)):
        smallest = i
        
        for j in range(i+1,len(nums)):
            if nums[j] < nums[smallest]:
                smallest = j
            
        
        if i!=smallest:
            nums[i],nums[smallest]=nums[smallest],nums[i]
    
    return nums