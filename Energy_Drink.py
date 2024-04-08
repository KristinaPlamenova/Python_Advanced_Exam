from collections import deque
drunk_caffeine = 0

miligrams_caffeine = list(map(int, input().split(", ")))
energy_drinks = deque(list(map(int, input().split(", "))))



while miligrams_caffeine and energy_drinks:
    multiply = miligrams_caffeine[-1] * energy_drinks[0]
    if multiply + drunk_caffeine <= 300:
        miligrams_caffeine.pop()
        energy_drinks.popleft()
        drunk_caffeine += multiply
    else:
        miligrams_caffeine.pop()
        energy_drinks.append(energy_drinks[0])
        energy_drinks.popleft()
        drunk_caffeine -= 30
        if drunk_caffeine < 0:
            drunk_caffeine = 0


if energy_drinks:
    print(f"Drinks left: {', '.join(map(str,energy_drinks))}")
else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {drunk_caffeine} mg caffeine.")
