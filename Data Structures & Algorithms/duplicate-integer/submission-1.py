class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a hash set
        s = set()
        # Loop through all nums in the list
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

        #     for n in s:
        #     # Check if they equal each other
        #         if n == num:
        #             return True
        # return False