# memoization
def allConstruct(target, wordBank, memo={}):
  if target in memo:
    return memo[target]
  if target == '':
    return [[]]

  result = []
  for word in wordBank:
    if target.startswith(word):
      suffix = target[len(word):]
      suffixWays = allConstruct(suffix, wordBank, memo)
      targetWays = [[word] + way for way in suffixWays]
      result.extend(targetWays)

  memo[target] = result
  return result


#time complexity: O(n^m)
# space complexity: O(m)

print(allConstruct('abcdef', ['ab', 'abc', 'cd', 'ef', 'def', 'abcd']))
