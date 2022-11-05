# Chronological Ordering | Sorting and two pointers

# Time complexity : O(nlogn)
# Space complexity : O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        
        start = sorted([ i[0] for i in intervals])
        end = sorted([ i[1] for i in intervals])
        
        res = 0 # whatever the max we have reached
        count = 0
        
        # two pointers
        sp = 0
        ep = 0
        
        while(sp < len(intervals)):
            if start[sp] < end[ep]:
                sp += 1
                count += 1
            else:
                ep += 1
                count -= 1
            res = max(res, count)
        
        return res
                
                
                
        
        
        