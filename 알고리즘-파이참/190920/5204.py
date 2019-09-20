import sys
sys.stdin = open('5204.txt', 'r')


def merge_sorted(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]


        l = merge_sorted(left)
        r = merge_sorted(right)
        return merge(l, r)
    else:
        return arr


def merge(left, right):
    global cnt
    if left[-1] > right[-1]:
        cnt += 1
    i = 0
    j = 0
    arr = []

    while (i < len(left)) & (j < len(right)):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1

        else:
            arr.append(right[j])
            j += 1

    while (i < len(left)):
        arr.append(left[i])
        i += 1


    #
    while (j < len(right)):
        arr.append(right[j])
        j += 1



    return arr


for tc in range(1, int(input())+1):
    N = int(input())
    ls = list(map(int, input().split()))
    cnt = 0
    ls2 = merge_sorted(ls)
    print('#%d %d %d' %(tc, ls2[N//2], cnt))

