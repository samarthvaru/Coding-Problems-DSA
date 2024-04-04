'''
Memoization
'''


def fibonacci(n, memo={}):
  if n in memo:
    return memo[n]
  if n <= 2:
    return 1
  memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
  return memo[n]


print(fibonacci(50))

# O(n) time | O(n) space


# tabulation
def fibTabulation(number):
  table = [0] * (number + 1)
  table[1] = 1
  for i in range(number):
    if i + 1 <= number:
      table[i + 1] += table[i]
    if i + 2 <= number:
      table[i + 2] += table[i]

  return table[number]


# time complexity : O(n)
# spaace complexity : O(n)

print(fibTabulation(6))
