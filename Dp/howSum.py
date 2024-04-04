## memoization
def howSum(target, numbers, memo={}):
  if target in memo:
    return memo[target]
  if target == 0:
    return []
  if target < 0:
    return None

  for n in numbers:
    remainder = target - n
    remainder_result = howSum(remainder, numbers, memo)
    if remainder_result is not None:
      memo[target] = [n] + remainder_result
      return memo[target]

  memo[target] = None
  return None


print(howSum(7, [3, 2, 1]))

# time complexity : O(n*m^2)
# space complexity : O(m^2)


# tabulation
def howSumTabulation(target, numbers):
  table = [None] * (target + 1)

  table[0] = []

  for i in range(0, target + 1):
    if table[i] != None:
      for num in numbers:
        if i + num < len(table):
          if table[i + num] == None:
            table[i + num] = [num]
          else:

            table[i + num] = table[i] + [num]

  return table[target]


print(howSumTabulation(7, [2, 3]))
