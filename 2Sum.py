from typing import List

def twoSum(nums, target):

    m={}
    for key, val in enumerate(nums):
        diff= target-val
        if diff in m:
            return[m[diff],key]
        m[val]=key
    return

if __name__=='__main__':
    nums=[1,2,5,6,7]
    print(twoSum(nums,13))

