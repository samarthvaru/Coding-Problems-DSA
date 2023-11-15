
"""
inputStr, represents the given string containing substring of latitude/longitude pairs.
"""
import re
def is_valid_pair(pair):

	if (
		pair.startswith("(")
		and pair.endswith(")")
		and pair.count(",") == 1
    ):
		x_str, y_str = pair[1:-1].split(",")
		x_str = x_str.strip()
		y_str = y_str.strip()
		if (
			not x_str.startswith(" ")
			and not x_str.endswith(" ")
			and not y_str.startswith(" ")
			and not y_str.endswith(" ")
			and not re.search(r'[a-zA-Z]', x_str)  # Check for letters in x
			and not re.search(r'[a-zA-Z]', y_str)  # Check for letters in y
		):
			try:
				x = float(x_str)
				y = float(y_str)
				if -90 <= x <= 90 and -180 <= y <= 180:
					if (x_str[0] == "+" or x_str[0] == "-") and len(x_str) > 1 and x_str[1] == "0":
						return False
					if (y_str[0] == "+" or y_str[0] == "-") and len(y_str) > 1 and y_str[1] == "0":
						return False
					if re.search(r'[a-zA-Z]', x_str) or re.search(r'[a-zA-Z]', y_str):
						return False  
					return True
			except ValueError:
				pass
	return False

def funcValidPairs(inputStr):
	# Write your code here
	result = []
	for pair in inputStr:
		if is_valid_pair(pair):
			result.append("Valid")
		else:
			result.append("Invalid")

	return result

def main():
	# input for inputStr
	inputStr = []
	inputStr_size  = int(input())
	inputStr = list(map(str,input().split()))
	
	result = funcValidPairs(inputStr)
	print(" ".join([str(res) for res in result]))	

if __name__ == "__main__":
	main()