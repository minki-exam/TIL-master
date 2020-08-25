import heapq


def solution(food_times, k):
    # (음식 크기, 원판에서의 위치) 로 food_times 재정의
    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    print(food_times)
    # heapify. 음식 크기가 작은 순으로 뽑아낸다.
    heapq.heapify(food_times)
    print(food_times)
    # 가장 크기 작은 음식
    small_food = food_times[0][0]
    prev_food = 0
    # 작은 음식을 완전히 소비하기 위해 원판을 완주할 수 있는 경우
    while k - ((small_food - prev_food) * len(food_times)) >= 0:
        # 해당 음식을 완전히 소비하는 데 걸린 시간만큼 뺀다
        k -= (small_food - prev_food) * len(food_times)
        prev_food, index = heapq.heappop(food_times)
        if not food_times:
            return -1
        small_food = food_times[0][0]
    food_times = sorted(food_times, key=lambda x: x[1])
    # print(food_times)
    return food_times[k % len(food_times)][1]

print(solution([3,1,2], 5 ))



class Tree:
    def __init__(self,dataList):
        self.data=max(dataList,key=lambda x :x[1])
        leftList =list(filter(lambda x :x[0] < self.data[0] , dataList))
        rightList = list(filter(lambda x :x[0] > self.data[0] , dataList))

        if leftList != []:
            self.left=Tree(leftList)
        else :
            self.left=None
        if rightList != []:
            self.right=Tree(rightList)
        else :
            self.right=None

def fix(node,postList,preList):
    postList.append(node.data)
    if node.left is not None:
        fix(node.left,postList,preList)
    if node.right is not None:
        fix(node.right,postList,preList)
    preList.append(node.data)