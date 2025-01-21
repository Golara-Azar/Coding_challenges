class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if len(intervals)==1:
            return 1
        
        
        intervals.sort(key=lambda item: item[0]) #O(nlogn)
        
        from heapq import heapify, heappush, heappop 
  
        # Creating empty heap 
        heap = [] 
        heapify(heap) #O(1)
        num = 1
        heappush(heap,intervals[0][1]) #O(1)
        
        for item in intervals[1:]: #O(n)
            
            head = heappop(heap) #O(1)
            if item[0]>=head: #O(1)
                heappush(heap,item[1]) #O(Log n)
                continue
            else:
                num+=1
                heappush(heap,head) #O(Log n)
                heappush(heap,item[1]) #O(Log n)
            
            
        return num
        
        
"""
 time: O(nlogn)
 space: O(n)
 
"""       
                
                    
            
        
                
                
        
        
