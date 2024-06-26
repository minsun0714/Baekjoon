from sys import stdin as s

s = open("input.txt", "rt")  # 주석 처리해야 하는 부분
king, stone, n = map(str, s.readline().split())
n = int(n)

d = {'R': (0, 1), 'L': (0, -1), 'B': (-1, 0), 'T': (1, 0)}
king_x, king_y = int(king[1]) - 1, ord(king[0]) - 65
stone_x, stone_y = int(stone[1]) - 1, ord(stone[0]) - 65
for _ in range(n):
    move = s.readline().strip()
    king_nx, king_ny = king_x, king_y
    stone_nx, stone_ny = stone_x, stone_y

    for m in move:
        dx, dy = d[m]
        king_nx, king_ny = king_nx + dx, king_ny + dy

    if king_nx == stone_nx and king_ny == stone_ny:
        for m in move:
            dx, dy = d[m]
            stone_nx, stone_ny = stone_nx + dx, stone_ny + dy

    if 0 <= king_nx < 8 and 0 <= king_ny < 8 and 0 <= stone_nx < 8 and 0 <= stone_ny < 8:
        king_x, king_y = king_nx, king_ny
        stone_x, stone_y = stone_nx, stone_ny

print(chr(king_y + 65) + str(king_x + 1))
print(chr(stone_y + 65) + str(stone_x + 1))
