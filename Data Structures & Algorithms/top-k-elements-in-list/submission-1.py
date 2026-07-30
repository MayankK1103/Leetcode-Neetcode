from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        result = []
        # num with freq as values
        for num in nums:
            num_freq[num] += 1
        # Build Min Heap
        heap = []
        for key in num_freq:
            heapq.heappush(heap, (-num_freq[key], key))
        # Add k most frequent elements to result 
        print(heap)
        while k > 0:
            freq, number = heapq.heappop(heap)
            result.append(number)
            k -= 1  
        return result