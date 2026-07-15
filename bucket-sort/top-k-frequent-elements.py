import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for key in nums:
            hashmap[key] = hashmap.get(key, 0) + 1

        poriority_queue = []
        for ke in hashmap.keys():
            heappush(poriority_queue, (hashmap[ke], ke))
            if len(poriority_queue) > k:
                heappop(poriority_queue)
        return [key for freq, key in poriority_queue]

