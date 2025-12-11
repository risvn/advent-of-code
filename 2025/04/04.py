
grid= [list(line.strip()) for line in open("input.txt")]
       
adj_8= [
    [-1, -1],  # top-left
    [-1,  0],  # top
    [-1,  1],  # top-right
    [ 0, -1],  # left
    [ 0,  1],  # right
    [ 1, -1],  # bottom-left
    [ 1,  0],  # bottom
    [ 1,  1],  # bottom-right
]




def find(row,col):
    count=0
    for adj in adj_8:
        adj_row=row+adj[0]
        adj_col=col+adj[1]
        #print(f"row:{row},col:{col},adj_row:{adj_row},adj_col:{adj_col}")
        if (adj_row>=0 and adj_row<len(grid)) and (adj_col>=0 and adj_col<len(grid[0])):
            #print(f"row_len:{len(grid)},col_len:{len(grid[0])},row:{row},col:{col},adj_row:{adj_row},adj_col:{adj_col}")
            if grid[adj_row][adj_col]=='@':
                #print("found",adj_row,adj_col,grid[adj_row][adj_col])
                count+=1
    return count

#TODO: '@' can be repalce with 'x' for now it servers no purpose
result=0
new_grid = [row[:] for row in grid]

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col]=='@':
            count=find(row,col)
            #print(row,col,grid[row][col],count)
            if count<4:
                new_grid[row][col]='x'

                result+=1
                #print(row,col,grid[row][col],count)


#for row in range(len(new_grid)):
#    print(new_grid[row])


        

print("result: ",result)
