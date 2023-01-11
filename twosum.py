def twosum(nums, target):
    index = 0
    while index < len(nums):
        for i in range(len(nums[:index])):
            print(i)
            if target == nums[index]+ nums[i]:
                return [i, index]
        index += 1

nums = [8, 7, 1, 2,9, 10]
target = 9
print(nums)
print(twosum(nums,target))
            
