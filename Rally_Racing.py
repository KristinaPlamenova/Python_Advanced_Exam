size = int(input())
racing_number = input()



matrix = []
for _ in range(size):
    matrix.append(input().split())

start_row, start_col = 0, 0
km = 0
result = ""
def moving(start_row, start_col,command):
    if command == "up":
        return start_row-1, start_col
    if command == "down":
        return start_row+1, start_col
    if command == "right":
        return start_row, start_col+1
    if command == "left":
        return start_row, start_col-1



while True:
    command = input()
    if command == "End":
        matrix[start_row][start_col] = "C"
        print(f"Racing car {racing_number} DNF.")
        print(f"Distance covered {km} km.")
        for row in matrix:
            result += ''.join(row) + '\n'
        print(result.strip())
        break

    row, col = moving(start_row, start_col, command)
    if 0 <= row < size and 0 <= col < size:
        start_col = col
        start_row = row
        if matrix[row][col] == ".":
            km += 10
        elif matrix[row][col] == "T":
            matrix[row][col] = "."
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] == "T":
                        row, col = i, j
                        start_row = row
                        start_col = col
                        matrix[i][j] = "."
                        km += 30
        elif matrix[row][col] == "F":
            km += 10
            matrix[row][col] = "C"
            print(f"Racing car {racing_number} finished the stage!")
            print(f"Distance covered {km} km.")
            for row in matrix:
                result += ''.join(row) + '\n'
            print(result.strip())
            break



