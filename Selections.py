from Configuration import Configuration
from Enums.SelectionMethod import SelectionMethod
import math

class Selections:

    def choose_selection(Configuration, specimen_list):
        if(Configuration.selection_method == SelectionMethod.BEST.name):
            Selections.best_selection(Configuration, specimen_list)
        if(Configuration.selection_method == SelectionMethod.TOURNAMENT.name):
            print("TOURNAMENT")
        if(Configuration.selection_method == SelectionMethod.ROULETTE.name):
            print("ROULETTE")

    pass

    def best_selection(Configuration, specimen_list):
        winners = []
        if(Configuration.maximization):
            #Highest num -> Lowest num
            newlist = sorted(specimen_list, key=lambda x: x.fitness_function, reverse=True)
        else:
            #Lowest num -> Highest num
            newlist = sorted(specimen_list, key=lambda x: x.fitness_function, reverse=False)
        #print('\n'.join(map(str, newlist)))
        how_many_winners = len(specimen_list) * Configuration.best_and_tournament_chromo_amount

        if (float(how_many_winners) % 1) >= 0.5:
            how_many_winners = math.ceil(how_many_winners)
        else:
            how_many_winners = round(how_many_winners)
            
        winners = newlist[:how_many_winners]
        #print('\n'.join(map(str, winners)))
        return winners

    #def tournament_selection():
