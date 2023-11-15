def power_sum(array,power=1):
    #write code here
    summ = 0
    for i in array:
        if type(i) == list:
            summ += power_sum(i,power+1)
        
        else:
            summ += i
        
    return summ**power