import sys, math

input = sys.stdin.readline


def init_tree(arr, tree, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    else:
        mid = (start + end) // 2
        tree[node] = init_tree(arr, tree, node * 2, start, mid) + init_tree(arr, tree, node * 2 + 1, mid + 1, end)
        return tree[node]


def sub_sum(tree, node, start, end, left, right):
    if end < left or start > right:
        return 0
    elif left <= start and end <= right:
        return tree[node]
    else:
        mid = (start + end) // 2
        return sub_sum(tree, node * 2, start, mid, left, right) + sub_sum(tree, node * 2 + 1, mid + 1, end, left, right)


def update(tree, node, start, end, index, diff):
    if index < start or end < index:
        return
    else:
        tree[node] += diff

        if start != end:
            mid = (start + end) // 2
            update(tree, node * 2, start, mid, index, diff)
            update(tree, node * 2 + 1, mid + 1, end, index, diff)


if __name__ == "__main__":
    N, Q = map(int, input().split())

    arr = [0] + list(map(int, input().split()))

    height = math.ceil(math.log(N, 2) + 1)
    tree = [0] * (2 ** height)

    init_tree(arr, tree, 1, 1, N)

    for _ in range(Q):
        x, y, a, b = map(int, input().split())

        if x > y:
            x, y = y, x

        print(sub_sum(tree, 1, 1, N, x, y))

        update(tree, 1, 1, N, a, b - arr[a])
        arr[a] = b
