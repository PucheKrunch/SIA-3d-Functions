# ABC Function
def artificial_bee_colony_optimization(food_sources = 3, iterations = 50, min_values = [-5,-5], max_values = [5,5], employed_bees = 3, outlookers_bees = 3, limit = 3, target_function = target_function, verbose = True): 
    count = 0
    best_value = float("inf")
    sources = initial_sources(food_sources = food_sources, min_values = min_values, max_values = max_values, target_function = target_function)
    fitness = fitness_function(sources)
    while (count <= iterations):
        if (count > 0):
            if (verbose == True):
                print('Iteration = ', count, ' f(x) = ', best_value)    
        e_bee = employed_bee(sources, min_values = min_values, max_values = max_values, target_function = target_function)
        for i in range(0, employed_bees - 1):
            e_bee = employed_bee(e_bee[0], min_values = min_values, max_values = max_values, target_function = target_function)
        fitness = fitness_function(e_bee[0])          
        o_bee = outlooker_bee(e_bee[0], fitness, e_bee[1], min_values = min_values, max_values = max_values, target_function = target_function)
        for i in range(0, outlookers_bees - 1):
            o_bee = outlooker_bee(o_bee[0], fitness, o_bee[1], min_values = min_values, max_values = max_values, target_function = target_function)
        value = np.copy(o_bee[0][o_bee[0][:,-1].argsort()][0,:])
        if (best_value > value[-1]):
            best_solution = np.copy(value)
            best_value    = np.copy(value[-1])       
        sources = scouter_bee(o_bee[0], o_bee[1], limit = limit, target_function = target_function)  
        fitness = fitness_function(sources)
        count = count + 1   
    return best_solution

############################################################################