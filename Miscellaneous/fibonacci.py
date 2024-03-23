def fibonacci(n):
    #Write code here
    if n<=1: return n
    
    else: return fibonacci(n-1)+fibonacci(n-2)
        


#solution n

def fibonacci(n):
    if n<=1: return n
    prev=0
    curr = 1
    counter = 1 
    
    while counter < n:
        nextP= prev + curr
        counter+=1
        prev=curr
        curr=nextP
    
    return curr