
def Encode(strs):
    res=[]
    res.append(str(len(strs))+"#"+strs)
    return res                            


def Decode(strs):
    answer,i=[],0
    while i<len(strs):
        j=i
        while strs[j]!='#':
            j+=1
        length=int(strs[i:j])    
        answer.append(strs[j+1:j+1+length])
        i=j+1+length
    return answer
if __name__=='__main__':
    print(Decode('9#melloetta'))



