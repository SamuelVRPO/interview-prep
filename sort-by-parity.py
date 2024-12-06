def solution(nums: list[int]) -> list[int]:
    sorted_nums = [0] * len(nums)
    even = 0
    odd = len(nums) - 1

    for num in nums:
        if num % 2 == 0:
            sorted_nums[even] = num
            even += 1
        elif num % 2 != 0:
            sorted_nums[odd] = num
            odd -= 1

    return sorted_nums


print(solution([0]))
