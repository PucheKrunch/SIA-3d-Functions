import numpy as np
from scipy.stats import norm

def roulette_wheel_selection(probabilities):
    p = np.random.uniform(0, sum(probabilities))
    for i in range(0, len(probabilities)):
        p -= probabilities[i]
        if p <= 0:
            return i

def ACO(f, f_range, no_max_iterations, no_ants, k, q, xi, n, plot):
    no_iterations, ranges, solutions_archive, colony = 0, [], np.zeros((k, n + 1)), np.zeros((no_ants, n + 1))
    for i in range(0, n):
        ranges.append(f_range)

    for i in range(0, k):
        for j in range(0, n):
            solutions_archive[i, j] = np.random.uniform(ranges[j][0], ranges[j][1])
        solutions_archive[i, -1] = f(solutions_archive[i, 0:n])
    solutions_archive = solutions_archive[solutions_archive[:, -1].argsort()]

    x = np.linspace(1, k, k)
    w = norm.pdf(x, 1, q * k)
    p = w / sum(w)

    function_values = []

    while no_iterations < no_max_iterations:
        means = solutions_archive[:, 0:n]
        for i in range(0, no_ants):
            potential_solution = roulette_wheel_selection(p)
            for coordinate in range(0, n):
                sigma_sum = 0
                for j in range(0, k):
                    sigma_sum += abs(solutions_archive[j, coordinate] - solutions_archive[potential_solution, coordinate])
                sigma = xi * (sigma_sum / (k - 1))

                colony[i, coordinate] = np.random.normal(means[potential_solution, coordinate], sigma)

                if not ranges[coordinate][0] <= colony[i, coordinate] <= ranges[coordinate][1]:
                    colony[i, coordinate] = np.random.uniform(ranges[coordinate][0], ranges[coordinate][1])

            colony[i, -1] = f(colony[i, 0:n])

        solutions_archive = np.append(solutions_archive, colony, axis=0)
        solutions_archive = solutions_archive[solutions_archive[:, -1].argsort()]
        solutions_archive = solutions_archive[0:k, :]

        function_values.append(solutions_archive[0][-1])

        no_iterations += 1

    return solutions_archive[0, 0:-1], solutions_archive[0][-1]


