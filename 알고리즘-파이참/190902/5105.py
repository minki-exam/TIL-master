import sys
sys.stdin = open('5105.txt', 'r')


def ispromising(maze, r, c, count):
    if maze[r][c] == 0:
        maze[r][c] = 1
        return 1
    elif maze[r][c] == 1:
        return 0
    elif maze[r][c] == 2:
        return 2
​

def find(maze, a, b, count):
    global N
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < N and 0 <= y < N:
            if maze[x][y] == 0:
                maze[x][y] = 1
                count += 1
                return find(maze, x, y, count)
            if maze[x][y] == 3:
                return count
    return 0


test_num = int(input())
for tc in range(test_num):
    N = int(input())
    count = 0
    maze = [list(map(int, input())) for _ in range(N)]
    print(maze)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                print(find(maze, i, j, 0))
