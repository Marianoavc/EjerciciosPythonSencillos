#method that verifies if a queen can be placed in a certain position
def if_valid(row, col, queens):
    for r in range(row):
        #if the queen is in the same column or in the same diagonal
        if col == queens[r] or abs(row - r) == abs(col - queens[r]):
            return False
    return True

#method that places the queens in the board
def n_queens(row, queens, n):
    if row == n:
        print(queens)
        return 1
    else:
        count = 0
        for col in range(n):
            if if_valid(row, col, queens):
                queens[row] = col
                #recursive call
                count += n_queens(row + 1, queens, n)
        return count    
    
def NReinas(n):
    queens = [0] * n
    row = 0
    print( n_queens(row, queens, n))

NReinas(5)