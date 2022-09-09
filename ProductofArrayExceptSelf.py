
from typing import List
def Productof(nums:List[int]):
    result=[1]*len(nums)
    prefix=1
    for i in range(len(nums)):
        result[i]=prefix
        prefix = prefix*nums[i]
    postfix=1
    for i in range(len(nums)-1,0,-1):
        result[i]=result[i]*postfix
        postfix= postfix*nums[i]
    return(result)
if __name__=='__main__':
    print(Productof([1,2,3,4]))

