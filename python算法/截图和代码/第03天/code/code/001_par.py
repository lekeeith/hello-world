def partition(nums):
    pivot = nums[0]
    return [i for i in nums[1:] if i < pivot] + [pivot] + [i for i in nums[1:] if i >= pivot]

def quick_sort(nums):
    if len(nums) <= 1:
        return nums
    pivot = nums[0]
    left = [num for num in nums[1:] if num <= pivot]
    right = [num for num in nums[1:] if num > pivot]
    return quick_sort(left) + [p] + quick_sort(right)

if __name__ == '__main__':
    nums = [4, 3, 1, 2, 7, 8, 5]
    result = partition(nums)
    print(result)

    res = quick_sort(nums)
    print(res)