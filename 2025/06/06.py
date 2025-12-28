from functools import reduce
from itertools import groupby
#inputs=[list(x) for x in open("sample.txt") if x.strip()]
lst=[]
result=[]


inputs=[list(line.strip("\n")) for line in open("input.txt")]



rows=range((len(inputs)))
cols=range(len(inputs[0]))
nums=[]
stack=[]

op=[]

for col in cols:
    num=[]
    for row in rows: 
        n=inputs[row][col]
        num.append(n)
    
    #print(num[-1],num[:-1])
    op.append(num[-1])
    
    num="".join(num)
    stack.append(num)


last_idx=0
for x in range(len(stack)):
    if stack[x].strip()=="":
        lst.append(stack[last_idx:x])
        last_idx=x+1
if last_idx<len(stack):
   lst.append(stack[last_idx:len(stack)])
       
#print(lst)

for rw in range(len(lst)):
    #print("Found *" if "*" in lst[rw][0] else "Not found")
    if "*" in lst[rw][0]:
        rm_op=lst[rw][0]
        lst[rw][0]=rm_op[:-1]
        result.append(reduce(lambda x,y:x*y,map(int,lst[rw])))
        
    if "+" in lst[rw][0]:
        rm_op=lst[rw][0]
        lst[rw][0]=rm_op[:-1]
        result.append(reduce(lambda x,y:x+y,map(int,lst[rw])))


print("final sum is ",reduce(lambda x,y:x+y,result))


############### i know code is a mess but,finally learned a lot of thing such as map,reduce and lambda function 








#for col in range(len(inputs[0])):
#    #print(inputs[col])
#    for row in range(len(inputs)):
#        cols=inputs[row]
#        print(cols)
#
#        if all(not s.strip() for s in cols):
#            print("col is empty")
#        else:
#            print(" ")


#def rearg(lst):
#    num=[]
#    for i in range(len(lst[0])):
#       nm="".join(map(lambda s:s[i],lst))
#       num.append(nm)
#    return num 
#
#
#for col in range(len(inputs[0])):
#    for row in range(len(inputs)):
#        #print(inputs[row][col]) 
#        num=inputs[row][col] 
#        if "*" not in num and "+" not in num:
#           lst.append(num)
#        else:
#            lst=rearg(lst)
#            lst = [x.strip() for x in lst if x.strip()]
#            print(lst)
#            cal=reduce(lambda a,b:a+b,list(map(int,lst)))if "+" in num else reduce(lambda a,b:a*b,list(map(int,lst)))
#            print("cal",cal)
#            result.append(cal)
#            lst=[]
#




#print("result: ",reduce(lambda a,b:a+b,result))


# colum wise ##


#for col in range(len(inputs[0])):
#    for row in range(len(inputs)):
#        print(inputs[row][col])


#########    part-1 ###################

## col scan the 2d list
#rows = len(inputs)
#cols = len(inputs[0])
#
#for col in range(cols):
#    for row in range(rows):
#        print(inputs[row][col])

#for col in range(len(inputs[0])):
#    for row in range(len(inputs)):
#        print(inputs[row][col]) 
#        num=inputs[row][col] 
#        if num not in ("+","*"):
#           lst.append(num)
#        else:
#            cal=reduce(lambda a,b:a+b,list(map(int,lst)))if num =="+" else reduce(lambda a,b:a*b,list(map(int,lst)))
#            print("cal",cal)
#            result.append(cal)
#            lst=[]
#
#
#
#
#
#print("result: ",reduce(lambda a,b:a+b,result))

        





            
            
