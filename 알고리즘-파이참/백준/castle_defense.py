from itertools import combinations
from copy import deepcopy


def possible_attack(arch, enemy, kill):
    global d
    cnt = 0

    for ar in arch:
        for ene in enemy:
            if ene[0] >= 0:
                if (abs(ar[0]-ene[0])+abs(ar[1] - ene[1])) <= d:

                    ene[0] = -1
                    kill += 1
                    cnt += 1
                    if cnt == 3:
                        return kill, enemy

    else:
        return kill, enemy



n, m, d = map(int, input().split())
d= d-1
arr = [list(map(int, input().split())) for _ in range(n)]
arr_attack = [[0]*m for _ in range(n)]
enemy = []

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            enemy.append([i, j])


enemy_num = len(enemy)
archers = [i for i in range(m)]


max_val = 0
archer = []
dxdy = [(1, 0), (0, -1), (0, 1)] # (-1,0)은 필요없다.

# 공격이 먼저 시작 그러고 나서 움직인다.



for k in combinations(archers, 3): # 궁수 위치 선정
    for i in k:
        archer.append((0, i))

    move_cnt = 0
    kills = 0
    try_enemy = deepcopy(enemy)

    while move_cnt < n:
        kills, try_enemy = possible_attack(archer, try_enemy, kills)

        for ene in try_enemy:
            if ene[0] == -1:
                pass
            else:
                ene[0] -= 1
        move_cnt += 1
    if kills > max_val:
        max_val = kills


    kills = 0
    archer = []  # 마지막에 다시 원점으로 돌리다.
print(max_val)

# ////////////////////////////////////////////////////////////////////////////////////

from itertools import combinations
from copy import deepcopy
import sys

N, M, D = map(int, sys.stdin.readline().split())
# 적군의 위치를 저장하는 set
enemy_position = set()
for y in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    for x in range(M):
        if arr[x] == 1:
            enemy_position.add((y, x))

maps = [[0 for _ in range(M)] for _ in range(N)]
# 궁사의 위치. map의 가장 하단이므로 (N, 0) ~ (N, M-1) 총 M개의 위치가 있다.
archor_position = [(N, i) for i in range(M)]

# M개의 위치 중 3개를 골라 궁사를 배치하는 모든 경우의 수
candidates = combinations(archor_position, 3)


# 궁사 위치별로 사격 가능한 적군 거리를 계산하는 함수.
# 궁사 세 명의 각 위치당 사격 가능한 좌표, 좌표까지의 거리를 계산한다.
def get_distance(maps, candidate, D):
    possible_attack_area = []
    for position in candidate:
        copied = []
        for y in range(len(maps)):
            for x in range(len(maps[0])):
                if abs(position[0] - y) + abs(position[1] - x) <= D:
                    copied.append((abs(position[0] - y) + abs(position[1] - x), y, x))
        possible_attack_area.append(copied)
    return possible_attack_area


# 적군이 전진하는 함수
def go_forward(enemy_position, N):
    return set([(y + 1, x) for y, x in enemy_position if y + 1 < N])


# 공격 가능한 '가장 가까운 적'을 찾는 함수.
# 거리가 가까운 순서, x값이 작은 순서로 공격 가능한 위치를 정렬하고,
# y, x축이 적군이 있는 좌표값이면 좌표값을 리턴한다.
def find_nearest_enemy(arc, enemy_position):
    arc.sort(key=lambda x: (x[0], x[2]))
    for dist, y, x in arc:
        if (y, x) in enemy_position:
            return (y, x)
    return None


maxs = 0
for archors in candidates:
    arc = get_distance(maps, archors, D)
    kills = 0
    # 각 경우의 수마다 적 위치는 초기화해야 하므로 deepcopy 사용
    copy_enemy_map = deepcopy(enemy_position)
    while enemy_position:
        temp = set()
        for arc_map in arc:
            kill = find_nearest_enemy(arc_map, enemy_position)
            if kill is not None:
                temp.add(kill)
        # 공격한 적의 좌표 개수만큼 kill 상승
        kills += len(temp)
        # 공격한 적의 좌표는 남은 적군의 위치에서 삭제한다.
        enemy_position -= temp
        # 적군의 위치를 전진시킨다.
        enemy_position = go_forward(enemy_position, N)

    enemy_position = copy_enemy_map
    if maxs < kills:
        maxs = kills
print(maxs)

