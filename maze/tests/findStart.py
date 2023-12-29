def check_repeats(matrix):
    counts = {}
    for row in matrix:
        for letter in row:
            if letter != "#" and letter != " " and letter != "E":
                if letter in counts:
                    counts[letter] += 1
                else:
                    counts[letter] = 1
                if counts[letter] > 1:
                    return "repeats"
    return "no repeats"

matrix = [['#', '#', '#', '#', '#', '#', '#', '#'], ['#', ' ', '#', 'r', '#', '#', '#', '#'], ['#', ' ', '#', ' ', '#', ' ', ' ', 'E'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', '#', ' ', '#', ' ', '#', '#'], ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#'], ['#', '#', '#', '#', '#', '#', '#', '#']]

print(check_repeats(matrix))