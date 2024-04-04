## Memoization
def countConstruct(target, wordBank, memo={}):
  if target in memo:
    return memo[target]
  if target == '':
    return 1

  totalCount = 0
  for word in wordBank:
    if target.startswith(word):
      suffix = target[len(word):]
      newwithRest = countConstruct(suffix, wordBank, memo)
      totalCount += newwithRest

  memo[target] = totalCount
  return totalCount


# time complexity : O(n*m^2)
# space comlexity : O(m^2)

print(countConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))


# Tabulation
def countConstructTab(target, wordBank):
  table = [0] * (len(target) + 1)
  table[0] = 1

  for i in range(len(target)):

    for word in wordBank:
      if target[i:].startswith(word):
        table[i + len(word)] += table[i]

  return table[len(target)]


print(countConstructTab('abcdef', ['ab', 'abc', 'cd', 'ef', 'def', 'abcd']))
