# N은 정점 M은 간선 V는 시작할 지점
N,M,V = map(int, input().split())

graph = [[0]*(N+1) for _ in range(N+1)]

for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

# 방문 리스트
visited1 = [0]*(N+1)
visited2 = visited1.copy()

def dfs(V):
    # 방문 처리 
    visited1[V] = 1
    print(V,end=' ')

    # dfs 알고리즘 
    for i in range(1,N+1):
        # 해당 정점 사이의 간선이 있으며 방문하지 않는 노드일 경우 
        if graph[V][i] == 1 and visited1[i] == 0:
            dfs(i)

def bfs(V):
    # 방문 처리 
    queue = [V]
    visited2[V] = 1

    # bfs 알고리즘
    while queue:
        # 큐에 있는 노드 제거 
        V = queue.pop(0) 
        print(V,end=' ')

        for i in range(1,N+1):
             # 해당 정점 사이의 간선이 있으며 방문하지 않는 노드일 경우 
            if graph[V][i] == 1 and visited2[i] == 0:
                queue.append(i)
                visited2[i] = 1

dfs(V)
print()
bfs(V)
