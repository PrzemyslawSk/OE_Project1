from Enums.MutationMethod import MutationMethod
import random
from Calculations import Calculations

class Mutation:
    def choose_mutation(Configuration, specimen_after_crossover):
        specimen_after_mutation = []
        if(Configuration.mutation_method == MutationMethod.ONE_POINT.name):
            specimen_after_mutation = Mutation.one_point_mutation(Configuration, specimen_after_crossover)
        if(Configuration.mutation_method == MutationMethod.TWO_POINTS.name):
            specimen_after_mutation = Mutation.two_point_mutation(Configuration, specimen_after_crossover)
        return specimen_after_mutation

    def one_point_mutation(Configuration, specimen_after_crossover):
        print('|One point mutation|')
        mutated_list = []

        for spec in specimen_after_crossover:
            mutation_prob_roll = round(random.uniform(0, 1), 2)
            
            if(mutation_prob_roll<float(Configuration.mutation_probability)):
                random_bit1 = random.randrange(0, int(Configuration.bits))
                random_bit2 = random.randrange(0, int(Configuration.bits))
                print('=======================================')
                print('x1| ' + str(random_bit1) + ' BIT| ' + spec.binary_x1)
                print('x2| ' + str(random_bit2) + ' BIT| ' + spec.binary_x2)
                # x1
                if(spec.binary_x1[random_bit1] == "0"):
                    temp = list(spec.binary_x1)
                    temp[random_bit1] = "1"
                    spec.binary_x1 = "".join(temp)
                else:
                    temp = list(spec.binary_x1)
                    temp[random_bit1] = "0"
                    spec.binary_x1 = "".join(temp)
                # x2
                if(spec.binary_x2[random_bit2] == "0"):
                    temp = list(spec.binary_x2)
                    temp[random_bit2] = "1"
                    spec.binary_x2 = "".join(temp)
                else:
                    temp = list(spec.binary_x2)
                    temp[random_bit2] = "0"
                    spec.binary_x2 = "".join(temp)
            else:
                print('Mutation failed')
            new_spec = Calculations.generate_specimen(Configuration, spec.binary_x1, spec.binary_x2)
            mutated_list.append(new_spec)
            print('x1 after mutation: ' + str(new_spec.binary_x1))
            print('x2 after mutation: ' + str(new_spec.binary_x2))
        return mutated_list

    def two_point_mutation(Configuration, specimen_after_crossover):
        print('|Two point mutation|')
        mutated_list = []
        number_ = 0
        for spec in specimen_after_crossover:
            print('NR ' + str(number_))
            mutation_prob_roll = round(random.uniform(0, 1), 1)
            for b in range(2):
                if(mutation_prob_roll<float(Configuration.mutation_probability) or float(Configuration.mutation_probability) == 1):
                    random_bit1 = random.randrange(0, int(Configuration.bits))
                    random_bit2 = random.randrange(0, int(Configuration.bits))
                    print('=======================================')
                    print('x1| ' + str(random_bit1) + ' BIT| ' + spec.binary_x1)
                    print('x2| ' + str(random_bit2) + ' BIT| ' + spec.binary_x2)
                    # x1
                    if(spec.binary_x1[random_bit1] == "0"):
                        temp = list(spec.binary_x1)
                        temp[random_bit1] = "1"
                        spec.binary_x1 = "".join(temp)
                    else:
                        temp = list(spec.binary_x1)
                        temp[random_bit1] = "0"
                        spec.binary_x1 = "".join(temp)
                    # x2
                    if(spec.binary_x2[random_bit2] == "0"):
                        temp = list(spec.binary_x2)
                        temp[random_bit2] = "1"
                        spec.binary_x2 = "".join(temp)
                    else:
                        temp = list(spec.binary_x2)
                        temp[random_bit2] = "0"
                        spec.binary_x2 = "".join(temp)
                else:
                    print('Mutation failed')

            new_spec = Calculations.generate_specimen(Configuration, spec.binary_x1, spec.binary_x2)
            mutated_list.append(new_spec)
            print('x1 after mutation: ' + str(new_spec.binary_x1))
            print('x2 after mutation: ' + str(new_spec.binary_x2))
            number_ += 1

        return mutated_list