# 合并2个升序数组

def merge(nums1, m, nums2, n):
    """
    Do not return anything, modify nums1 in-place instead.
    """
    k = m+n-1
    j = n-1
    i = m-1
    while j>=0 and i >=0:
        # print(j)
        if nums2[j]>= nums1[i]:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
        else:
            print('yes')
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
    nums1[:j+1] = nums2[:j+1]
    return nums1

if __name__ == "__main__":
    nums1 = [2,0]
    m = 1
    nums2 = [1]
    n = 1

    print(merge(nums1, m , nums2, n))
