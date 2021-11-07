from Enums.SelectionMethod import SelectionMethod
import math
import random

class Selections:

    def choose_selection(Configuration, specimen_list):
        specimen_after_selection = []
        if(Configuration.selection_method == SelectionMethod.BEST.name):
            specimen_after_selection = Selections.best_selection(Configuration, specimen_list)
        if(Configuration.selection_method == SelectionMethod.TOURNAMENT.name):
            specimen_after_selection = Selections.tournament_selection(Configuration, specimen_list)
        if(Configuration.selection_method == SelectionMethod.ROULETTE.name):
            specimen_after_selection = Selections.roulette_selection(Configuration, specimen_list)
        return specimen_after_selection

    def best_selection(Configuration, specimen_list):
        winners = []
        newlist = sorted(specimen_list, key=lambda x: x.fitness_function, reverse=Configuration.maximization)
        print('|Sorted specimen list|')
        print('\n'.join(map(str, newlist)))
        how_many_winners = Configuration.best_and_tournament_chromo_amount

        if (float(how_many_winners) % 1) >= 0.5:
            how_many_winners = math.ceil(how_many_winners)
        else:
            how_many_winners = round(how_many_winners)
            
        winners = newlist[:how_many_winners]
        print('|Winners|')
        print('\n'.join(map(str, winners)))
        return winners

    def tournament_selection(Configuration, specimen_list):
        tournament_winners = []
        tournaments = [specimen_list[x:x+int(Configuration.best_and_tournament_chromo_amount)] for x in range(0, len(specimen_list), int(Configuration.best_and_tournament_chromo_amount))]

        #display all tournaments
        cnt = 1
        for lst in tournaments:
            print(str(cnt) + '|\n' + '\n'.join(map(str, lst)))
            cnt += 1

        for tournament in tournaments:
            sorted_tournament = sorted(tournament, key=lambda x: x.fitness_function, reverse=Configuration.maximization)
            tournament_winners.append(sorted_tournament[0])
        
        print('==Winners==\n' + '\n'.join(map(str, tournament_winners)))
        return tournament_winners

    def roulette_selection(Configuration, specimen_list):
        winners = []
        for i in range(int(Configuration.best_and_tournament_chromo_amount)):
            sum_of_all = 0
            max_range = 0
            win_prob = round(random.uniform(0, 1), 18)

            print(f'{i}|List of specimen|\n' + '\n'.join(map(str, specimen_list)))
            for spec in specimen_list:
                if(Configuration.maximization):
                    sum_of_all += spec.fitness_function
                else:
                    sum_of_all += 1/spec.fitness_function
            print('\nSum of all y: ' + str(sum_of_all))
            print('Win range: ' + str(win_prob))
            print(f'\n{i}|Probability for each specimen with winner|')
            for spec in specimen_list:
                min_range = max_range
                if(Configuration.maximization):
                    prob = spec.fitness_function / sum_of_all
                else:
                    prob = 1/spec.fitness_function / sum_of_all
                max_range += prob
                if(min_range<win_prob and max_range>win_prob):
                    winner = spec
                    print(' v Winner below v')
                print(prob)
            winners.append(winner)
            i += 1
        print(f'|Winners|')
        print('\n'.join(map(str, winners)))
        return winners