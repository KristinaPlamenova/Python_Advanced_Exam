from collections import deque

armour = deque([int(x) for x in input().split(",")])
soldier_impact = [int(x) for x in input().split(",")]

killed_monsters = 0

while armour and soldier_impact:
    copy_armour = armour.popleft()
    soldier_copy = soldier_impact.pop()

    if soldier_copy >= copy_armour:
        soldier_copy -= copy_armour
        killed_monsters += 1

        if soldier_impact:
            soldier_impact[-1] += soldier_copy
        elif not soldier_impact and soldier_copy > 0:
            soldier_impact.append(soldier_copy)

    else:
        copy_armour -= soldier_copy
        armour.append(copy_armour)


if len(armour) == 0:
    print("All monsters have been killed!")

if not soldier_impact:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {killed_monsters}")


