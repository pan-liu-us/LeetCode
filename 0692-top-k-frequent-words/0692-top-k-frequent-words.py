# MaxHeap

# Time complexity: O(klogN)
# count the frequency of each word in O(N)
# heapify the list of unique words in O(N) time
# each time we pop the top from the heap, it costs O(logN) time as the size of the heap is O(N)
# Space complexity: O(N) 
 
from collections import Counter
from heapq import nsmallest

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        return nsmallest(k, cnt.keys(), key=lambda x: (-cnt[x], x))