inputs=[list(line.strip("\n")) for line in open('input.txt') ]
result=0



def beam_spliter(idx,lst):
    global result
    if idx==len(inputs):
        return inputs


    
    n_lst=set()
    for x in lst:
        if inputs[idx][x]=='^':
            result=result+1
            inputs[idx][x+1]='|'
            inputs[idx][x-1]='|'
            n_lst.add(x+1)
            n_lst.add(x-1)
        else: 
            inputs[idx][x]='|'
            n_lst.add(x)
    if not n_lst:
       n_lst=set(lst)


            
    return beam_spliter(idx+1,list(n_lst))



ini=[x for x in range(len(inputs[0])) if inputs[0][x]=='S']
beam_spliter(1,ini)



for x in inputs:
    print(x)
print(result)
