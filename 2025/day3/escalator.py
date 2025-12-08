#converting int to the dict with index as keys
sum=0
result=[]
with open("sample.txt","r") as f:
    inputs= [line.strip() for line in f]




def digits(n):
    n = str(n)
    inx_dict = {i: int(n[i]) for i in range(len(n))}
    ls = [int(x) for x in n]
    return inx_dict, ls

def get_max(inx_dict,start,end):
    max_val=-1
    idx=None
    for x in range(start,end+1):
        if x in inx_dict:
            ## handle the edge case when to skip the same values and when to not 
            if max_val<=inx_dict[x] :
                max_val=inx_dict[x]
                idx=x 
    #print("index",idx,"max val : ",max_val)
    return idx 





def get_number(n,n_digits):
    inx_dict, ls = digits(n)
    ls_1 = ls[:]  # local copy
    indices=[]
    max_idx=-1
    while n_digits>0:
        range_max=max(inx_dict)
        range_min=max_idx
        
        if max_idx>=max(inx_dict):
            range_min=min(indices)
            print("first")
            if range_min>range_max:
                print("second")
                range_min=min(inx_dict)
                print(range_min) 
        print("range:",range_min,max(inx_dict))
        max_idx=get_max(inx_dict,range_min,range_max)
        print("index:",max_idx,"val :",inx_dict[max_idx])
        del inx_dict[max_idx]
        print(inx_dict)
        indices.append(max_idx)
         


        n_digits-=1 
    return indices,ls_1 


def inx_val(indices,ls):
    val=[]
    indices.sort()
    for x in indices:
        val.append(ls[x])
    num = int("".join(str(x) for x in val))
    return num 




#for n in inputs:
#    inx=get_number(n,12)
#    print(inx)
#    num=inx_val(inx)
#    result.append(num)
#    print(result)


for n in inputs:
    inx,ls=get_number(n,12)
    num=inx_val(inx,ls)
    sum+=int(num)
    result.append(num)
    print("for input: ",n,"largest num :",num,"\n")

print(sum)


#n='234234234234278'    
#inx,ls=get_number(n,12)
#num=inx_val(inx,ls)
#sum+=int(num)
#result.append(num)
#print("for input: ",n,"largest num :",num,"\n")

