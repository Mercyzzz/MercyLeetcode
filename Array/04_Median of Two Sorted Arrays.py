class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        length1 = len(nums1)
        length2 = len(nums2)
        k = (length1 + length2) // 2
        if (length1 + length2) % 2 == 0:
            return (self.findK(nums1, nums2, k) + self.findK(nums1, nums2, k - 1)) / 2.0  # 2 is enough in python3
        else:
            return self.findK(nums1, nums2, k)

    def findK(self, nums1, nums2, k):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        if k == 0:
            return min(nums1[0], nums2[0])
        mid1 = len(nums1) // 2
        mid2 = len(nums2) // 2
        if nums1[mid1] > nums2[mid2]:
            if k > mid1 + mid2:
                return self.findK(nums1, nums2[mid2 + 1:], k - mid2 - 1)
            else:
                return self.findK(nums1[:mid1], nums2, k)
        else:
            if k > mid1 + mid2:
                return self.findK(nums1[mid1 + 1:], nums2, k - mid1 - 1)
            else:
                return self.findK(nums1, nums2[:mid2], k)


print Solution().findMedianSortedArrays([1, 3], [2])
