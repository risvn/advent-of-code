##problem:find the invalid ids from the given range with pattern matching that made with twice or trice


with open("sample.txt", "r") as f:
    inputs = f.read().strip().split(",")

def create_range(inrange):
    inrange=[int(x) for x in inrange.split('-')]
    return list(range(inrange[0],inrange[1]+1))


def digits(n):
    dg=[]
    while n>0:
        dg.append(n%10)
        n//=10
    return dg[::-1] # reverse the list

def part2(num):
    lis=digits(num)

    
    offset=len(lis)//3 
  #  if offset==1:
  #     return lis[:offset]==lis[offset:2*offset]==lis[2*offset:3*offset]  
  #  
  #  if offset==2:
  #     return lis[:offset]==lis[offset:2*offset]==lis[2*offset:3*offset]  
  #  if offset==3:
    if offset !=0:
      return lis[:offset]==lis[offset:2*offset]==lis[2*offset:3*offset]  
     
   
#use get_invds by passing list of nums not use pattern_match directly
def pattern_match(num):
    lis=digits(num)
    mid=len(lis)//2
    return lis[:mid]==lis[mid:] or part2(num)

def get_invds(nums):
    #nums is list
    inv_ids=[]
    for i in range(len(nums)):
        if pattern_match(nums[i]):
            inv_ids.append(nums[i])
    return inv_ids

lol_ids=[]
for i in range(len(inputs)):
    nums=create_range(inputs[i])
    lol_ids.append(get_invds(nums))
flat=[x for sub in lol_ids for x in sub]
print(flat)
sum=0
for x in range(len(flat)):
    sum+=flat[x]
print(sum);
print(part2(2121212121))
