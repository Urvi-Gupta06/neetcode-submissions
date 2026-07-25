class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''count = {} #hashmap
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            count[i]= 1 + count.get(i,0) #zero is the default here if i hasn't been seen yet
        
        for i,c in count.items():
            freq[c].append(i)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res'''


        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # push (-frequency, number) so the "smallest" negative = highest frequency
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)   # O(m) — this is the heapify we discussed earlier

        result = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)   # O(log m) each
            result.append(num)

        return result