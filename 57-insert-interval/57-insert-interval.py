# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        i, output = 0, []
        
        # Append non-overlapping intervals on the left side before newInterval starts
        while i < n and intervals[i][1] < newInterval[0]:
            output.append(intervals[i])
            i += 1
        
        # Merge overlapping intervals (update start/end if needed, append merged newInterval when interation ended)
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i += 1
        output.append(newInterval)
        
        # Append remaining non-overlapping intervals on the right side 
        while i < n:
            output.append(intervals[i])
            i += 1
            
        return output
      
      