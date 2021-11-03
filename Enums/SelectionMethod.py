from enum import Enum
# set of symbolic names (members) bound to unique, constant values
class SelectionMethod(Enum):
    BEST = 0
    ROULETTE = 1
    TOURNAMENT = 2