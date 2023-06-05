def min_product_sum(nums1, nums2):
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    min_product_sum = 0

    for i in range(n):
        min_product_sum += nums1[i] * nums2[n - 1 - i]

    return min_product_sum
nums1 = [5, 3, 4, 2]
nums2 = [4, 2, 2, 5]

print(min_product_sum(nums1, nums2))
