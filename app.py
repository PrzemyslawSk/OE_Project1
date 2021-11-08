from GUI import GUI
from Calculations import Calculations
from Selections import Selections
from Cross import Cross
from Mutation import Mutation
from Inversion import Inversion
import csv
from Specimen import Specimen
import timeit
import matplotlib.pyplot as plt
import pandas as pd

def main():
    winners_after_epochs = []
    configuration = GUI.openGUI()
    start = timeit.default_timer()

    specimen_list = Calculations.generate_specimen_list(configuration)
    for i in range(int(configuration.epochs_amount)):
        print('==================| ' + str(i) + ' epoch |==================')
        if(i==0):
            next_spec_list = one_epoch(configuration, specimen_list)
            winner = best_spec_after_epoch(configuration, next_spec_list)
            winners_after_epochs.append(winner)
        else:
            spec_after_elite_strategy = add_elite_strategy(configuration, next_spec_list)
            next_spec_list = one_epoch(configuration, spec_after_elite_strategy)
            winner = best_spec_after_epoch(configuration, next_spec_list)
            winners_after_epochs.append(winner)
    
    #print('|winners after epochs|')
    #print('\n'.join(map(str, winners_after_epochs)))
    write_to_csv(winners_after_epochs)
    generate_charts(configuration, winners_after_epochs)
    stop = timeit.default_timer()
    print('Time: ', stop - start)  
    #print('\n'.join(map(str, specimen_after_mutation)))

def one_epoch(configuration, specimen_list):
    specimen_after_selection = Selections.choose_selection(configuration, specimen_list)
    specimen_after_crossover = Cross.choose_crossover(configuration, specimen_after_selection)
    specimen_after_mutation = Mutation.choose_mutation(configuration, specimen_after_crossover)
    specimen_after_inversion = Inversion.inversion(configuration, specimen_after_mutation)
    #print('[|][|]Final[|][|]')
    #print('\n'.join(map(str, specimen_after_inversion)))
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

def write_to_csv(list):
    file = open("Data.csv", "w")
    str = "Epoch, x1, x2, Fitness function \n"
    file.write(str)
    for i in range(len(list)):
        str = f'{i + 1}, {list[i].x1}, {list[i].x2}, {list[i].fitness_function}\n'
        file.write(str)
    file.close()
    
def best_spec_after_epoch(Configuration, specimen_list):
    newlist = sorted(specimen_list, key=lambda x: x.fitness_function, reverse=Configuration.maximization)
            
    winner = newlist[0]
    return winner

def generate_charts(configuration, list):
    data = pd.read_csv('Data.csv')
    
    fig = plt.figure(figsize=(6.8, 4.2))
    x = range(len(data['Epoch']))
    plt.plot(x, data[' Fitness function '], 'b.-')
    plt.xticks(x, data['Epoch'])

    plt.title('Winners after each epoch')
    plt.xlabel('Epoch')
    plt.ylabel('Fitness function')

    fig.savefig('winners_after_each_epoch.png', dpi=fig.dpi)

if __name__ == "__main__":
    main()