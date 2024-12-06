def knapSackRecur(i, capacity, val):
    if i == len(val):
        return 0
    
    take = 0
    if val[i] <= capacity:
        take = val[i] + knapSackRecur(i, capacity - val[i], val)

    noTake = knapSackRecur(i + 1, capacity, val)

    return max(take, noTake)


def knapSack(capacity, val):
    return knapSackRecur(0, capacity, val)


solution = knapSack(11, [1, 2, 5])

print(solution)