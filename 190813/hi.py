snail = [[9,20,2,18,11],[19,1,25,3,21],[8,24,10,17,7],[15,4,16,5,6],[12,13,22,23,14]]

# [9,20,2,18,11]
# [19,1,25,3,21]
# [8,24,10,17,7]
# [15,4,16,5,6]
# [12,13,22,23,14]

new_snail = [[0]*5 for i in range(5) ]


dx = [1,0,-1,0]
dy = [0,1,0,-1]


# count = 1 ->  x축으로 +1
# count = 2 ->  y축으로 +1
# count = 3 ->  x축으로 -1
# count = 4 ->  y축으로 -1

if i == 5 or j ==5:
    count += 1


for i in range(0,25):
    min = i
    for j in range(0,24):
        direct_x = i + dx[]
