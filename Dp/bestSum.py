## memoization
def bestSum(target, numbers, memo={}):
  if target in memo:
    return memo[target]
  if target == 0:
    return []
  if target < 0:
    return None

  shortest = None
  for n in numbers:
    remainder = target - n
    remainder_result = bestSum(remainder, numbers, memo)
    if remainder_result is not None:
      combination = [n] + remainder_result
      if shortest is None or len(combination) < len(shortest):
        shortest = combination
  memo[target] = shortest
  return shortest


print(bestSum(7, [3, 2, 1]))
print(bestSum(8, [2, 3, 5]))

# time complexity : O(n*m^2)
# space complexity : O(m^2)


# tabulation
def bestSumTabulation(target, numbers):
  table = [None] * (target + 1)

  table[0] = []

  for i in range(0, target + 1):
    if table[i] != None:
      for num in numbers:
        if i + num < len(table):
          comb = table[i] + [num]
          if not table[i + num] or len(table[i + num]) > len(comb):
            table[i + num] = table[i] + [num]

  return table[target]


print(bestSumTabulation(8, [2, 3, 5]))
print(bestSumTabulation(7, [5, 3, 4, 7]))
