from Enums.CrossMethod import CrossMethod
from Calculations import Calculations
import random

class Cross:
    def choose_crossover(Configuration, specimen_after_selection):
        specimen_after_crossover = []
        if(Configuration.cross_method == CrossMethod.ONE_POINT.name):
            specimen_after_crossover = Cross.one_point_crossover(Configuration, specimen_after_selection)
        if(Configuration.cross_method == CrossMethod.TWO_POINTS.name):
            specimen_after_crossover = Cross.two_point_crossover(Configuration, specimen_after_selection)
        if(Configuration.cross_method == CrossMethod.THREE_POINTS.name):
            specimen_after_crossover = Cross.three_point_crossover(Configuration, specimen_after_selection)
        if(Configuration.cross_method == CrossMethod.HOMO.name):
            specimen_after_crossover = Cross.homo_crossover(Configuration, specimen_after_selection)
        return specimen_after_crossover
        
    def one_point_crossover(Configuration, specimen_after_selection):
        #print('|Crossing|')
        crossed_list = list(specimen_after_selection)
        while(len(crossed_list)<int(Configuration.population)):
            tempList = []
            point = random.randrange(1, int(Configuration.bits)-1)
            cross_prob_roll = round(random.uniform(0, 1), 2)
            #print('CROSS PROB: ' + str(cross_prob_roll))

            random_spec1 = (random.choice(specimen_after_selection))
            random_spec2 = (random.choice(specimen_after_selection))

            while(random_spec1==random_spec2):
                random_spec2 = (random.choice(specimen_after_selection))

            if(cross_prob_roll<float(Configuration.cross_probability) or float(Configuration.cross_probability) == 1):
                # x1
                tempList.append(random_spec1.binary_x1[:point])
                tempList.append(random_spec2.binary_x1[point:])
                #print('x1: ' + tempList[0] + ',' + tempList[1])

                # x2
                tempList.append(random_spec1.binary_x2[:point])
                tempList.append(random_spec2.binary_x2[point:])
                #print('x2: ' + tempList[2] + ',' + tempList[3])

                new_specimen = Calculations.generate_specimen(Configuration, tempList[0]+tempList[1], tempList[2]+tempList[3])
                crossed_list.append(new_specimen)
            #else:
                #print('Crossing failed')
        return crossed_list


    def two_point_crossover(Configuration, specimen_after_selection):
        pass
        
    def three_point_crossover(Configuration, specimen_after_selection):
        pass
        
    def homo_crossover(Configuration, specimen_after_selection):
        pass
    