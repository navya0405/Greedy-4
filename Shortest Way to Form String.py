# Time Complexity:O(s * t) where s is length of source string and t is length of target string
# Space Complexity:O(1)


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        sCursor = 0
        tCursor = 0
        count = 0

        #   iterate until the target cursor reaches the end
        while (tCursor < len(target)):

            #   keep note of the index in target cursor
            currentTargetCursor = tCursor

            #   iterate through the source cursor
            while (sCursor < len(source) and tCursor < len(target)):
                if (source[sCursor] == target[tCursor]):
                    sCursor += 1
                    tCursor += 1
                else:
                    sCursor += 1

            #   if the target cursor doesn't move forward => new char found => return -1
            if (currentTargetCursor == tCursor):
                return -1

            #   after inner iteration of source cursor => increment count and reset source cursor
            count += 1
            sCursor = 0

        #   return count
        return count
        