from typing import List
def Longest(nums:List[int]):
    array_set=set(nums)
    longest=0
    for num in nums:
        while num-1 not in array_set:
            length=1
            if num+length in array_set:
                length+=1
            longest=max(longest,length)
    return longest
if __name__=='__main__':
    print(Longest([3,4,7,8,1,9]))