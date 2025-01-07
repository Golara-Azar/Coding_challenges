class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if intervals==[]:
            return [newInterval]


        if newInterval[1]<intervals[0][0]:
            return [newInterval]+intervals
        

        res = []
        i = 0
        l,r = intervals[i][0],intervals[i][1]
        a,b = newInterval[0],newInterval[1]

        while r<a:
                #not reached the new interval yet
                res.append([l,r])
                i+=1
                if i==len(intervals):
                    return res + [[a,b]]
                l,r = intervals[i][0],intervals[i][1]
                
                
        
        if b<l:
            res.append([min(l,a),b])
            

        elif b<=r: #the new interval is contained in one interval
            
            res.append([min(l,a),r])
            i+=1

        else: # we have multiple overlaps
            
            
            while i<len(intervals):
                # scenario 1:
                # b is smaller than the beginning of the next interval
                # we add [l,b] and move on to the next interval by incrementing i
                if b<intervals[i][0]:
                    
                    res.append([min(a,l),b])
                    break
                
            
                # scenario 2:
                # b is inside the next interval
                # we keep l where it is, but update r to be the end of next interval, and add that
                elif b<intervals[i][1]:
                    
                    r = intervals[i][1]
                    res.append([min(a,l),r])
                    i+=1
                    break
                    

                # scenario 3:
                # b completely covers next interval
                # keep l where it is, increment i and check right side again
                else:
                    
                    i+=1
                    if i==len(intervals):
                        res.append([min(a,l),b])
                        break
                    r = intervals[i][1]
                    continue


        while i<len(intervals):
            l,r = intervals[i][0],intervals[i][1]
            res.append([l,r])
            i+=1
        return res

"""
Time: O(n) since we go over all intervals once
Space: O(n) to keep the resulting intervals

"""


