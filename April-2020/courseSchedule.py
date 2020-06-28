"""

207. Course Schedule
Medium

3100

157

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
             
             
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
 

Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. 
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

"""


from collections import defaultdict, deque


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        graph = [[] for _ in range(numCourses)]
        for post, pre in prerequisites:
            graph[post].append(pre)
        print(graph)
        visit = [0]*numCourses
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
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
        
        # zero_in_degree_queue = deque()
        # in_degree, out_degree = {}, {}
        
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
        #     return False

        # return True



numCourses = 2
prerequisites = [[1,0], [1, 2], [1,3]]
print(Solution().canFinish(numCourses, prerequisites))




