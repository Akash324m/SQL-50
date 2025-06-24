class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for x in nums2:
            nums1.append(x)
        nums1.sort()
        arr_len = len(nums1)
        if arr_len%2 != 0:
            median=(arr_len-1)/2
            return nums1[median]
        else:
            index = arr_len/2
            median1=nums1[index]
            median2=nums1[index-1]
            result=(median1+median2)/2.0
            return result
        