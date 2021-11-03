class Configuration:
    # defining
    def __init__(self, range_a, range_b, population, bits, epochs_amount, best_and_tournament_chromo_amount, elite_strategy_amount, cross_probability, mutation_probability, inversion_probability, selection_method, cross_method, mutation_method, maximization):
        self.range_a = int(range_a)
        self.range_b = int(range_b)
        self.population = int(population)
        self.bits = int(bits)
        self.epochs_amount = epochs_amount
        self.best_and_tournament_chromo_amount = float(best_and_tournament_chromo_amount)
        self.elite_amount = elite_strategy_amount
        self.cross_probability = cross_probability
        self.mutation_probability = mutation_probability
        self.inversion_probability = inversion_probability
        self.selection_method = selection_method
        self.cross_method = cross_method
        self.mutation_method = mutation_method
        self.maximization = bool(maximization)
    # listing of results
    def __str__(self):
        return "Begin range: " + self.range_a + \
        " |End range: " + self.range_b + \
        " |Population amount: " + self.population + \
        " |Number of bits: " + self.bits + \
        " |Epochs amount: " + self.epochs_amount + \
        " |Best and tournament chromosome amount: " + self.best_and_tournament_chromo_amount + \
        " |Elite Strategy amount: " + self.elite_amount + \
        " |Cross probability: " + self.cross_method + \
        " |Mutation probability: " + self.mutation_method + \
        " |Inversion probability: " + self.inversion_probability + \
        " |Selection method: " + self.selection_method + \
        " |Cross method: " + self.cross_method + \
        " |Mutation method: " + self.mutation_method + \
        " |Maximization: " + str(self.maximization)