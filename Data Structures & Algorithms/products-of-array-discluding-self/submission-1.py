class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] *len(nums)
        pro = 1
        for i in range(len(nums)):
            pre[i] = pro
            pro *= nums[i]

        pro = 1
        for i in range(len(nums)-1, -1, -1):
            suf[i] = pro
            pro *= nums[i]

        for i in range(len(pre)):
            suf[i] = suf[i] * pre[i]

        return suf
                
        