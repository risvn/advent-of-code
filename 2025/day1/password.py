def safe_dail(instruction,currentPos):
    direction=instruction[0]
    rotation = int(instruction[1:])  # convert to int

    if direction=="R":
        currentPos=(currentPos+rotation)%100
    else:
        currentPos=(currentPos-rotation)%100

    return currentPos




with open("input.txt", "r") as f:
    instructions = [line.strip() for line in f]


pos = 50
count = 0

for instruction in instructions:
    pos=safe_dail(instruction,pos)
    if pos==0:
        count+=1

print(count)



