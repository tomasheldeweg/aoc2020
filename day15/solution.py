input = [2, 0, 1, 7, 4, 14, 18]

def memory_game(input, target_turn):
    spoken_numbers = {val: turn for turn, val in enumerate(input, 1)}
    prev = input[-1]
    for turn in range(len(input) + 1, target_turn + 1):
        if prev in spoken_numbers and spoken_numbers[prev] != turn - 1:
            new = turn - 1 - spoken_numbers[prev]
            spoken_numbers[prev] = turn - 1
            prev = new

        else:
            spoken_numbers[prev] = turn - 1
            prev = 0

    return prev

# Solve 1
print(memory_game(input, 2020))

# Solve 2
print(memory_game(input, 30000000))