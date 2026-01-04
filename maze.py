def main():
 
    dir  = 1
    
    directions = [(-1,0),#up
                  (0,1), #right
                  (1,0),#down
                  (0,-1) #left
                  ]
    curent_position = list((1,1))
    # maze=[maze_row1,maze_row2,maze_row3, maze_row4,maze_row5]
    maze =[['*', '*', '*', '*', '*'],['*', 'o', '*', 'x', '*'],['*', ' ', ' ', ' ', '*'],['*', '*', '*', '*', '*']]
   
    right_dir = (dir+1)%4
    new_row = curent_position[0]+directions[right_dir][0]
    print(new_row)
    
    new_col = curent_position[1]+directions[right_dir][1]
    # print(maze[curent_position[0]][curent_position[1]])
   
    print(new_col)
    
    while maze[new_row][new_col]!='x':
        right_dir = (dir+1)%4
        new_row = curent_position[0]+directions[right_dir][0]
        print(new_row)
    
        new_col = curent_position[1]+directions[right_dir][1]
        if maze[new_row][new_col]!='*':
            dir =   right_dir
            curent_position[0] = new_row
            curent_position[1]= new_col
            print(maze[curent_position[0]][curent_position[1]])
            right_dir = (dir+1)%4
            new_row = curent_position[0] + directions[right_dir][0]
            new_col = curent_position[1] + directions[right_dir][1]
           
        elif maze[new_row][new_col]=='*':
             print(maze[curent_position[0]][curent_position[1]])
             return
    # for row in maze:
    #     print(row)
    
    
    

if __name__ == "__main__":
    main()
