def solution(coins: list[int], amount: int) -> int:
    total = 0
    num_coins = 0

    coins.sort()
    for it in range(len(coins)-1, -1, -1):
        while total + coins[it] <= amount:
            total = total + coins[it]
            num_coins += 1
        
        if total == amount: return num_coins

    return -1
    


#result = solution([1, 2, 5], 11)
#result = solution([1], 0)
#result = solution([2], 3)
#result = solution([2, 5, 10, 1], 27)
result = solution([186, 419, 83, 408], 6249)
print(result)