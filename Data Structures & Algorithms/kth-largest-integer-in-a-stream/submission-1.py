import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        #adds val to the stream
        #returns the kth largest integer in stream

        heapq.heappush(self.minHeap, val)

        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        return self.minHeap[0]



        
