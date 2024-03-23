l = [-2,-3,1,2,6,4,5]

def secondLargestInList(l):
  secondMax = float('-inf')

  max = float('-inf')
  
  for i in l:
    if i > max:
      secondMax = max
      max = i
    elif i > secondMax:
      secondMax = i

  return secondMax

print(secondLargestInList(l))
