class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Dijkstra greedily finalizes the cheapest-known path to each node. But here we have a constraint on number of stops. 
        # The cheapest path to some intermediate node might use too many stops to be useful, while a more expensive path uses 
        # fewer stops and is the only way to reach dst within k stops.
        prices = [float("inf")] * n
        prices[src] = 0
        
        # k stops = k + 1 edges, so do k + 1 rounds
        for _ in range(k + 1):
            # Snapshot prices into tmp at the start of each round.
            # Two things this gives us:
            #   1) tmp accumulates the best 1-edge extensions found this round,
            #      so multiple flights into the same v can compete and the cheapest wins.
            #   2) Reads of prices[u] below are FROZEN at last round's values, so we
            #      can't chain edges within a single round — each round adds exactly
            #      one more edge of reach. Without this, edge order could let one
            #      round walk 2, 3, or more hops at once, breaking the k-stop limit.
            tmp = prices.copy()   # snapshot of last round's prices, prices holds last rounds, tmp holds changes made this round
            for u, v, w in flights:
                if prices[u] == float("inf"): # READ from prices (frozen)
                    continue
                if prices[u] + w < tmp[v]: # so that we compare with the updated value, so we only ever add ONE edge
                    tmp[v] = prices[u] + w
                    #Net effect over the full round: tmp[v] ends up holding min(prices[v], cheapest 1-edge extension into v). 
            prices = tmp  # at end of round, prices catches up
        
        return prices[dst] if prices[dst] != float("inf") else -1