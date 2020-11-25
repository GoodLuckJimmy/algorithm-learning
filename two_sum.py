# 타겟에서 첫 번째 값을 뺀 값(target -n)이 존재하는지 탐색
def towSum1(nums, target):
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


#한번에 찾기
def towSum2(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        nums_map[num] = i

    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]

#한번에 찾기 개선. 성능은 비슷
# 전체를 모두 저장하는 부분이 없다
def towSum3(nums, target):
    nums_map = {}
    for i, num in enumerate(nums):
        if target - num in nums_map:
            return [nums_map[target - num], i]
        nums_map[num] = i

#투포인터로 구현(정렬된 nums에 한해)
def twoSum4(nums, target):
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]

arr = [2, 7, 11, 15]
print(twoSum4(arr, 9))



