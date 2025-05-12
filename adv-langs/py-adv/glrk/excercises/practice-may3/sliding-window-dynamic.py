# sub arreglo que de X

arr = [2, 3, 2, 5, 1, 5]
x = 8


def subarr_eq_x(nums, goal):
    if not isinstance(nums, list) or not nums:
        return None

    end = 0
    current_sum = 0

    for i in range(len(nums)):
        while end < len(nums) - 1 and current_sum < goal:
            end += 1
            current_sum += nums[end]
        if current_sum == goal:
            return nums[i : end + 1]
        current_sum -= nums[i]
    return None

print(subarr_eq_x(arr, x))

def find_subarr_eq_x(nums, goal):
    if not isinstance(nums, list) or not nums:
        return None
    if nums[0] == goal:
        return nums[:1]
    current_sum = nums[0]
    start = 0
    end = 0
    i = 0

    while i < len(nums):
        if current_sum == goal:
            break
        if current_sum < goal:
            end += 1
            current_sum += arr[end]
        if current_sum > goal:
            current_sum -= nums[start]
            start += 1
        i += 1
    if current_sum != goal:
        return None
    return arr[start : end + 1]


print(find_subarr_eq_x(arr, x))
