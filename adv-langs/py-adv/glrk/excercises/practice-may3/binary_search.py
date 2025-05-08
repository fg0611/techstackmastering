nums = [2, 5, 7, 8, 11, 12, 12]
target = 5

# search for a number inside this list
def b_search(input_list, n):
    left, right = 0, len(input_list) - 1

    while left < right:
        mid = (left + right) // 2

        if input_list[mid] == n:
            return mid, n
        elif n < input_list[mid]:
            right = mid-1
        elif n > input_list[mid]:
            left = mid+1
    return 'not found'

print(b_search(nums, target))