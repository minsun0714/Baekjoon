from sys import stdin as s
import sys
sys.setrecursionlimit(10**6)

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분

nodes = []
while True:
    try:
        nodes.append(int(s.readline()))
    except:
        break


def postorder(nodes):
    if not nodes:
        return
    root = nodes.pop(0)

    left, right = [], []

    for node in nodes:
        if node < root:
            left.append(node)
        else:
            right.append(node)

    postorder(left)
    postorder(right)
    print(root)


postorder(nodes)
