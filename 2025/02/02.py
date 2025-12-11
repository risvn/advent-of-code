##problem:find the invalid ids from the given range with pattern matching that made with twice or trice


with open("input.txt", "r") as f:
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
def check(lis,offset):
    i=1
    while i*offset<len(lis):
        if lis[:offset]!=lis[i*offset:(i+1)*offset]:
            return False
        i+=1
    return True



def part2(num):
    lis=digits(num)
    if len(lis)>=2 and lis[:1]==lis[-1:]:
        return check(lis,1)
    if len(lis)%2==0 and len(lis)>=4 and lis[:2]==lis[-2:]:
        offset=2
        return check(lis,offset)
    if len(lis)%3==0 and len(lis)>=6 and lis[:3]==lis[-3:] :
        offset=3
        return check(lis,offset)

    if len(lis)%4==0 and len(lis)>=8 and lis[:4]==lis[-4:]:
        offset=4
        return check(lis,offset)
    return False





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
