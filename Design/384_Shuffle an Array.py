class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)
        print id(self.array), id(self.original)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.array

    def shuffle(self):
        for i in range(len(self.array)):
            swap_idx = random.randrange(i, len(self.array))
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array

a = Solution([1,2,3])
print a.shuffle()
print a.reset()