def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col

    while j >= 0 and i < N:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True

def solve_n_queen_until(board,col,N,solutions):
    if col == N:
        solution=[]
        for i in range(N):
            row=[]
            for j in range(N):
                row.append(board[i][j])
            solution.append(row)
        solutions.append(solution)
        return 
    
    for i in range(N):
        if is_safe(board,i,col,N):
            board[i][col]=1
            solve_n_queen_until(board,col+1,N,solutions)
            board[i][col]=0

def solve_n_queen(N):
    board = [[0] * N for _ in range (N)]
    solutions=[]
    solve_n_queen_until(board,0,N,solutions)
    if len(solutions) == 0:
        print(" Not Possible ")
    else:
        for solution in solutions:
            for row in solution:
                for cell in row:
                    print("Q" if cell == 1 else ".", end=" ")
                print()
            print()

N=int(input("Enter no of queens: "))
solve_n_queen(N)

"""output
Enter no of queens: 4
. . Q . 
Q . . . 
. . . Q 
. Q . . 

. Q . . 
. . . Q 
Q . . . 
. . Q . 
"""
