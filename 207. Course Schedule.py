from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        store = defaultdict(list);
        visit = [False for _ in range(numCourses)]
        for course1, course2 in prerequisites:
            store[course1].append(course2);
        
        def dfs(num):
            if visit[num]==-1:
                return False;
            if visit[num]==1:
                return True;
            
            visit[num] = -1;
            for course in store[num]:
                if not dfs(course):
                    return False;
            
            visit[num] = 1;
            return True;
    
        for i in range(numCourses):
            if not dfs(i):
                return False;
        
        return True
        
        