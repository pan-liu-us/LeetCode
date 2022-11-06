# Brute Force
# Time complexity: O(N + NlogN) 
# count the frequency of each word in O(N),use sorting O(NlogN)
# Space complexity: O(N) 
# store frequencies in a HashMap and return a slice from a sorted list

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        cnt = Counter(words)
        
        # define a sort key
        def sort_key(x):
            return (-cnt[x], x) # first sort by frequcy, then sort by the word itself

        return sorted(list(cnt.keys()), key=sort_key)[:k] # key=lambda x: (-cnt[x], x)