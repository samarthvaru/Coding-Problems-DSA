class Solution:

  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    n = len(gas)

    curr = start = 0

    for i, (g, c) in enumerate(zip(gas * 2, cost * 2)):
      if i == start + n:
        return start

      curr += g - c

      if curr < 0:
        start = i + 1
        curr = 0

    return -1


