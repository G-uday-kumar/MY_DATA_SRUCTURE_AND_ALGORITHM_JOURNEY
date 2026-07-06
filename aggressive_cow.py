def canPlace(stalls, cows, distance):
    count = 1
    last = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last >= distance:
            count += 1
            last = stalls[i]
            if count == cows:
                return True
    return False
def aggressiveCows(stalls, cows):
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    ans = 0
    while low <= high:
        mid = (low + high) // 2
        if canPlace(stalls, cows, mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans
if __name__ == "__main__":
    stalls = [1, 2, 4, 8, 9, 12]
    cows = 4
    print(aggressiveCows(stalls, cows))