class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = { i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited_set = set()

        def dfs(crs):
            if crs in visited_set:
                return False
            if preMap[crs] == []:
                return True

            visited_set.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited_set.remove(crs)

            preMap[crs] = []
            return True
        

        for crs in range(numCourses):
            if not dfs(crs): return False
        
        return True
            