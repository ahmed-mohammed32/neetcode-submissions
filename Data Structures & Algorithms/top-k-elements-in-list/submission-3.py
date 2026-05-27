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

        dic = {}
        for num in nums:
            dic[num] = 1 + dic.get(num, 0)

        # Sort keys by frequency (highest first)
        sorted_nums = sorted(dic, key=lambda x: dic[x], reverse=True)

        # Take the top k
        ans = sorted_nums[:k]
        return ans

            