from GUI import GUI
from Calculations import Calculations
from Selections import Selections
from Cross import Cross
from Mutation import Mutation
from Inversion import Inversion
from Specimen import Specimen

def main():
    configuration = GUI.openGUI()
    specimen_list = Calculations.generate_specimen_list(configuration)
    for i in range(int(configuration.epochs_amount)):
        print('==================| ' + str(i) + ' epoch |==================')
        if(i==0):
            next_spec_list = one_epoch(configuration, specimen_list)
        else:
            spec_after_elite_strategy = add_elite_strategy(configuration, next_spec_list)
            next_spec_list = one_epoch(configuration, spec_after_elite_strategy)
    #print('\n'.join(map(str, specimen_after_mutation)))

def one_epoch(configuration, specimen_list):
    specimen_after_selection = Selections.choose_selection(configuration, specimen_list)
    specimen_after_crossover = Cross.choose_crossover(configuration, specimen_after_selection)
    specimen_after_mutation = Mutation.choose_mutation(configuration, specimen_after_crossover)
    specimen_after_inversion = Inversion.inversion(configuration, specimen_after_mutation)
    print('[|][|]Final[|][|]')
    print('\n'.join(map(str, specimen_after_inversion)))
    return specimen_after_inversion

def add_elite_strategy(configuration, next_spec_list):
    spec_after_elite_strategy = list(next_spec_list)

    for i in range(int(configuration.elite_amount)):

        binary_x = Calculations.binary_representation(configuration.bits)
        binaryStr_x1 = Calculations.convertListToString(binary_x[0])
        binaryStr_x2 = Calculations.convertListToString(binary_x[1])

        spec_after_elite_strategy.append(Calculations.generate_specimen(configuration, binaryStr_x1, binaryStr_x2))

    configuration.population = int(configuration.population) + int(configuration.elite_amount)
    return spec_after_elite_strategy


    
if __name__ == "__main__":
    main()