def main():
    dir = 1  # 0=UP, 1=RIGHT, 2=DOWN, 3=LEFT

    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # UP  # RIGHT  # DOWN  # LEFT

    curent_position = [1, 1]  # start at 'o' for now (skipping auto-detect)

    maze = [
        ["*", "*", "*", "*", "*", "*", "*"],
        ["*", "o", " ", " ", " ", " ", "*"],
        ["*", " ", " ", "*", "*", "*", "*"],
        ["*", " ", " ", " ", " ", " ", "*"],
        ["*", "*", "*", "*", "*", "*", "*"],
    ]

    # Run until we stand on the exit
    while maze[curent_position[0]][curent_position[1]] != "x":

        # 1) Try RIGHT
        right_dir = (dir + 1) % 4
        rr = curent_position[0] + directions[right_dir][0]
        rc = curent_position[1] + directions[right_dir][1]

        if maze[rr][rc] != "*":
            dir = right_dir
            curent_position[0], curent_position[1] = rr, rc
            print("Moved RIGHT-turn to:", curent_position, "cell=", maze[rr][rc])
            continue

        # 2) Try FORWARD
        fr = curent_position[0] + directions[dir][0]
        fc = curent_position[1] + directions[dir][1]

        if maze[fr][fc] != "*":
            curent_position[0], curent_position[1] = fr, fc
            print("Moved FORWARD to:", curent_position, "cell=", maze[fr][fc])
            continue

        # 3) Try LEFT
        left_dir = (dir + 3) % 4
        lr = curent_position[0] + directions[left_dir][0]
        lc = curent_position[1] + directions[left_dir][1]

        if maze[lr][lc] != "*":
            dir = left_dir
            curent_position[0], curent_position[1] = lr, lc
            print("Moved LEFT-turn to:", curent_position, "cell=", maze[lr][lc])
            continue

        # 4) Otherwise, go BACK
        back_dir = (dir + 2) % 4
        br = curent_position[0] + directions[back_dir][0]
        bc = curent_position[1] + directions[back_dir][1]

        # In a valid maze, back should be possible here.
        if maze[br][bc] != "*":
            dir = back_dir
            curent_position[0], curent_position[1] = br, bc
            print("Moved BACK to:", curent_position, "cell=", maze[br][bc])
        else:
            print("Stuck at:", curent_position)
            return

    print("Exit found at:", curent_position)


if __name__ == "__main__":
    main()
