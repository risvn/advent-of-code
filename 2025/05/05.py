

inputs = [line.strip() for line in open("sample.txt") if line.strip()]


fresh=[ list(ranges.split('-')) for ranges in inputs if '-' in ranges]
ingrnt_id=[ int(ranges) for ranges in inputs if '-' not in ranges]
#print(fresh,ingrnt_id)


#def is_fresh(fresh,id):
#    #for now using brute force i know it can be done better
#    global sum
#    lst=[]
#    for each_id in id:
#        for indx in range(len(fresh)):
#            if each_id in range(int(fresh[indx][0]),int(fresh[indx][1])+1):
#                #print(int(fresh[indx][0]),int(fresh[indx][1])+1)
#                #print(each_id)
#                lst.append(each_id)
#    return lst
#result=set(is_fresh(fresh,ingrnt_id))
#print(len(result))



def overlap(fresh):
    min_id=int(fresh[1][0])
    max_id=int(fresh[1][1])
    no_overlap=[]
    for item in range(len(fresh)):
        for indx in range(len(fresh)):
            range_min=int(fresh[indx][0])
            range_max=int(fresh[indx][1])
            #print(min_id,max_id,range_min,range_max)
            if max_id in range(range_min,range_max):
                #print("max:overlap")
                #print("old max_id:",max_id)
                max_id=max(min_id,max_id,range_min,range_max)
                #print("new max_id:",max_id)
            if min_id in range(range_min,range_max):
                #print("min:overlap")
                #print("old min:",min_id)
                min_id=min(min_id,max_id,range_min,range_max)
            
            if int(fresh[item][0]) not in range(min_id,max_id) and int(fresh[item][1]) not in range(min_id,max_id):
                no_overlap.append([int(fresh[item][0]),int(fresh[item][1])])
                
        print(min_id,max_id,no_overlap)
    return min_id,max_id,no_overlap



min_range,max_range,non_overlap=overlap(fresh)

##chat gpt said:  ;}
non_overlap = [list(x) for x in set(tuple(x) for x in non_overlap)]
fresh_items = sum((ids[1] - ids[0] + 1) for ids in non_overlap)+((max_range+1)-min_range)
print(fresh_items)

# TOO HIGH:404572467314799



#ingrn_id is irrelevent
#def part2(fresh_id):
#    lst=[]
#    for indx in range(len(fresh_id)):
#        lst=[x for x in (range(int(fresh[indx][0]),int(fresh[indx][1])+1))]
#        print(int(fresh[indx][0]),int(fresh[indx][1])+1)
# 
#    return lst
#
#result=part2(fresh)
#print(result)
#result=[x for lst in result for x in lst]
#total=set(result)
#print(len(total))

