from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get a counter for the list
        # count = Counter(nums)

        # 1 : 1
        # 2 : 2
        # 3 : 3
        # # Loop through nums list
        # for n in nums:
        #     for k, v in count.items():
        #         if k >= count[v]:

        # Hashmap for count of each value
        count = {}
        
        # Loop through the list
        for num in nums:
            # Add a count to the num value, default to 0 otherwise
            count[num] = 1 + count.get(num, 0)
        
        # Empty list
        stack = []
        # Loop through the number/counter in the hashmap and add them
        for num, cnt in count.items():
            stack.append([cnt, num])
            # Sort them at the end
        stack.sort()

        # Empty list
        res = []
        # Loop through the list if it's less than the length of k, pop the last value in the list
        # and append it to the new list
        while len(res) < k:
            res.append(stack.pop()[-1])
        return res