class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Create an array list to store the output result...
        output = []
        for i in range(numRows):
            if(i == 0):
                prev = [1]
                output.append(prev)
            else:
                curr = [1]
                j = 1
                while(j < i):
                    curr.append(prev[j-1] + prev[j])
                    j+=1
                # Store the number 1...
                curr.append(1)
                # Store the value in the Output array...
                output.append(curr)
                # Set prev is equal to curr...
                prev = curr
        return output       # Return the output list of pascal values...        