import random
from Calculations import Calculations

class Inversion:
    def inversion(Configuration, specimen_after_mutation):
        print('|Inversion|')
        inverted_list = []

        for spec in specimen_after_mutation:
            inversion_prob_roll = round(random.uniform(0, 1), 2)

            if(inversion_prob_roll<float(Configuration.inversion_probability) or float(Configuration.inversion_probability) == 1):
                # x1
                print('Spec x1 BEFORE: ' + str(spec.binary_x1))
                temp = []
                how_many_to_change = random.randrange(0, int(Configuration.bits)-1)
                last_index = int(Configuration.bits) - (int(how_many_to_change))
                range_of_bits = random.randrange(0, int(last_index))
                temp.append(spec.binary_x1[:range_of_bits])
                temp.append(spec.binary_x1[range_of_bits:how_many_to_change])
                temp.append(spec.binary_x1[how_many_to_change:])
                print(temp[0] + ',' + temp[1] + ',' + temp[2])
                temp[1] = temp[1][::-1]
                print('Reversed middle piece: ' + temp[1])
                # x2
                print('Spec x2 BEFORE: ' + str(spec.binary_x2))
                how_many_to_change = random.randrange(0, int(Configuration.bits)-1)
                last_index = int(Configuration.bits) - (int(how_many_to_change))
                range_of_bits = random.randrange(0, int(last_index))
                temp.append(spec.binary_x2[:range_of_bits])
                temp.append(spec.binary_x2[range_of_bits:how_many_to_change])
                temp.append(spec.binary_x2[how_many_to_change:])
                print(temp[3] + ',' + temp[4] + ',' + temp[5])
                temp[4] = temp[4][::-1]
                print('Reversed middle piece: ' + temp[4])

                inversed_specimen = Calculations.generate_specimen(Configuration, temp[0]+temp[1]+temp[2], temp[3]+temp[4]+temp[5])
                inverted_list.append(inversed_specimen)
            else:
                print('Inversion failed')
                inverted_list.append(spec)

        return inverted_list