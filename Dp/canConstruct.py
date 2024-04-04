## Memoization
def canConstruct(target, wordBank, memo={}):
  if target in memo:
    return memo[target]
  if target == '':
    return True

  for word in wordBank:
    if target.startswith(word):
      suffix = target[len(word):]
      if canConstruct(suffix, wordBank, memo):
        memo[target] = True
        return True

  memo[target] = False
  return False


# time complexity : O(n*m^2)
# space comlexity : O(m^2)

print(canConstruct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))


# Tabulation
def canConstructTab(target, wordBank):
  table = [False] * (len(target) + 1)
  table[0] = True

  for i in range(len(target)):
    if table[i] == True:
      for word in wordBank:
        if target[i:].startswith(word):
          table[i + len(word)] = True

  return table[len(target)]


print(canConstructTab('abcdef', ['ab', 'abc', 'cd', 'ef', 'def', 'abcd']))

