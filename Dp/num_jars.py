
"""
numJars, represents the number of jars.
Value of the array represents the number of chocolates in each jar.
"""
def maxSum(inputArr):
	# Write your code here
	n = len(inputArr)

	if n == 1:
		return inputArr[0]

	dp = [0] * n

	dp[0] = inputArr[0]
	dp[1] = max(inputArr[0], inputArr[1])

	for i in range(2, n):
		dp[i] = max(dp[i-1], dp[i-2] + inputArr[i])

	return dp[n-1]

def main():
	# input for inputArr
	inputArr = []
	inputArr_size  = int(raw_input())
	inputArr = list(map(int,raw_input().split()))
	
	result = maxSum(inputArr)
	print(result)	

if __name__ == "__main__":
	main()