def get_solutions(perimiter: int) -> int:
    # c^2 = a^2 + b^2
    # a^2 + b^2 = a^2 + b^2
    # c = (a^2 + b^2)^(1/2)
    # (a^2 + b^2)^(1/2) = (a^2 + b^2)^(1/2)

    solutions = []

    perimiter = int(perimiter / 2)

    for a in range(1, perimiter):
        rest_perimiter = perimiter - a
        a_root = a**2
        for b in range(1, rest_perimiter):
            c = (a_root + (b**2)) ** (1 / 2)
            if a + b + c == perimiter:
                solution = {a, b, c}
                if not solution in solutions:
                    solutions.append(solution)
                    break

    return len(solutions)


MAX_PERIMITER = 10**3

max_solutions = 0
max_perimiter = 0

for p in range(1, MAX_PERIMITER):
    total_solutions = get_solutions(p)
    if total_solutions > max_solutions:
        max_solutions = total_solutions
        max_perimiter = p

print(max_perimiter)
