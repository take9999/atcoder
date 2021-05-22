from scipy.sparse.csgraph import shortest_path
from scipy.sparse import csr_matrix

row = []
column = []
cost_data = []

tyouten, hen = map(int, input().split())
for _ in range(hen):
    f, t, cost = map(int, input().split())
    row.append(f)
    column.append(t)
    cost_data.append(cost)

g = csr_matrix((cost_data, (row, column)))
sp = shortest_path(g, indices=0)
print(sp)
