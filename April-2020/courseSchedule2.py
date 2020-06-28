"""

2210. Course Schedule II
Medium

1732

117

Add to List

Share
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
             
             
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

"""


from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        print(prerequisites)
        graph = [[] for _ in range(numCourses)]
        print('graph', graph)        
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        print('graph', graph)
        visit = [0]*numCourses
        print('visit', visit)
        result = []
        
        def dfs(node):
            if visit[node]==1:
                return True
            if visit[node] == -1:
                return False
            visit[node] = -1
            
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visit[node] = 1
            result.append(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        return result
        
        
        
        # zero_in_degree_queue = deque()
        # in_degree, out_degree = {}, {}
        # result = []
        # for i, j in prerequisites:
        #     if i not in in_degree:
        #         in_degree[i] = set()
        #     if j not in out_degree:
        #         out_degree[j] = set()
        #     in_degree[i].add(j)
        #     out_degree[j].add(i)
        
        # print('indegree', in_degree)
        # print('outdegree', out_degree)
        
        # for i in range(numCourses):
        #     if i not in in_degree:
        #         zero_in_degree_queue.append(i)
        
        # print('zero', zero_in_degree_queue)
        # print('-------------------------')

        # while zero_in_degree_queue:
        #     prerequisite = zero_in_degree_queue.popleft()
        #     result.append(prerequisite)
        #     print('prerequisite', prerequisite)

        #     if prerequisite in out_degree:
        #         for course in out_degree[prerequisite]:
        #             print('course', course)
        #             in_degree[course].discard(prerequisite)
        #             if not in_degree[course]:
        #                 zero_in_degree_queue.append(course)

        #         del out_degree[prerequisite]
                
        #     print('indegree', in_degree)
        #     print('outdegree', out_degree)
        #     print('zero', zero_in_degree_queue)
        #     print('-------------------------')

        # if out_degree:
        #     return []

        # return result



numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().canFinish(numCourses, prerequisites))




