from functools import reduce
inputs=[list(x.split()) for x in open("input.txt") if x.strip()]

operations=inputs[-1]
data=inputs[:-1]
lst=[]
result=[]


for x in inputs:
    print(x)

## col scan the 2d list
#rows = len(inputs)
#cols = len(inputs[0])
#
#for col in range(cols):
#    for row in range(rows):
#        print(inputs[row][col])

for col in range(len(inputs[0])):
    for row in range(len(inputs)):
        print(inputs[row][col]) 
        num=inputs[row][col] 
        if num not in ("+","*"):
           lst.append(num)
        else:
            cal=reduce(lambda a,b:a+b,list(map(int,lst)))if num =="+" else reduce(lambda a,b:a*b,list(map(int,lst)))
            print("cal",cal)
            result.append(cal)
            lst=[]





print("result: ",reduce(lambda a,b:a+b,result))

        





            
            
