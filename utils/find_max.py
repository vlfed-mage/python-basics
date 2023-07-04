def find_max(nums):
    max_num = nums[0]
    for number in nums:
        if number > max_num:
            max_num = number
    return max_num
