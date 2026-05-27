class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Use a set to omit duplicates
        s = set()
        # Loop through the list
        for num in nums:
            # Check if num is in the set
            if num in s:
                return True
            s.add(num)
        return False
