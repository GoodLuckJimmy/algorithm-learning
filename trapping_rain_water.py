#투포인터
def trap(hight):
    if not hight:
        return 0

    volume = 0
    left, right = 0, len(hight) - 1
    left_max, right_max = hight[left], hight[right]

    while left < right:
        left_max, right_max = max(hight[left], left_max), max(hight[right], right_max)

        if left_max <= right_max:
            volume += left_max - hight[left]
            left += 1
        else:
            volume += right_max - hight[right]
            right -= 1

    return volume


input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(input))