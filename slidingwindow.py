# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组。如果不存在符合条件的连续子数组，返回 0。
#
# 示例:
#
# 输入: s = 7, nums = [2,3,1,2,4,3]
# 输出: 2
# 解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

def solver(nums, s):
    optim = len(nums) + 1
    for start in range(len(nums)):
        summation = 0
        for end in range(start, len(nums)):
            summation += nums[end]
            if summation >= s:
                optim = min(optim, end - start + 1)
                break
    return optim
