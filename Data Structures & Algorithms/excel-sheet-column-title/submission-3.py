class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        '''
            1-26 indices -> convert to 0-based 
            subtract 1 from column number 
            do % 26
            build right -> left

            27-1 = 26%26 = 0 = A -> A
            26//26 = 1 -> update column number 

            1-1 = 0%26 = 0 = A -> A
            0//26 = 0 -> stop
            A,A -> reverse to AA
        '''
        title = []
        while columnNumber>0:
            columnNumber-=1
            rem = columnNumber%26
            title.append(chr(ord('A') + rem))
            columnNumber //= 26

        title.reverse()
        return "".join(title)
