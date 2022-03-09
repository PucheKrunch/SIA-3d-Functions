import random
import numpy as np
from aco import ACO
from michalewicz import MICHALEWICZ, OPSEG_MICHALEWICZ

def find_statistics(functionValues):
    print("Best", min(functionValues))
    print("Worst", max(functionValues))
    print("Mean", np.mean(functionValues))
    print("Std", np.std(functionValues))

def main(n, chromosome_length, no_iterations, population_size, no_executions, plot=False):
    P = generate_p(n)
    micha_aco = []

    x, f_x = ACO(MICHALEWICZ, OPSEG_MICHALEWICZ, no_iterations, population_size, 50, 0.0001, 0.5, n, plot)
    micha_aco.append(f_x)

    print('------------------------------------------------------------------------')

    print('ACO')
    print('Michalewicz:')
    find_statistics(micha_aco)

    print('------------------------------------------------------------------------')


def generate_p(n):
    W = [0.8] * n
    C1 = []
    for i in range(0, n):
        C1.append(random.uniform(0, 1.47))

    C2 = []
    for i in range(0, n):
        C2.append(random.uniform(0, 1.47))

    return [W, C1, C2]


if __name__ == '__main__':

    main(2, 20, 50, 20, 30)
