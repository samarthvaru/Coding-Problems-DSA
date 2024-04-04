class Solution:

  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)

    ratings_d = sorted((x, i) for i, x in enumerate(ratings))

    candy = [1] * n

    for _, i in ratings_d:
      if i > 0 and ratings[i] > ratings[i - 1]:
        candy[i] = max(candy[i], candy[i - 1] + 1)

      if i < n - 1 and ratings[i] > ratings[i + 1]:
        candy[i] = max(candy[i], candy[i + 1] + 1)

    return sum(candy)


'''
if kid > l_kid:
  candy = candy[l_kid] + 1

if kid > r_kid:
  candy = candy[r_kid] + 1
'''
