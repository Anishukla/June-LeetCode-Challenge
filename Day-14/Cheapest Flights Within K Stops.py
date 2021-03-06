class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        graph = defaultdict(list)
        deque_vert = deque([[src, 0, 0]])
        min_price = float('inf')
     
        for i, j, w in flights: 
            graph[i].append([j, w])

        while deque_vert:
            city, visited, price = deque_vert.popleft()

            if price <= min_price and visited <= k and city != dst:
                for neibh, price_neibh in graph[city]:
                     deque_vert.append([neibh, visited + 1, price + price_neibh])
            
            if city == dst:
                min_price = min(min_price, price)
                
        if min_price != float('inf'):
            return min_price 
    
    
        else:
            return -1
