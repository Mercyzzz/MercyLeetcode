class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        k -= 1
        factorial = 1
        for i in range(1, n):
            factorial *= i

        result = []
        array = list(range(1, n + 1))
        for i in range(n - 1, 0, -1):
            index = k // factorial
            result.append(str(array[index]))
            array = array[:index] + array[index + 1:]
            k %= factorial
            factorial //= i
        result.append(str(array[0]))
        return "".join(result)

print Solution().getPermutation(3, 6)
