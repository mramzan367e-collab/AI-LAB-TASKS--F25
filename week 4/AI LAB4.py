import heapq

g = {'S':[('A',1),('B',4)], 'A':[('C',2)],
     'B':[('G',5)], 'C':[('G',3)], 'G':[]}
h = {'S':5,'A':4,'B':4,'C':2,'G':0}

def search(astar):
    q = [(0,'S',0,['S'])]
    seen = []
    while q:
        _, n, cost, path = heapq.heappop(q)
        if n in seen:
            continue
        seen.append(n)
        if n == 'G':
            print(path, cost, seen, len(seen)-1)
            return
        for x,w in g[n]:
            c = cost+w
            heapq.heappush(q, (c+h[x] if astar else c, x, c, path+[x]))

search(True)   # A*
search(False)  # UCS