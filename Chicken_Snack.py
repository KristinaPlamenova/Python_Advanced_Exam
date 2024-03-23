n = int(input())
matrix = []
position = []
armour = 300
enemy_planes = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(n):
    matrix.append(input().split())

    if "J" in matrix[row]:
        position = [row, matrix[row].index("J")]
        matrix[row][position[1]] = "-"
    if "E" in matrix[row]:
        enemy_planes += 1

while armour != 0 or enemy_planes != 0:
    direction = input()
    row = position[0] + directions[direction][0]
    col = position[1] + directions[direction][1]

    position = [row, col]























