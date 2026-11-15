import heapq
from collections import defaultdict
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Grafo dirigido y ponderado: u -> (v, w)
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        # Dijkstra desde k: dist guarda los nodos ya cerrados con su distancia final.
        dist = {}
        heap = [(0, k)]  # (distancia tentativa, nodo)

        while heap:
            d, u = heapq.heappop(heap)
            if u in dist:
                continue  # ya se cerró con una distancia menor
            dist[u] = d
            for v, w in graph[u]:
                if v not in dist:
                    heapq.heappush(heap, (d + w, v))

        # Si algún nodo no fue alcanzado, la señal nunca llega a todos
        if len(dist) < n:
            return -1

        # Hay que esperar al nodo que más tarda
        return max(dist.values())
