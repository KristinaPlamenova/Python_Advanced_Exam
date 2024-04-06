from collections import deque
count_vader = 0
count_thor = 0
count_big_blue = 0
count_small = 0
time_for_task = deque(map(int, input().split()))
number_of_tasks = list(map(int, input().split()))

while time_for_task and number_of_tasks:
    multiply = time_for_task[0] * number_of_tasks[-1]
    if 0 <= multiply <= 60:
        count_vader += 1
        time_for_task.popleft()
        number_of_tasks.pop()
    elif 61 <= multiply <= 120:
        count_thor += 1
        time_for_task.popleft()
        number_of_tasks.pop()
    elif 121 <= multiply <= 180:
        count_big_blue += 1
        time_for_task.popleft()
        number_of_tasks.pop()
    elif 181 <= multiply <= 240:
        count_small += 1
        time_for_task.popleft()
        number_of_tasks.pop()

    if multiply > 240:
        number_of_tasks[-1] -= 2
        time_for_task.append(time_for_task[0])
        time_for_task.popleft()

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {count_vader}\nThor Ducky: {count_thor}\nBig Blue Rubber Ducky: {count_big_blue}\nSmall Yellow Rubber Ducky: {count_small}"
)