from tkinter.constants import X
from Configuration import Configuration
from GUI import GUI
from Calculations import Calculations
from Specimen import Specimen
from Selections import Selections
from Enums.SelectionMethod import SelectionMethod

def main():
    configuration = GUI.openGUI()
    #configuration = Configuration(10, -10, 25, 15, 0, 3, 0, 0, 0, 0, SelectionMethod.ROULETTE.name, 0, 0, False)
    specimen_list = Calculations.generate_specimen_list(configuration)
    specimen_after_selection = Selections.choose_selection(configuration, specimen_list)
    #print('\n'.join(map(str, specimen_after_selection)))


if __name__ == "__main__":
    main()