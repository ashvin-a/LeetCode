from typing import List 
def longestSubstring(s)-> bool:
    l=0
    result=0
    charset=set()
    for r in range(len(s)):
        while s[r] in charset:
            charset.remove(s[l])
            l+=1
        charset.add(s[r])
        result=max(result,r-l+1)
    return result

string='jjjjjjjjj'
print(longestSubstring(string))


