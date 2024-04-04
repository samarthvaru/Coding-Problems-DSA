'''
Memoization
'''


def gridTraveller(n, m, memo={}):
  key = (m, n)
  if key in memo:
    return memo[key]
  if m == 1 and n == 1:
    return 1
  if m == 0 or n == 0:
    return 0
  memo[key] = gridTraveller(n - 1, m, memo) + gridTraveller(n, m - 1, memo)
  return memo[key]


print(gridTraveller(18, 18))

# O(n*m) time | O(n+m) space


# Tabulation
def gridTravellerTabulation(m, n):
  table = [[0] * (n + 1) for _ in range(m + 1)]
  table[1][1] = 1
  for i in range(m + 1):
    for j in range(n + 1):
      current = table[i][j]
      if j + 1 <= n:
        table[i][j + 1] += current
      if i + 1 <= m:
        table[i + 1][j] += current
  return table[m][n]


# time complexity : O(m*n)
# space complexity : O(m*n)

print(gridTravellerTabulation(3, 3))
