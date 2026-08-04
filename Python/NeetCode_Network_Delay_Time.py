def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    visited = set()

    time_to_reach = [-1] * (n + 1)
    time_to_reach[k] = 0

    graph = [ [-1] * (n+1) for i in range(0, n + 1) ]
    for (src, tgt, weight) in times:
        graph[src][tgt] = weight

    def find_min_unvisited(time_to_reach, visited):
        min_time, min_node = float("infinity"), 0
        for i in range(1, n + 1):
            if time_to_reach[i] != -1 and \
               time_to_reach[i] < min_time and \
               i not in visited:
                min_time = time_to_reach[i]
                min_node = i

        return min_node

    next = find_min_unvisited(time_to_reach, visited)
    while next != 0:
        print(next, time_to_reach)

        visited.add(next)
        for neighbour in range(1, n + 1):
            edge = graph[next][neighbour]
            if edge != -1:
                time_to_reach[neighbour] = \
                    time_to_reach[next] + edge \
                    if time_to_reach[neighbour] == -1 \
                       else min(time_to_reach[neighbour], time_to_reach[next] + edge)
        next = find_min_unvisited(time_to_reach, visited)

    all_visited = True
    for i in range(1, n+1):
        all_visited = all_visited and time_to_reach[i] != -1
    return max(time_to_reach) if all_visited else -1
