

inputs = [line.strip() for line in open("input.txt") if line.strip()]


fresh=[ list(ranges.split('-')) for ranges in inputs if '-' in ranges]
ingrnt_id=[ int(ranges) for ranges in inputs if '-' not in ranges]
print(fresh,ingrnt_id)


def is_fresh(fresh,id):
    #for now using brute force i know it can be done better
    global sum
    lst=[]
    for each_id in id:
        for indx in range(len(fresh)):
            if each_id in range(int(fresh[indx][0]),int(fresh[indx][1])+1):
                #print(int(fresh[indx][0]),int(fresh[indx][1])+1)
                #print(each_id)
                lst.append(each_id)
    return lst




result=set(is_fresh(fresh,ingrnt_id))

print(len(result))

