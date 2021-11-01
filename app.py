from tkinter.constants import X
from Configuration import Configuration
from GUI import GUI
from Calculations import Calculations
from Specimen import Specimen
from Selections import Selections

def main():
    configuration = GUI.openGUI()
    specimen_list = Calculations.generate_specimen_list(configuration)
    Selections.choose_selection(configuration, specimen_list)


if __name__ == "__main__":
    main()