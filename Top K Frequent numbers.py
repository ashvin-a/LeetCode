from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
        
        count={}
        freq=[[] for i in range(len(nums))]
        for num in nums:
            count[num]= 1+count.get(num,0)#Counts no of times a number occured 
        for num,c in count.items():
            freq[c].append(num)#Attaches the number to the no. of times it occured

        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res
              

if __name__=='__main__':
     print(topKFrequent([0,0,0,0,1,6,1,2,2,6,2,6,2,6,6,6,6,66,6,6,6,6,6,6,6,6,7,8,65,456,243,5,34,5,2,2,2,2,2,2],5))
