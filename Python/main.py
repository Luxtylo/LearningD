"""

This main file contains a command-line launcher for all my test projects.

"""

# Imports
import os


# Main function
def main():
	programList = listPrograms()
	program = getSelection(programList)


# List programs
def listPrograms():

	for i in os.walk(".", topdown = True):
		programTuple = i

	programList = []

	for j in range(len(programTuple[-1])):

		if j != 0:

			programList.append(programTuple[-1][j])

			programNameList = programTuple[-1][j].split(".")

			programName = str(programNameList[0])

			print(programName)

			#exec("import " + programName)

	print("Programs available:")

	for item in range(len(programList)):

		print(str(item + 1) + ". " + programList[item])

	return programList


# Get program selection
def getSelection(programs):
	pass


# Run correct program


# Run main function
main()