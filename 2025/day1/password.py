zc=0
rc=0
def safe_dail(instruction,currentPos):
    global zc
    global rc 
    direction=instruction[0]
    rotation = int(instruction[1:])  # convert to int

    if direction=="R":
        oldPos=currentPos
        currentPos=(currentPos+rotation)%100
        
        #track total rotations
        wrapcount=rotation//100
        extra=rotation%100
        zc+=wrapcount
        if currentPos!=0 and currentPos<oldPos:
            zc+=1
    else:
        
        oldPos=currentPos
        currentPos=(currentPos+(100-rotation))%100
        wrapcount=rotation//100
        extra=rotation%100
        extra=100-extra
        zc+=wrapcount

        #idont know how but it works the logic seems different for R and L in IF condition 
        if oldPos!=0 and currentPos>oldPos:
            zc+=1

    #wrapcount=rotation//100
    #extra=rotation%100
    #zc+=wrapcount
    #if extra+currentPos>100:
    #    zc+=1
        

    return currentPos




with open("input.txt", "r") as f:
    instructions = [line.strip() for line in f]


pos = 50
count = 0

for instruction in instructions:
    pos=safe_dail(instruction,pos)
    if pos==0:
        count+=1
print(f"zero count :{count}")
print(f"zero crosses:{zc}")
print(f"password:{count+zc}")


