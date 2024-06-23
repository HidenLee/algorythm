# https://leetcode.com/problems/path-with-maximum-probability/description/
from typing import List
import heapq
from collections import defaultdict
class Solution:
    # fail - time
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        route = [[] for _ in range(n)]
        for idx, (fr,to) in enumerate(edges):
            route[fr].append((to,succProb[idx]))
            route[to].append((fr,succProb[idx]))
        maxprobability = [0.0 for _ in range(n)]
        maxprobability[start_node] = 1.0
        stack = [(start_node,1.0)]
        while(stack):
            onode, oprob = stack.pop()
            if oprob < maxprobability[onode]:
                continue
            
            for nnode, routeprob in route[onode]:
                nprob = oprob * routeprob
                if maxprobability[nnode] < nprob:
                    maxprobability[nnode] = nprob
                    stack.append((nnode,nprob))

        return maxprobability[end_node]
    
    # pass - use priority queue with maxheap
    def maxProbability2(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        route = [[] for _ in range(n)]
        for idx, (fr,to) in enumerate(edges):
            route[fr].append((to,succProb[idx]))
            route[to].append((fr,succProb[idx]))
        maxprobability = [0.0 for _ in range(n)]
        maxprobability[start_node] = 1.0
        stack = [(-1.0,start_node)]
        while(stack):
            oprob, onode = heapq.heappop(stack)
            oprob *= -1
            if onode == end_node:
                return oprob
            
            for nnode, routeprob in route[onode]:
                nprob = oprob * routeprob
                if maxprobability[nnode] < nprob:
                    maxprobability[nnode] = nprob
                    heapq.heappush(stack,(-nprob,nnode))

        return 0.00000

    # use dictionary but memory efficiency become worse then sol2. i guess the differences are came from import defaultdict library
    def maxProbability3(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # route = [[] for _ in range(n)]
        route = defaultdict(list)
        for idx, (fr,to) in enumerate(edges):
            route[fr].append((to,succProb[idx]))
            route[to].append((fr,succProb[idx]))
        maxprobability = [0.0 for _ in range(n)]
        maxprobability[start_node] = 1.0
        stack = [(-1.0,start_node)]
        while(stack):
            oprob, onode = heapq.heappop(stack)
            oprob *= -1
            if onode == end_node:
                return oprob
            
            for nnode, routeprob in route[onode]:
                nprob = oprob * routeprob
                if maxprobability[nnode] < nprob:
                    maxprobability[nnode] = nprob
                    heapq.heappush(stack,(-nprob,nnode))

        return 0.00000



sol = Solution()
print(sol.maxProbability2(5, [[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]],[0.37,0.17,0.93,0.23,0.39,0.04], 3, 4))  # Output should be 0.25