import heapq
class MedianFinder:

    def __init__(self):
        self.small = [] #maxheap - we want to take the max out for median
        self.large = [] #minheap - we want to take the min out for median  

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num) #-1 so that maxheap

        #make sure every elem in small <= every elem in large
        if (self.small and self.large and (-1*(self.small[0]))>self.large[0]):
            val= -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        
        #uneven size (diff bw len >1)
        if len(self.small) > len(self.large)+1:
            heapq.heappush(self.large,-1 * heapq.heappop(self.small))

        if len(self.large) > len(self.small)+1:
            heapq.heappush(self.small,-1*heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small)==len(self.large):
            return ((-1*self.small[0])+self.large[0])/2
        if len(self.small) > len(self.large):
            return -1* self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]



