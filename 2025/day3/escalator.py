#converting int to the dict with index as keys
ls=[]
result=[]
sum=0

with open("input.txt","r") as f:
    inputs= [line.strip() for line in f]




print(inputs)

def digits(n):
    n=int(n)
    dg={}
    index=len(str(n))-1
    global ls
    ls=[]
    while index>=0:
        dg[n%10]=index
        ls.append(n%10)
        n//=10
        index-=1
    ls=ls[::-1]
    return dg 


#gets the max digit from the given list
def get_elements(n):
    n_dict=digits(n)
    sorted_ls=sorted(ls,reverse=True)

    index_ls=[n_dict[sorted_ls[0]],n_dict[sorted_ls[1]]]
    index_ls.sort()
    if ls[index_ls[0]]>ls[index_ls[1]] or index_ls[1]==len(ls)-1:
        print(str(ls[index_ls[0]])+str(ls[index_ls[1]]) ,index_ls,n)
        return result.append((str(ls[index_ls[0]])+str(ls[index_ls[1]])))
    else:
        first_dg=ls[index_ls[1]]
        sliced_ls=ls[index_ls[1]+1:]
        max=sliced_ls[0]
        for i in sliced_ls:
            if max<i:
                max=i
        print(first_dg,max)
        return result.append(str(first_dg)+str(max))




for i in range(len(inputs)):
    get_elements(inputs[i])


for i in range(len(result)):
    sum+=int(result[i])

print(result)
print(sum)

            
        
        

        


























