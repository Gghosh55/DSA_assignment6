def find_max_length(nums):
    max_length = 0
    count = 0
    count_map = {0: -1}

    for i in range(len(nums)):
        count += 1 if nums[i] == 1 else -1

        if count in count_map:
            subarray_length = i - count_map[count]
            max_length = max(max_length, subarray_length)
        else:
            count_map[count] = i

    return max_length
nums = [0, 1]

print( find_max_length(nums))
