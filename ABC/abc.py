import numpy as np

# ABCO
from pyMetaheuristic.algorithm import artificial_bee_colony_optimization
from pyMetaheuristic.utils import graphs

def eggholder(variables_values = [0, 0]):
    x1, x2     = variables_values
    func_value = - (x2 + 47)*np.sin(np.sqrt(abs( (x1/2) + x2 + 47))) - x1*np.sin(np.sqrt(abs( x1 - (x2 + 47))))
    return func_value

# Target Function - Values
plot_parameters = {
    'min_values': (-512, -512),
    'max_values': (512, 512),
    'step': (5, 5),
    'solution': [],
    'proj_view': '3D',
    'view': 'notebook'
}
graphs.plot_single_function(target_function = eggholder, **plot_parameters)

# ABCO - Parameters
parameters = {
    'food_sources': 20,
    'min_values': (-512, -512),
    'max_values': (512, 512),
    'iterations': 100,
    'employed_bees': 20,
    'outlookers_bees': 20,
    'limit': 20,
    'verbose': True
}

# ABCO - Algorithm
abco = artificial_bee_colony_optimization(target_function = eggholder, **parameters)