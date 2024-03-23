
a = 'have a good day'

output = 'day doog a evah'

def func(a):
    words = a.split()
    for i in range(len(words)):
        if i%2==1:
            words[i] = words[i][::-1]
    words.reverse()
    output_str = ' '.join(words) 
    return output_str

#print
print(func(a))


    
    