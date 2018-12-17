# A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

# Given N, write a function to return the number of knight's tours on an N by N chessboard.

def numKnightsTours(n):
    squares = [(i, j) for i in range(n) for j in range(n)]
    numTours = 0
    def recurse(currSquare, visited):
        nonlocal numTours
        if all([all([val == 1 for val in row]) for row in visited]):
            numTours += 1
            print(numTours)
            return
        moves = ((2,1), (-2,1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2))
        for move in moves:
            dx, dy = move
            x, y = currSquare
            xNew = x+dx
            yNew = y+dy
            if xNew >= 0 and xNew < n and yNew >= 0 and yNew < n and visited[xNew][yNew] != 1:
                # gotta deep copy our visited matrix so different recursive calls aren't using the same object. . . 
                # dat memory footprint . . . yikes
                newVisited = [[val for val in row] for row in visited]
                newVisited[xNew][yNew] = 1
                recurse((xNew, yNew), newVisited)
    # try starting from every possible square
    for startingSquare in squares:
        visited = [[0 for _ in range(n)] for _ in range(n)]
        visited[startingSquare[0]][startingSquare[1]] = 1
        recurse(startingSquare, visited)
    return numTours

print(numKnightsTours(5))


