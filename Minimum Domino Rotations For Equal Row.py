# Time complexity: O(n)
# Space complexity: O(1)
# Approach: assume that, the value to be updated is with tops[0] or bototms[0] if not, then making all the values of top or bottoms equal is not possible.
# start by keeping the target as tops[0] and check for rotations, if its -1, 
# check by keeping target as bottoms[0] and check for roations.
# to check for rotations, traverse the elements from index 0 to n-1
# if both top and bottom at i are not equal to target, then return -1 since not possible to make all equal
# if element at top[i] is alone not equal to target, then it means we have tto rotate top with bottom, so toprotation++
# if element at bottom[i] is alone not equal to target, then it means we have to rotate the bottom with top, swo bottom rotation++
# return min(toprotation, bottomrotation)


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops)== 0 and len(bottoms) == 0:
            return 0
        value = self.getrotations(tops, bottoms, tops[0])
        if value != -1:
            return value
        else:
            return self.getrotations(tops, bottoms, bottoms[0])
        
    def getrotations(self, tops, bottoms, target):
        toprotation = 0
        bottomrotation = 0
        for i in range(len(tops)):
            if tops[i] != target and bottoms[i] != target:
                return -1
            elif tops[i] != target:
                toprotation += 1
                
            elif bottoms[i] != target:
                bottomrotation += 1
                
        return min(toprotation, bottomrotation)
            
            
            
        