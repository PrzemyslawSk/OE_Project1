from Configuration import Configuration
from Enums.CrossMethod import CrossMethod
import numpy as np
import math
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
    # One Point crossover randomly selects a partition point in the chromosome vector and takes the head and tail of 
    # parent_1 and parent_2 respectively to for the new chromosome         
    # We are making the assumption that the parent_1 vector is one dimensional
        one = []
        parent_collection = [specimen_after_selection[x:x+2] for x in range(0, len(specimen_after_selection), 2)]
        crossover_flag = np.random.random() < float(Configuration.cross_probability)
        which_parent = np.random.choice(np.array(["Parent 1", "Parent 2"]))
        # Wyciagamy tylko z pierwszej listy w liście parentsów. Bedzie trzeba dodać pętle która iteruje po każdej liście
        # znajdującej się w liście "parent_collection".
        # Example: parent_1 = parent_collection[i][0]
        #          parent_2 = parent_collection[i][1]
        parent_1 = parent_collection[0]
        parent_2 = parent_collection[1]
        if crossover_flag == True:
            partition = np.random.randint(0, parent_1.shape[0])
            if which_parent == "Parent 1":
                one = parent_1
                one[partition:] = parent_2[partition:]
            elif which_parent == "Parent 2":
                one = parent_2
                one[partition:] = parent_1[partition:]
        else:
            # There is probability (1 - p) that we will not perform crossover
            # In such an event one takes the gene of one of the parents (randomly selected)
            if which_parent == "Parent 1":
                one = parent_1
            elif which_parent == "Parent 2":
                one = parent_2

        print('|one_point_crossover|')
        print('\n'.join(map(str, one)))
        return one

    def two_point_crossover(Configuration, specimen_after_selection):
    # Two Point crossover is similar to one point, except now we have to reference points and it is the portion 
    # in between that gets swapped
        two = []
        parent_collection = [specimen_after_selection[x:x+2] for x in range(0, len(specimen_after_selection), 2)]
        crossover_flag = np.random.random() < (Configuration.cross_probability)
        which_parent = np.random.choice(np.array(["Parent 1", "Parent 2"]))
        parent_1 = parent_collection[0]
        parent_2 = parent_collection[1]
        if crossover_flag == True:
            lower_limit = np.random.randint(0, parent_1.shape[0]-1)
            upper_limit = np.random.randint(lower_limit+1, parent_1.shape[0]) 
            if which_parent == "Parent 1":
                two = parent_1
                two[lower_limit:upper_limit+1] = parent_2[lower_limit:upper_limit+1]
            elif which_parent == "Parent 2":
                two = parent_2
                two[lower_limit:upper_limit+1] = parent_1[lower_limit:upper_limit+1] 
        else:
            # There is probability (1 - p) that we will not perform crossover
            # In such an event one takes the gene of one of the parents (randomly selected)
            if which_parent == "Parent 1":
                two = parent_1
            elif which_parent == "Parent 2":
                two = parent_2

        print('|two_point_crossover|')
        print('\n'.join(map(str, two)))
        return two
        
    def three_point_crossover(Configuration, specimen_after_selection, crossover_flag, which_parent):
        parent_collection = [specimen_after_selection[x:x+2] for x in range(0, len(specimen_after_selection), 2)]
        crossover_flag = np.random.random() < (Configuration.cross_probability)
        which_parent = np.random.choice(np.array(["Parent 1", "Parent 2"]))
        parent_1 = parent_collection[0]
        parent_2 = parent_collection[1]
        if crossover_flag == True:
            list(parent_1(range(Configuration.int(bits)), 3))
            lower = list[0]
            mid = list[1]
            upper = list[2]
            if which_parent == "Parent 1":
                three = parent_1
                three[low:mid:upper] = parent_2[low:mid:upper]
            elif which_parent == "Parent 2":
                three = parent_2
                three[low:mid:upper] = parent_1[low:mid:upper]
        else:
            # There is probability (1 - p) that we will not perform crossover
            # In such an event one takes the gene of one of the parents (randomly selected)
            if which_parent == "Parent 1":
                three = parent_1
            elif which_parent == "Parent 2":
                three = parent_2

        print('|two_point_crossover|')
        print('\n'.join(map(str, three)))
        return three
        
    def homo_crossover(Configuration, specimen_after_selection, crossover_flag, which_parent):
    # Uniform randomly selects indexes with a uniform distribution to be swapped during crossover
    # Unlike the previous two methods, the genes to be swapped do not have to be in a sequence
        homo = []
        parent_collection = [specimen_after_selection[x:x+2] for x in range(0, len(specimen_after_selection), 2)]
        crossover_flag = np.random.random() < (Configuration.cross_probability)
        which_parent = np.random.choice(np.array(["Parent 1", "Parent 2"]))
        parent_1 = parent_collection[0]
        parent_2 = parent_collection[1]
        if crossover_flag == True:
            random_sequence = np.random.choice(np.arange(parent_1.shape[0]), np.random.randint(1, parent_1.shape[0]), replace = False)
            if which_parent == "Parent 1":
                homo = parent_1
                homo[np.sort(random_sequence)] = parent_2[np.sort(random_sequence)]
            elif which_parent == "Parent 2":
                homo = parent_2
                homo[np.sort(random_sequence)] = parent_1[np.sort(random_sequence)]
        else:
            # There is probability (1 - p) that we will not perform crossover
            # In such an event one takes the gene of one of the parents (randomly selected)
            if which_parent == "Parent 1":
                homo = parent_1
            elif which_parent == "Parent 2":
                homo = parent_2
        print('|uniform_crossover|')
        print('\n'.join(map(str, homo)))
        return homo
        
    