from numpy.random import randint
from Specimen import Specimen
# perform calculations
class Calculations:
    def generate_specimen_list(configuration):
        specimen_list = []
        for i in range(configuration.population):
            binary_x = Calculations.binary_representation(configuration.bits)

            binaryStr_x1 = Calculations.convertListToString(binary_x[0])
            binaryStr_x2 = Calculations.convertListToString(binary_x[1])

            x1 = Calculations.calculate_binary_representation(configuration.range_a, configuration.range_b, configuration.bits, binaryStr_x1)
            x2 = Calculations.calculate_binary_representation(configuration.range_a, configuration.range_b, configuration.bits, binaryStr_x2)

            fitness_function = Calculations.calculate_fitness_function(x1, x2)

            specimen_list.append(Specimen(binaryStr_x1, binaryStr_x2, x1, x2, fitness_function))
        #print('\n'.join(map(str, specimen_list)))
        return specimen_list
        
    # create binary x1 and x2
    def binary_representation(number_of_bits):
        binary_x1 = list(randint(0, 2, number_of_bits))
        binary_x2 = list(randint(0, 2, number_of_bits))
        return [binary_x1, binary_x2]
    def convertListToString(list):
        str1 = ""
        for item in list:
            str1 += str(item)
        return str1
    def calculate_binary_representation(range_a, range_b, number_of_bits, binaries):
        x = range_a + int(binaries, 2) * (range_b - range_a) / (2**number_of_bits - 1)
        return x
    # From calculated binary x1 and x2 we calculate fitness function
    # We use 'booth function'
    def calculate_fitness_function(x1, x2):
        calc = (x1 + 2 * x2 - 7)**2 + (2 * x1 + x2 - 5)**2
        return calc
    