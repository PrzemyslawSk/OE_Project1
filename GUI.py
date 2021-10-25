from tkinter import *
from typing import Collection
from Configuration import Configuration
from Enums.CrossMethod import CrossMethod
from Enums.MutationMethod import MutationMethod
from Enums.SelectionMethod import SelectionMethod

class GUI():

    def openGUI():
        root = Tk()
        root.title("Genetic Algorithm")

        def myClick():
            configuration = Configuration(entryBeginRange.get(), entryEndRange.get(), entryPopulation.get(),
            entryBits.get(), entryEpchos.get(), entryBestTournament.get(), entryElite.get(), entryCross.get(),
            entryMutation.get(), entryInversion.get(), chooseSelection.get(), chooseCross.get(), chooseMutation.get(), maximization.get())

            print(configuration)
            pass

        # Labels with entries
        labelBeginRange = Label(root, text="Begin of the range")
        entryBeginRange = Entry(root, width=50)
        labelEndRange = Label(root, text="End of the range")
        entryEndRange = Entry(root, width=50)
        labelPopulation = Label(root, text="Population amount")
        entryPopulation = Entry(root, width=50)
        labelBits = Label(root, text="Number of bits")
        entryBits = Entry(root, width=50)
        labelEpchos = Label(root, text="Epochs amount")
        entryEpchos = Entry(root, width=50)
        labelBestTournament = Label(root, text="Best and tournament chromosome amount")
        entryBestTournament = Entry(root, width=50)
        labelElite = Label(root, text="Elite Strategy amount")
        entryElite = Entry(root, width=50)
        labelCross = Label(root, text="Cross probability")
        entryCross = Entry(root, width=50)
        labelMutation = Label(root, text="Mutation probability")
        entryMutation = Entry(root, width=50)
        labelInversion = Label(root, text="Inversion probability")
        entryInversion = Entry(root, width=50)

        labelSelectionMethod = Label(root, text="Choose selection method")
        chooseSelection = StringVar(value=SelectionMethod.BEST.name)
        chooseSelection.set(value=SelectionMethod.BEST.name)
        dropSelection = OptionMenu(root, chooseSelection, *[option.name for option in SelectionMethod])

        labelCrossMethod = Label(root, text="Choose cross method")
        chooseCross = StringVar(value=CrossMethod.ONE_POINT.name)
        chooseCross.set(value=CrossMethod.ONE_POINT.name)
        dropCross = OptionMenu(root, chooseCross, *[option.name for option in CrossMethod])

        labelMutationMethod = Label(root, text="Choose mutation method")
        chooseMutation = StringVar(value=MutationMethod.ONE_POINT.name)
        chooseMutation.set(value=MutationMethod.ONE_POINT.name)
        dropMutation = OptionMenu(root, chooseMutation, *[option.name for option in MutationMethod])

        maximization = BooleanVar()
        checkbuttonMaximization = Checkbutton(root, text="Maximization", variable=maximization, onvalue=True, offvalue=False)

        buttonStart = Button(root, text="Start", padx=100, command=myClick)


        # Positions
        labelBeginRange.grid(row=0, column=0)
        entryBeginRange.grid(row=0, column=1)
        labelEndRange.grid(row=1, column=0)
        entryEndRange.grid(row=1, column=1)
        labelPopulation.grid(row=2, column=0)
        entryPopulation.grid(row=2, column=1)
        labelBits.grid(row=3, column=0)
        entryBits.grid(row=3, column=1)
        labelEpchos.grid(row=4, column=0)
        entryEpchos.grid(row=4, column=1)
        labelBestTournament.grid(row=5, column=0)
        entryBestTournament.grid(row=5, column=1)
        labelElite.grid(row=6, column=0)
        entryElite.grid(row=6, column=1)
        labelCross.grid(row=7, column=0)
        entryCross.grid(row=7, column=1)
        labelMutation.grid(row=8, column=0)
        entryMutation.grid(row=8, column=1)
        labelInversion.grid(row=9, column=0)
        entryInversion.grid(row=9, column=1)

        labelSelectionMethod.grid(row=10, column=0)
        dropSelection.grid(row=10, column=1)
        labelCrossMethod.grid(row=11, column=0)
        dropCross.grid(row=11, column=1)
        labelMutationMethod.grid(row=12, column=0)
        dropMutation.grid(row=12, column=1)

        checkbuttonMaximization.grid(row=13, column=0)

        buttonStart.grid(row=13, column=1)

        root.mainloop()
    