<<<<<<< HEAD
import sys
sys.stdin = open('5178.txt', 'r')


def traversal(N):




for tc in range(int(input())):
    N, M, L = map(int, input().split())
    tree = [0] + list(map(int, input().split()))
    n = len(ls)
=======
# import sys
# sys.stdin = open("input_5178.txt", "r")
# def nodes_sum(node):
#     global n, m
#     if node < n - m + 1:
#         nodes_sum(node * 2)
#         nodes_sum(node * 2 + 1)
#         if node * 2 < n + 1:
#             nodes[node] += nodes[node * 2]
#         if node * 2 + 1 < n + 1:
#             nodes[node] += nodes[node * 2 + 1]
# T = int(input())
# for tc in range(T):
#     n, m, l = map(int, input().split())
#     data = [list(map(int, input().split())) for _ in range(m)]
#     nodes = [0] * (n + 1)
#     for i in data:
#         node, value = i[0], i[1]
#         nodes[node] = value
#     tree = [[0] * 2 for _ in range(n + 1)]
#     nodes_sum(1)
#     print("#{} {}".format(tc + 1, nodes[l]))
ls = [6,7,'+',2,3]
map(int, ''.join(ls))
>>>>>>> bfa3c05ab17be4efe1fc72a5a5df311cae4cfd77
