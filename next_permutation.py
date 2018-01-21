class Solution(object):
    def pIndex(self, nums):
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i+1]:
                break
            i -= 1
        return i
    
    def qIndex(self, nums, p):
        i = p
        while i+1 < len(nums):
            if nums[p] >= nums[i+1]:
                break
            i += 1
        return i
    
    def swap(self, nums, p, q):
        n = nums[p]
        nums[p] = nums[q]
        nums[q] = n
        
    def reverse(self, nums, begin, end):
        i = 0
        while i < (end-begin+1)/2:
            self.swap(nums, begin+i, end-i)
            i += 1
            
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        p = self.pIndex(nums)
        if p < 0:
            self.reverse(nums, 0, len(nums)-1)
        else:
            q = self.qIndex(nums, p)
            self.swap(nums, p, q)
            self.reverse(nums, p+1, len(nums)-1)
        

