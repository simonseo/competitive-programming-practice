num_test_cases = int(input())

for _ in range(num_test_cases): 
    F = int(input()) # 친구 관계의 수 < 100,000
    graphs = []
    for _ in range(F):
        friendship = set(input().split())
        friend_graph = set([])
        for graph in graphs:
            if friendship.intersection(graph):
                if not friend_graph: # first graph
                    graph.update(friendship)
                else: # second graph
                    graph.update(friend_graph)
                    graphs.remove(friend_graph)
                friend_graph = graph
        if not friend_graph:
            friend_graph = friendship
            graphs.append(friend_graph)
        # print(len(friend_graph), friend_graph, graphs)
        print(len(friend_graph))
