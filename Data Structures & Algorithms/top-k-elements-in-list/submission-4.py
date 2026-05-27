class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Get a counter for each number in the list
        # {1: 1
        #  2: 2
        #  3: 3}
        # Compare the values to k. If the value is greater than or equal to k, add it's respected 
        # key to an empty list.
        # Return the new list at the end

        # dic = {}
        # ans = []

        # for num in nums:
        #     dic[numn] = 1 + dic.get(num, 0)
        # for v in dic.values():
        #     if dic.values() == k:
        #         ans.append(dic[nums[i]])
        # return ans

        # Counter for the freq of each number in a hashmap
        counter_count = {}

        for num in nums:
            counter_count[num] = 1 + counter_count.get(num, 0)

        # Sort the numbers in reverse order
        sorted_nums = sorted(counter_count, key = lambda x: counter_count[x], reverse = True)
        # Get the 'k' most frequent element
        k_most = sorted_nums[:k]

        return k_most

            