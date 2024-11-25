def solution(candy_type: list[int]) -> int:
    number_candies = 0
    seen_candy = {}

    for candy in candy_type:
        if seen_candy.get(candy) == None:
            number_candies += 1
            seen_candy[candy] = 1

        if number_candies >= (len(candy_type) / 2):
            return number_candies
        
    return number_candies


output = solution([6, 6, 6, 6])
print(output)