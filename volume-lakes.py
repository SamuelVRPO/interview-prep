def solution(island):
    total_volume = 0
    l_high = 0
    r_high = 0
    valley = 0

    while l_high < len(island) or r_high < len(island):
        if island[idx] > island[l_high]:
            l_high = idx


solution([1, 3, 2, 4, 1, 3, 1, 4, 5, 2, 2, 1, 4, 2, 2])
