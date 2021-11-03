class Specimen:
    #x1 x2 - binary representations
    #calc_binary_x1,x2 - calculated binary representation
    def __init__(self, binary_x1, binary_x2, x1, x2, fitness_function):
        self.binary_x1 = binary_x1
        self.binary_x2 = binary_x2
        self.x1 = x1
        self.x2 = x2
        self.fitness_function = fitness_function
        pass

    def __str__(self):
        return "x1:" + str(self.x1) + \
        ", x2:" + str(self.x2) + \
        ", fitness:" + str(self.fitness_function)