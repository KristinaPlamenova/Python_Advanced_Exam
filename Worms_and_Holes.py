
worms = list(map(int, input().split()))
holes = list(map(int, input().split()))

matches = 0



while worms and holes:
    current_worm = worms[-1]
    current_holes = holes[0]
    if current_worm == current_holes:
        worms.pop()
        holes.pop(0)
        matches += 1

    else:
        worms[-1] -= 3
        if worms[-1] <= 0:
            worms.pop()
        holes.pop(0)


if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if len(worms) == 0:
    print("Every worm found a suitable hole!")
else:
    print(f"Worms left:{', '.join(map(str, worms))}")
if holes:
    print(f"Holes left: {', '.join(map(str, holes))}")
else:
    print("Holes left: none")





















