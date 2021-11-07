from GUI import GUI
from Calculations import Calculations
from Selections import Selections
from Cross import Cross
from Mutation import Mutation
from Inversion import Inversion

def main():
    configuration = GUI.openGUI()
    specimen_list = Calculations.generate_specimen_list(configuration)
    for i in range(int(configuration.epochs_amount)):
        print('==================| ' + str(i) + ' epoch |==================')
        if(i==0):
            next_spec_list = one_epoch(configuration, specimen_list)
        else:
            next_spec_list = one_epoch(configuration, next_spec_list)
    #print('\n'.join(map(str, specimen_after_mutation)))

def one_epoch(configuration, specimen_list):
    specimen_after_selection = Selections.choose_selection(configuration, specimen_list)
    specimen_after_crossover = Cross.choose_crossover(configuration, specimen_after_selection)
    specimen_after_mutation = Mutation.choose_mutation(configuration, specimen_after_crossover)
    specimen_after_inversion = Inversion.inversion(configuration, specimen_after_mutation)
    print('[|][|]Final[|][|]')
    print('\n'.join(map(str, specimen_after_inversion)))
    return specimen_after_inversion

if __name__ == "__main__":
    main()