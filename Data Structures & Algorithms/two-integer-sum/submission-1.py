class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Empty hash map
        hash_map = {}
        # Loop through the list
        for i, v in enumerate(nums):
            # Initialize the difference of the target and the list value
            diff = target - v
            # Check if the difference of the target and the list value is in 
            # the hash map. Return the indencies of the diff and value if found
            if diff in hash_map:
                return [hash_map[diff], i]
            # Add the index to the value in the hash map
            hash_map[v] = i
