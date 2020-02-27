class Solution:
    def twoSum(self, nums, target):
        idxDict = dict()
        idx_list = []
        for idx, num in enumerate(nums):
            if target - num in idxDict:
                idx_list.append([idxDict[target - num], idx])
            idxDict[num] = idx
        return idx_list

    def threeSum1(self, num):
        num.sort()
        res = set()
        result = []
        for i in range(len(num) - 2):
            if (i == 0 or num[i] > num[i - 1]) and num[i] <= 0:
                left = i + 1
                result_idx = self.twoSum(num[left:], -num[i])
                for each_idx in result_idx:
                    each_result = tuple([num[i], num[each_idx[0] + (i + 1)], num[each_idx[1] + (i + 1)]])
                    res.add(each_result)
        for value in res:
            result.append(value)
        return result

    def threeSum(self, nums):
        nums.sort()
        res = set()
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    res.add((v, -v - x, x))
        return map(list, res)


print Solution().threeSum([-1, 0, 1, 2, -1, -4])
