from collections import deque

tools = deque(map(int, input().split()))
substances = list(map(int, input().split()))
challenges = list(map(int, input().split()))



while len(challenges) > 0:
    if tools and substances:

        multiply = tools[0] * substances[-1]
        if multiply in challenges:
            tools.popleft()
            substances.pop()
            challenges.remove(multiply)
        else:
            tools[0] += 1
            tools.append(tools[0])
            tools.popleft()

            substances[-1] -= 1
            if substances[-1] == 0:
                substances.pop()

    else:
        print("Harry is lost in the temple. Oblivion awaits him.")
        if tools:
            print(f"Tools: {', '.join(map(str, tools))}")
        if substances:
            print(f"Substances: {', '.join(map(str, substances))}")
        if challenges:
            print(f"Challenges: {', '.join(map(str, challenges))}")
            break

else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
    if tools:
        print(f"Tools: {', '.join(map(str, tools))}")
    if substances:
        print(f"Substances: {', '.join(map(str, substances))}")
    if challenges:
        print(f"Challenges: {', '.join(map(str, challenges))}")



