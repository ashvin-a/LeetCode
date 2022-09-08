from collections import Counter

s="anagram"
t="nafgram"
# dict1=Counter(s)
# dict2=Counter(t)
# print(dict1,dict2)
count1,count2={},{}
for i in range(len(s)):
    count1[s[i]]=1+count1.get(s[i],0)
print(count1)
