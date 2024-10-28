N, M = map(int,input().split())
dic = {x:x for x in range(0,N+1)}
# common parent : child
def find_stack(node):
    stack = [node]
    while stack:
        now = stack.pop()
        if dic[now] == now:
            dic[node] = now
            break
        stack.append(dic[now])

    # if dic[node] == node:
    #     return node
    # dic[node] = find(dic[node])
    return dic[node]


def find(node):
    # Start with the node itself
    root = node
    # Find the root of the node
    while dic[root] != root:
        root = dic[root]
    
    # Path compression: update all nodes on the path to point directly to the root
    while node != root:
        parent = dic[node]
        dic[node] = root
        node = parent
    
    return root


def union(node1, node2):
    node1_parent = find(node1)
    node2_parent = find(node2)
    dic[max(node1_parent,node2_parent)] = min(node1_parent,node2_parent)

def calc(node1,node2):
    return find(node1) == find(node2)

for i,a,b in [tuple(map(int, input().split())) for _ in range(M)]:
    
    if i == 0:
        union(a,b)
    else:
        print("YES" if calc(a,b) else "NO")
