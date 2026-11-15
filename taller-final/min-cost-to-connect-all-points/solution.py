from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim sobre el grafo completo: crece un árbol desde el punto 0
        # y en cada paso agrega el punto más barato de conectar.
        n = len(points)
        INF = float("inf")

        best = [INF] * n      # costo mínimo para conectar cada punto al árbol actual
        in_tree = [False] * n
        best[0] = 0

        total = 0
        for _ in range(n):
            # Punto fuera del árbol con menor costo de conexión
            u = -1
            for i in range(n):
                if not in_tree[i] and (u == -1 or best[i] < best[u]):
                    u = i

            in_tree[u] = True
            total += best[u]

            # Actualizar costos de los puntos que quedan fuera, usando la distancia de Manhattan a u
            xu, yu = points[u]
            for v in range(n):
                if not in_tree[v]:
                    d = abs(points[v][0] - xu) + abs(points[v][1] - yu)
                    if d < best[v]:
                        best[v] = d

        return total
