class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        
        rstart, rend = 0, M - 1
        # Consider the end record
        while rstart < rend:
            rmid = (rstart + rend) // 2
            if matrix[rmid][-1] == target:
                return True
            elif target < matrix[rmid][-1]:
                # If target is less than last element in row it could still belong to that row
                rend = rmid
            else:
                # If target is greater than end element it must belong at least to the i + 1 row
                rstart = rmid + 1
        
        desired_row = rstart
        
        # Apply the same logic at col level
        cstart, cend = 0, N - 1
        
        while cstart < cend:
            cmid = (cstart + cend) // 2
            if matrix[desired_row][cmid] == target:
                return True
            elif target < matrix[desired_row][cmid]:
                cend = cmid - 1
            else:
                cstart = cmid + 1
        
        desired_col = cstart
        
        return matrix[desired_row][desired_col] == target     