class Configuration:
    
    def __init__(self, range_a, range_b, population, bits, epochs_amount, best_and_tournament_chromo_amount, elite_strategy_amount, cross_probability, mutation_probability, inversion_probability, selection_method, cross_method, mutation_method, maximization):
        self.r_a = range_a
        self.r_b = range_b
        self.pop = population
        self.bts = bits
        self.ep_am = epochs_amount
        self.best_and_tour = best_and_tournament_chromo_amount
        self.elite = elite_strategy_amount
        self.cross = cross_probability
        self.mutation = mutation_probability
        self.inversion = inversion_probability
        self.sel_method = selection_method
        self.cross_method = cross_method
        self.muta_method = mutation_method
        self.maximization = maximization

    def __str__(self):
        return "Begin range: " + self.r_a + \
        " |End range: " + self.r_b + \
        " |Population amount: " + self.pop + \
        " |Number of bits: " + self.bts + \
        " |Epochs amount: " + self.ep_am + \
        " |Best and tournament chromosome amount: " + self.best_and_tour + \
        " |Elite Strategy amount: " + self.elite + \
        " |Cross probability: " + self.cross + \
        " |Mutation probability: " + self.mutation + \
        " |Inversion probability: " + self.inversion + \
        " |Selection method: " + self.sel_method + \
        " |Cross method: " + self.cross_method + \
        " |Mutation method: " + self.muta_method + \
        " |Maximization: " + str(self.maximization)