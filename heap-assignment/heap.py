import heapq

heap = [20,40,30,40]
heapq.heapify(heap)
heapq.heappush(heap,50)
heapq.heappop(heap)
largestElement = heapq.nlargest(1,heap)[0]
print(heap)
print(largestElement)

heap3 = ["Mary","Caren","Zippy"]
heapq.heapify(heap3)
heapq.heappop(heap3)
print(heap3)
heapq.heappush(heap3,"Tracy")
print(heap3)


