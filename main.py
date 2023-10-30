nums=list(map(int,input().split()))
nums.sort()  
triplets = []
for i in range(len(nums) - 2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue  
    left, right = i + 1, len(nums) - 1  
    target_sum = -nums[i]  
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target_sum:
            triplets.append([nums[i], nums[left], nums[right]])
            while left < right and nums[left] == nums[left + 1]:
                left += 1
            while left < right and nums[right] == nums[right - 1]:
                right -= 1
            left += 1
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
print(triplets)

