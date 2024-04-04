# tabulation
def canSumTabulation(target, numbers):
  table = [None] * (target + 1)

  table[0] = True

  for i in range(0, target + 1):
    if table[i] == True:
      for num in numbers:
        if i + num < len(table):
          table[i + num] = True

  return table[target]


print(canSumTabulation(7, [2, 3]))
