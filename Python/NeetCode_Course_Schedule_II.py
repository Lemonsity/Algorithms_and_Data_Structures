from collections import deque
import copy

def findOrder(numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    max_course = numCourses
    for [course, prereq] in prerequisites:
        max_course = max(max_course, course, prereq)

    adj = [ set() for _ in range(max_course + 1) ]
    adj_rev = [ set() for _ in range(max_course + 1) ]
    for [course, prereq] in prerequisites:
        adj[course].add(prereq)
        adj[prereq].add(prereq)

    needed = set()
    for i in range(numCourses):
        queue = deque([i])
        while queue:
            course = queue.popleft()
            if course not in needed:
                needed.add(course)
                for prereq in adj[course]:
                    queue.append(prereq)

    unsolved = copy.copy(needed)
    ans = []
    queue = deque([])
    for course in needed:
        if adj_rev[course] == []:
            queue.append(course)
            unsolved.remove(course)

    while queue:
        course = queue.popleft()
        ans.append(course)
        for next in adj_rev[course]:
            adj[next].remove(course)
            if adj[next] == {}:
                queue.append(next)
                unsolved.remove(next)

    return [] if unsolved else ans
