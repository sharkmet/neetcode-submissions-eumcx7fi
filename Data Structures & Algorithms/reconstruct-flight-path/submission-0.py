import heapq
from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj[airport] = min-heap of destinations from that airport.
        # Heap lets us always pop the lex-smallest next destination in O(log n).
        adj = defaultdict(list)
        for src, dst in tickets:
            heapq.heappush(adj[src], dst)
        
        # Final itinerary, but built in REVERSE order during DFS.
        result = []
        
        def dfs(airport):
            # Keep flying out of `airport` until no tickets remain.
            while adj[airport]: # whiles loop never runs if it is a dead end so it just appends
                # Pop the smallest available destination — this "uses" the ticket.
                next_airport = heapq.heappop(adj[airport])
                # Recurse: explore everything reachable from next_airport first.
                dfs(next_airport)
            # No more tickets out of `airport` → it's a dead end from here.
            # Add it to result NOW (post-order). This is the Hierholzer trick.
            result.append(airport)
            # DFS naturally writes them in this right-to-left order because of when it appends — after all deeper work is done.
        
        dfs("JFK")
        # We built result back-to-front, so reverse it for the real itinerary.
        return result[::-1]


# Two scenarios:
# You picked a "throwaway" loop first (one that returns to the current airport). It runs, comes back, and the current airport still has tickets left.
# The loop's airports get appended in the middle of the result. Then you continue with the remaining tickets.
# You picked the "final" branch first (the one that leads to the dead end). It dives all the way to the dead end and 
# appends from the bottom up. When it returns, the current airport has no tickets left, so it appends itself right after.
# The reversal at the end reorders these correctly either way:

# Loops appended "in the middle" end up in the middle of the forward itinerary (correct — you take the loop, return, continue).
# The dead-end branch, appended first, ends up last in the forward itinerary (correct — that's where the trip ends).

# And the heap ensures that whenever you have a choice, you take the lex-smallest one first. If that choice happens to be a loop, great, you
# take it now and come back. If it happens to be the dead-end branch, also fine — you'll just descend immediately, and any other branches don't 
# exist (because if they did, the heap would've offered them too and you'd have picked something else).
# The algorithm doesn't need to "know" which is which. The post-order append + reverse handles both cases identically.