class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''First attempt: 1st case worked, 2nd failed
            It would return True the first time it found the same character'''
        # 2 loops - 1 for each string
        # Loop through each and check if it's in the other
        # Return True if all characters are in the other's string
        # Return False if not
        # for i in s:
        #     for j in t:
        #         if i in t:
        #             return True
        # return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            return True
        else:
            return False